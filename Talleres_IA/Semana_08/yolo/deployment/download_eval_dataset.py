"""Download complete validation/test partitions without downloading unused train images."""
from pathlib import Path
import concurrent.futures
import io
import json
import tempfile
import zipfile
import requests

class RemoteZipReader(io.RawIOBase):
    def __init__(self, url, size):
        self.url, self.size, self.position = url, size, 0
        self.cache = {}
        self.session = requests.Session()
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.position
    def seek(self, offset, whence=0):
        self.position = offset if whence == 0 else self.position + offset if whence == 1 else self.size + offset
        return self.position
    def read(self, size=-1):
        if size < 0: size = self.size - self.position
        size = min(size, self.size - self.position)
        parts = []
        block_size = 4 * 1024 * 1024
        while size > 0:
            block = self.position // block_size
            start = block * block_size
            if block not in self.cache:
                response = self.session.get(self.url, headers={
                    "Range": f"bytes={start}-{min(start + block_size, self.size)-1}"}, timeout=90)
                if response.status_code != 206:
                    raise RuntimeError("The download server must support HTTP Range")
                self.cache[block] = response.content
            piece = self.cache[block][self.position-start:self.position-start+size]
            if not piece: raise IOError("Empty byte range")
            parts.append(piece)
            self.position += len(piece)
            size -= len(piece)
        return b"".join(parts)

def download_evaluation_dataset(api_key, destination="datasets/logistics_eval"):
    """Exact version 2, all exported valid/test images and labels; no subsampling."""
    destination = Path(destination)
    marker = destination / "download_complete.json"
    if marker.exists():
        return destination.resolve()
    try:
        response = requests.get(
            "https://api.roboflow.com/large-benchmark-datasets/logistics-sz9jr/2/yolov8",
            params={"api_key": api_key}, timeout=90)
        response.raise_for_status()
        url = response.json()["export"]["link"]
        head = requests.head(url, allow_redirects=True, timeout=90)
        head.raise_for_status()
        size = int(head.headers["Content-Length"])
        remote = RemoteZipReader(url, size)
        with zipfile.ZipFile(remote) as archive:
            infos = archive.infolist()
            selected = [info for info in infos if info.filename.startswith(("valid/", "test/"))
                        or "/" not in info.filename]
            # Local records are contiguous by split in this export. Compute spans
            # from actual ZIP offsets rather than relying on fixed byte positions.
            selected_names = {info.filename for info in selected}
            ordered = sorted(infos, key=lambda info: info.header_offset)
            spans = []
            for i, info in enumerate(ordered):
                if info.filename not in selected_names: continue
                end = ordered[i+1].header_offset if i+1 < len(ordered) else size
                spans.append((info.header_offset, end))
            spans.append((archive.start_dir, size))
        merged = []
        for start,end in sorted(spans):
            if merged and start <= merged[-1][1]: merged[-1] = (merged[-1][0],max(end,merged[-1][1]))
            else: merged.append((start,end))
        chunks = [(start,min(start+64*1024*1024,end)) for a,end in merged
                  for start in range(a,end,64*1024*1024)]
        destination.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory() as tmp:
            sparse_zip = Path(tmp)/"evaluation.zip"
            with sparse_zip.open("wb") as output: output.truncate(size)
            def fetch(chunk):
                a,b = chunk
                for attempt in range(3):
                    try:
                        result = requests.get(url,headers={"Range":f"bytes={a}-{b-1}"},stream=True,timeout=120)
                        if result.status_code != 206: raise RuntimeError("HTTP Range unavailable")
                        total = 0
                        with sparse_zip.open("r+b") as output:
                            output.seek(a)
                            for block in result.iter_content(1024*1024):
                                output.write(block); total += len(block)
                        if total != b-a: raise IOError("Incomplete range")
                        return total
                    except Exception:
                        if attempt == 2: raise
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
                downloaded = sum(pool.map(fetch,chunks))
            with zipfile.ZipFile(sparse_zip) as archive:
                for info in selected:
                    target = (destination/info.filename).resolve()
                    if not target.is_relative_to(destination.resolve()):
                        raise RuntimeError("Unsafe path in ZIP")
                    archive.extract(info,destination)
        # Paths from Roboflow exports must resolve relative to this new directory.
        import yaml
        config_path = destination/"data.yaml"
        config = yaml.safe_load(config_path.read_text())
        config.update(path=str(destination.resolve()),val="valid/images",test="test/images")
        config_path.write_text(yaml.safe_dump(config,sort_keys=False))
        counts = {split:len(list((destination/split/"images").glob("*"))) for split in ("valid","test")}
        marker.write_text(json.dumps({"source":"large-benchmark-datasets/logistics-sz9jr/2",
            "selection":"All exported validation and test images, no train", "counts":counts,
            "downloaded_bytes":downloaded},indent=2))
        print("Download complete:",counts)
        return destination.resolve()
    except Exception as error:
        raise RuntimeError("Dataset download failed; check network and Roboflow credentials. "
                           + type(error).__name__) from None
