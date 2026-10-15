"""Regression tests: real encoding, bundled weights and HTTP CLI failures."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest.mock import patch

import cv2
import imageio
import numpy as np
from PIL import Image

DEPLOYMENT = Path(__file__).resolve().parents[1] / 'Semana_08/yolo/deployment'


def load_script(name):
    spec = importlib.util.spec_from_file_location('taller_' + name, DEPLOYMENT / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VideoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = load_script('app')

    def test_even_odd_and_downscaled_video(self):
        with tempfile.TemporaryDirectory() as tmp:
            for height, width, limit, expected in [(64, 64, 960, (64, 64)),
                                                     (65, 67, 960, (64, 66)),
                                                     (65, 67, 32, (30, 32))]:
                with self.subTest(shape=(height, width), limit=limit):
                    source = Path(tmp) / 'input.mkv'
                    with imageio.get_writer(source, fps=5, codec='ffv1', macro_block_size=1,
                                            pixelformat='bgr0') as writer:
                        for i in range(3):
                            writer.append_data(np.full((height, width, 3), i * 40, dtype=np.uint8))
                    result = self.app.detect_video(str(source), 'yolov8n.pt', .25, .45, limit,
                                                   progress=lambda *a, **k: None)
                    try:
                        self.assertGreater(Path(result).stat().st_size, 0)
                        cap = cv2.VideoCapture(result)
                        frames = []
                        try:
                            while True:
                                ok, frame = cap.read()
                                if not ok:
                                    break
                                frames.append(frame.shape[:2])
                        finally:
                            cap.release()
                        self.assertEqual(frames, [expected] * 3)
                    finally:
                        Path(result).unlink(missing_ok=True)

    def test_invalid_video_raises(self):
        with self.assertRaises(ValueError):
            self.app.detect_video('/nonexistent/video.mp4', 'yolov8n.pt', .25, .45, 960)

    def test_encoder_failure_is_not_returned_as_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'input.mkv'
            with imageio.get_writer(source, fps=5, codec='ffv1', macro_block_size=1) as writer:
                writer.append_data(np.zeros((64, 64, 3), dtype=np.uint8))
            # Simulate a backend that silently writes an empty file.
            output = Path(tmp) / 'empty.mp4'
            output.touch()
            class SilentWriter:
                def write(self, frame): pass
                def release(self): pass
            with patch.object(self.app, '_make_writer', return_value=(SilentWriter(), str(output))):
                with self.assertRaises(RuntimeError):
                    self.app.detect_video(str(source), 'yolov8n.pt', .25, .45, 960)
            self.assertFalse(output.exists())

    def test_webcam_bundled_model_from_another_directory(self):
        webcam = load_script('app_webcam')
        self.assertIn('best.pt', webcam.MODEL_CHOICES)
        result = webcam.detect_frame(np.zeros((64, 64, 3), dtype=np.uint8), 'best.pt', .25, .45, 960)
        self.assertEqual(result.shape, (64, 64, 3))
        webcam.build_ui()
        self.app.build_ui()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args): pass
    def do_POST(self):
        self.rfile.read(int(self.headers['Content-Length']))
        status = 500 if self.path == '/error' else 200
        body = b'invalid json' if self.path == '/invalid' else json.dumps({'detections': []}).encode()
        self.send_response(status)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class ClientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def run_client(self, image, route='/ok'):
        return subprocess.run([sys.executable, str(DEPLOYMENT / 'client.py'), '--image', str(image),
                               '--url', f'http://127.0.0.1:{self.server.server_port}{route}'],
                              capture_output=True, text=True, timeout=60)

    def test_missing_image_returns_failure(self):
        self.assertNotEqual(self.run_client('/nonexistent/image.jpg').returncode, 0)

    def test_http_and_json_errors_return_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / 'input.png'
            Image.new('RGB', (64, 64)).save(image)
            for route in ['/error', '/invalid']:
                with self.subTest(route=route):
                    self.assertNotEqual(self.run_client(image, route).returncode, 0)

    def test_rgba_input_and_empty_detections_succeed(self):
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / 'input.png'
            Image.new('RGBA', (64, 64)).save(image)
            result = self.run_client(image)
            self.assertEqual(result.returncode, 0, result.stderr)
            with Image.open(Path(tmp) / 'input_annotated.jpg') as annotated:
                self.assertEqual(annotated.size, (64, 64))

    def test_unreadable_image_returns_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / 'input.jpg'
            image.write_text('not an image')
            self.assertNotEqual(self.run_client(image).returncode, 0)


if __name__ == '__main__':
    unittest.main()
