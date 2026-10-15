# Talleres de Inteligencia Artificial — semanas 4, 6, 7, 8 y 9

Los notebooks mantienen el nombre del archivo base y están organizados por semana. La semana 4 parte del repositorio de la estudiante; las demás, del repositorio del curso. No se ha subido nada a GitHub. Revisa las explicaciones y resultados antes de hacer tu entrega individual.

## Organización y orden

- `Semana_04/`: los tres notebooks revisados y ejecutados. El laboratorio incluye experimentos A/B/C, bonus, probabilidades de destino y pruebas del MDP. Se corrigió la conclusión de gamma=0,99 y la identificación de estados afectados por el piso.
- `Semana_06/challenge/`: ejecutar **01 → 02 → 03**. Contiene la solución de vinos, datos, pipelines, resultados CV, modelo y reporte final. `classification/` conserva los seis ejemplos de clase, adaptados a rutas locales y ejecutados; se corrigió la visualización del árbol cuando el campeón es regresión logística.
- `Semana_07/`: ejecutar Fashion-MNIST y luego ambos challenges. Incluye respuestas, entrenamientos, curvas, predicciones y resultados en `reports/`. Olivetti conserva el fallo de aprendizaje de la receta base y un diagnóstico adicional de centrado con resultado real, claramente separado.
- `Semana_08/transfer_learning/taller_transfer_learning_datos_propios_keras3.ipynb`: actividad completa de tres flores, dataset propio, fuentes, revisión, split, EfficientNetB0, fine-tuning y análisis de ocho imágenes con error. Incluye pesos finales. El notebook `CNN_Transfer_Keras3.ipynb` es el ejemplo guiado original de gatos/perros, sin nuevos espacios de actividad; se ejecutó completo, incluyendo entrenamiento, guardado, recarga y fine-tuning con el dataset completo.
- `Semana_08/yolo/Lecture_08_Yolo_Intro.ipynb`: ejercicio resuelto y ejecutado con una segunda imagen pública. Los dos ejemplos de entrenamiento usan los datasets públicos de Roboflow indicados por el profesor, 20 épocas y evaluación separada de test; conservan pesos en `models/` y métricas en `reports/`. `deployment/test.ipynb` evalúa `best.pt` del profesor sobre todas las imágenes exportadas de validación y test de logística. Consulta el estado efectivo de ejecución en `ESTADO_VALIDACION.md`.
- `Semana_09/tokenization_Introduction.ipynb`: reto de dolphin, tres operaciones vectoriales, PCA y análisis real con Word2Vec Google News completo.
- `Semana_09/05_ejercicio_nvidia_documentos.ipynb`: extracción del paper, chat con historial y streaming, interfaz Gradio, citas de página, reflexiones y pruebas locales. **NVIDIA real probado:** seis preguntas ejecutadas y respuestas guardadas en `nvidia_answers.json`. Se comprobó también la interfaz en el navegador. La prueba simulada se conserva como prueba unitaria separada.
- Los notebooks 03 y 04 de `Semana_09/` están ejecutados con NVIDIA real: chat, memoria, streaming, menús y prompt personalizado. Se adaptó Gradio para cargar `.env` local y usar servidores en 127.0.0.1. El ejemplo 01 de Ollama se ejecutó completo. El 02 de Hugging Face se ejecutó en su parte local; la inferencia remota está implementada y configurada, pero responde HTTP 402 por falta de créditos. El ejemplo de Ollama ya no ejecuta comandos de instalación Linux en macOS.

## Ejecutar localmente

