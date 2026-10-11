# Estado real de validación

Revisión del 10 de octubre de 2026. **27 notebooks incluidos: 26 ejecutados de principio a fin y 1 con la parte local ejecutada y la parte remota bloqueada por falta de créditos en Hugging Face (HTTP 402).** No se presentan resultados simulados como resultados reales de NVIDIA.

Los 27 notebooks tienen estructura válida y código revisado sintácticamente. No quedan espacios de código de actividad sin completar ni salidas de error guardadas. Las gráficas de las ejecuciones están incrustadas. La parte remota de Hugging Face no se considera ejecutada satisfactoriamente.

| Notebook | Celdas ejecutadas / código | Gráficas incrustadas | Alcance |
|---|---:|---:|---|
| [Semana_04/01_value_iteration_gridworld.ipynb](Semana_04/01_value_iteration_gridworld.ipynb) | 5/5 | 0 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_04/02_policy_iteration_gridworld.ipynb](Semana_04/02_policy_iteration_gridworld.ipynb) | 6/6 | 0 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_04/03_lab_warehouse_mdp_estudiantes.ipynb](Semana_04/03_lab_warehouse_mdp_estudiantes.ipynb) | 8/8 | 0 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/challenge/01_data_challenge.ipynb](Semana_06/challenge/01_data_challenge.ipynb) | 9/9 | 3 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/challenge/02_training_challenge.ipynb](Semana_06/challenge/02_training_challenge.ipynb) | 9/9 | 0 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/challenge/03_evaluation_deployment_challenge.ipynb](Semana_06/challenge/03_evaluation_deployment_challenge.ipynb) | 8/8 | 1 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/classification/01_data_profiling_and_splitting.ipynb](Semana_06/classification/01_data_profiling_and_splitting.ipynb) | 10/10 | 0 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/classification/02_eda.ipynb](Semana_06/classification/02_eda.ipynb) | 10/10 | 4 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/classification/03_data_processing_and_feature_engineering.ipynb](Semana_06/classification/03_data_processing_and_feature_engineering.ipynb) | 6/6 | 0 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/classification/04_training.ipynb](Semana_06/classification/04_training.ipynb) | 10/10 | 2 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/classification/05_evaluation.ipynb](Semana_06/classification/05_evaluation.ipynb) | 9/9 | 2 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_06/classification/06_inference_and_deployment.ipynb](Semana_06/classification/06_inference_and_deployment.ipynb) | 8/8 | 0 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_07/Challenge_Keras3_CIFAR10_Grayscale.ipynb](Semana_07/Challenge_Keras3_CIFAR10_Grayscale.ipynb) | 18/18 | 4 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_07/Challenge_Keras3_OlivettiFaces.ipynb](Semana_07/Challenge_Keras3_OlivettiFaces.ipynb) | 16/16 | 5 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_07/YourFirstDeepNN_FashionMNIST_Keras3.ipynb](Semana_07/YourFirstDeepNN_FashionMNIST_Keras3.ipynb) | 14/14 | 4 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_08/transfer_learning/CNN_Transfer_Keras3.ipynb](Semana_08/transfer_learning/CNN_Transfer_Keras3.ipynb) | 23/23 | 2 | Ejecutado completo con Cats/Dogs: extracción, entrenamiento, guardado, recarga y fine-tuning; TensorFlow/Metal. |
| [Semana_08/transfer_learning/taller_transfer_learning_datos_propios_keras3.ipynb](Semana_08/transfer_learning/taller_transfer_learning_datos_propios_keras3.ipynb) | 24/24 | 6 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_08/yolo/Lecture_08_Yolo_Intro.ipynb](Semana_08/yolo/Lecture_08_Yolo_Intro.ipynb) | 9/9 | 4 | Ejecutado completo; salidas guardadas, sin errores. |
| [Semana_08/yolo/Lecture_08_Yolo_training.ipynb](Semana_08/yolo/Lecture_08_Yolo_training.ipynb) | 8/8 | 3 | Entrenamiento real de 20 épocas con Roboflow; evaluación de test y pesos guardados. |
| [Semana_08/yolo/Lecture_08_Yolo_training_own_data.ipynb](Semana_08/yolo/Lecture_08_Yolo_training_own_data.ipynb) | 8/8 | 3 | Entrenamiento real de 20 épocas con Roboflow; evaluación de test y pesos guardados. |
| [Semana_08/yolo/deployment/test.ipynb](Semana_08/yolo/deployment/test.ipynb) | 17/17 | 1 | Modelo del profesor evaluado en validación y test completos de logística; métricas reales guardadas. |
| [Semana_09/01_local_chatbot_lab.ipynb](Semana_09/01_local_chatbot_lab.ipynb) | 14/14 | 0 | Ejecutado completo con Ollama y TinyLlama local; respuestas y errores del modelo analizados. |
| [Semana_09/02_local_remote_hf_chatbot_lab.ipynb](Semana_09/02_local_remote_hf_chatbot_lab.ipynb) | 16/26 | 0 | Parte local ejecutada; parte remota implementada y configurada, bloqueada por HTTP 402: cuenta sin créditos. |
| [Semana_09/03_nvidia_chatbot_lab.ipynb](Semana_09/03_nvidia_chatbot_lab.ipynb) | 22/22 | 0 | Ejecutado con NVIDIA real: chat, memoria y streaming; sin errores. |
| [Semana_09/04_nvidia_gradio_lab.ipynb](Semana_09/04_nvidia_gradio_lab.ipynb) | 31/31 | 0 | Ejecutado: interfaces locales y pruebas reales de chat, streaming, memoria, menú y prompt personalizado. |
| [Semana_09/05_ejercicio_nvidia_documentos.ipynb](Semana_09/05_ejercicio_nvidia_documentos.ipynb) | 7/7 | 0 | Ejecutado con NVIDIA real: seis preguntas, PDF y pruebas unitarias; interfaz comprobada en navegador. |
| [Semana_09/tokenization_Introduction.ipynb](Semana_09/tokenization_Introduction.ipynb) | 8/8 | 2 | Ejecutado completo; salidas guardadas, sin errores. |

## Comprobaciones adicionales

- Semana 4: mapa cotejado con la imagen; probabilidades normalizadas; límites y terminales; acuerdo entre algoritmos y residuo de Bellman; experimentos A/B/C y bonus.
- Semana 6: separación estratificada; CV con preprocesamiento dentro del pipeline; test reservado; archivos generados; esquema de inferencia, orden de columnas y suma de probabilidades.
- Semana 7: arquitecturas y normalización verificadas; entrenamiento real y respuestas basadas en métricas. Se documenta el fallo base de Olivetti y el experimento de centrado.
- Semana 8: imágenes revisadas antes del split, entrenamiento y fine-tuning reales; informes por clase; errores inspeccionados. Inferencia YOLO con imagen adicional, dos entrenamientos de 20 épocas y evaluación de logística completas. Servidor y cliente locales probados por HTTP.
- Semana 9: Word2Vec completo, vecinos y PCA reales. PDF extraído, seis respuestas reales de NVIDIA revisadas contra el paper y chatbot probado en navegador. Los ejemplos 03 y 04 también ejecutaron llamadas reales, memoria y streaming. Se documentan omisiones de citas e idioma.

Ollama y Hugging Face local también fueron probados realmente. El token remoto está configurado, pero el proveedor rechazó la inferencia por falta de créditos. Las limitaciones están también en el README y en los propios notebooks.