Se probó con Python 3.11 en macOS arm64: CPU para los ejemplos iniciales y MPS para los entrenamientos y evaluaciones de YOLO. Desde esta carpeta:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install jupyterlab
python -m ipykernel install --user --name talleres-ia --display-name "Talleres IA"
jupyter lab
```

Selecciona el kernel **Talleres IA**. Abre cada notebook desde su carpeta; las rutas de datos son relativas a ella. Ejecuta de arriba abajo. Los modelos y datasets públicos se descargan la primera vez. Word2Vec descarga aproximadamente 1,6 GB; CIFAR-10 puede descargar lentamente desde Toronto. Estos datasets grandes no se duplican en la entrega.

El dataset de flores **sí está incluido** con `data_raw/`, `dataset/`, `image_sources.json` y `dataset_review.json`. Sus búsquedas y exclusiones están documentadas. La procedencia de las imágenes no equivale a una licencia de redistribución verificada. El script de entrenamiento reutiliza el dataset conservado en vez de cambiarlo silenciosamente al descargar de nuevo.

`wine.csv` y el CSV del ejemplo de cáncer no estaban en el repositorio del curso. Se reconstruyeron desde los datasets distribuidos por scikit-learn y se guardaron; esa decisión está documentada en las celdas correspondientes.

## Configuración de servicios

- **NVIDIA ya está configurado en este equipo:** `Semana_09/.env` contiene la clave y **no se incluye en el ZIP ni debe subirse a GitHub**. En otro equipo, copia `.env.example` a `.env` e introduce tu clave. Los notebooks 03, 04 y 05 están probados. Para abrir la interfaz del 05, cambia `LAUNCH_UI = True`; escucha solo en el equipo local. Las respuestas reales y su evaluación se conservan en el notebook y en `nvidia_answers.json`.
- **Roboflow ya está configurado en este equipo:** la clave está en `Semana_08/yolo/apikeys.env`, excluido del ZIP y de Git. En otro equipo, copia `apikeys.env.example` a `apikeys.env` y configura tu clave. El notebook de deployment lee ese mismo archivo desde la carpeta superior. Los datasets descargados y las carpetas `runs/` permanecen locales, pero no se duplican en el ZIP ni en GitHub. El helper de logística descarga aproximadamente 1,55 GB de validación y test, evitando el entrenamiento que no se utiliza. El acceso depende de los proyectos/versiones públicos del docente.
- **Ejemplos LLM locales:** Ollama debe instalarse por separado. Los ejemplos 01 y 02 requieren el entorno independiente de `requirements-ejemplos-llm.txt`; el token remoto ya está configurado localmente, pero la cuenta no tiene créditos de inferencia (HTTP 402). No se compró saldo.

No incluyas archivos `.env` reales en GitHub; el `.gitignore` los excluye. Las plantillas no contienen credenciales.

## Interpretación de las pruebas

`ESTADO_VALIDACION.md` indica qué se ejecutó realmente en cada archivo. No se consideran pruebas completas ni los análisis estáticos ni las pruebas con cliente simulado. Los resultados se mantienen dentro de los notebooks, sin errores de ejecución en los entregables ejecutados.

La semana 7 conserva el protocolo del enunciado, que utiliza test como validation durante fit. Se documenta que no es una evaluación completamente ciega y que para seleccionar hiperparámetros se necesita un conjunto de validación independiente.

Los originales clonados permanecen separados en el directorio de trabajo; los commits exactos están en `PROCEDENCIA.json`. La carpeta que debes revisar/subir es esta, no el entorno virtual ni las cachés de trabajo.

## Despliegue local de YOLO

Desde `Semana_08/yolo/deployment/`, ejecuta `python server.py --port 8010`. En otra terminal, usa `python client.py --image RUTA_IMAGEN --url http://127.0.0.1:8010/predict`. El cliente guarda una imagen anotada junto a la imagen de entrada. El servidor usa los pesos `best.pt` suministrados por el profesor y escucha en localhost.

El ejemplo SiteSafety contiene solo 4 imágenes de entrenamiento, 2 de validación y 3 de test: sus resultados no permiten validar un sistema real de seguridad industrial. No se presenta este dataset público como una recolección propia. Tampoco se conoce el split utilizado originalmente para entrenar el `best.pt` de logística; su evaluación no demuestra ausencia de solapamiento con su entrenamiento.

## Revisión final del 10 de octubre de 2026

Consulta `REVISION_PUNTO_POR_PUNTO.md`: 234 puntos documentados en 27 notebooks. Hay 26 notebooks ejecutados completos; solo queda sin comprobar satisfactoriamente la inferencia remota del notebook 02 de Hugging Face. Su parte local sí se probó.

Para reproducir Cats/Dogs con GPU en un Mac Apple Silicon, utiliza un entorno separado con `requirements-macos-metal.txt`, en lugar de mezclarlo con el entorno principal. Instala Jupyter y registra ese entorno como kernel. Los notebooks 01 y 02 de semana 9 usan el entorno LLM separado descrito abajo; el resto conserva las dependencias principales. Ollama se instala por separado; si no está en PATH, define OLLAMA_BIN en tu `.env` local. La ruta de este equipo no se distribuye como credencial ni como requisito de otro equipo.

## Correcciones de instalación y despliegue

Los notebooks 01 (Ollama) y 02 (Hugging Face) de semana 9 usan un **entorno separado**: Transformers 4.57.6 necesita huggingface_hub 0.36.2, incompatible con el requisito de Gradio 6.29.1 del entorno principal. No mezcles ambos archivos de dependencias.

Desde `Talleres_IA/`, crea y registra el entorno LLM:

```bash
python3.11 -m venv .venv-llm
source .venv-llm/bin/activate
python -m pip install -r requirements-ejemplos-llm.txt
python -m pip check
python -m ipykernel install --user --name talleres-ia-llm --display-name "Talleres IA LLM"
```

Selecciona **Talleres IA LLM** para los notebooks 01 y 02. Jupyter puede abrirse desde el entorno principal; los notebooks NVIDIA/Gradio siguen usando el kernel principal. Ollama se instala por separado y la inferencia remota necesita un token válido y acceso al proveedor.

El entorno principal declara ahora `imageio` e `imageio-ffmpeg`, incluido FFmpeg para generar video H.264. Reinstala sus dependencias con `python -m pip install -r requirements.txt` usando el entorno principal. Las aplicaciones de video y cámara buscan los pesos incluidos junto al script, aunque se inicien desde otra carpeta. La cámara ofrece `best.pt`. El video ajusta también dimensiones impares y rechaza resultados vacíos o ilegibles. El cliente HTTP termina con código 1 si falla la entrada, la petición o el guardado; devuelve 0 solo cuando guarda la imagen anotada.

Las pruebas de regresión del despliegue se ejecutan desde esta carpeta, con el entorno principal:

```bash
python -m unittest discover -s tests -v
```

Las cifras de validación del 10 de octubre son históricas. La auditoría del 15 de octubre reprodujo 19 notebooks completos, tres de forma parcial y cinco quedaron bloqueados por credenciales. Cats/Dogs alcanzó el límite de tiempo durante el fine-tuning; los resultados de llamadas remotas anteriores no sustituyen su repetición con claves propias. Estas correcciones no acreditan esas pruebas pendientes.
