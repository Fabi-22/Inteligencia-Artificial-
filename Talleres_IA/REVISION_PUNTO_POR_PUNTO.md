# Revisión punto por punto de los talleres

Revisión del 10 de octubre de 2026. Se cotejaron instrucciones, implementación, explicaciones, salidas y archivos auxiliares. Las filas identifican evidencia concreta; la presencia de código no se confunde con una prueba real.

Original del curso: commit `336a28e693b53f0a448ba967c5f37287c8c6c8ef`. Numeración de celdas desde 1, contando Markdown y código.

## Criterios y aclaraciones

- `training_own_data` original descarga SiteSafety del profesor y no contiene una instrucción adicional de recolectar datos. Se cumplió ese ejemplo. El dataset propio requerido se construyó en el taller de flores.
- Las propuestas expresamente opcionales o sugeridas no son requisitos obligatorios: variaciones de arquitectura de Fashion-MNIST, imagen externa de flores y mejoras B/D de documentos. Se implementaron las mejoras A/C; sus límites de formato están documentados.
- El notebook de flores analiza ocho imágenes erróneas distintas: cuatro de test antes del ajuste y cuatro de validación después. No se inventaron errores para llegar al mínimo de cinco.
- La ejecución de modelos de lenguaje no garantiza respuestas correctas. Se registran las confusiones, alucinaciones y errores de código observados.

## Semana_04/01_value_iteration_gridworld.ipynb

[Notebook resuelto](Semana_04/01_value_iteration_gridworld.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture4/01_value_iteration_gridworld.ipynb)

Ejecución registrada: 5/5 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Definir estados, pared, terminales, R(s), acciones y transición | Celdas 4 | Revisado y cumplido |
| 2 | Aplicar Bellman de optimalidad hasta convergencia | Celdas 7 | Revisado y cumplido |
| 3 | Mostrar valores y extraer política óptima | Celdas 10 | Revisado y cumplido |

## Semana_04/02_policy_iteration_gridworld.ipynb

[Notebook resuelto](Semana_04/02_policy_iteration_gridworld.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture4/02_policy_iteration_gridworld.ipynb)

Ejecución registrada: 6/6 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Evaluar una política fija sin maximizar durante evaluación | Celdas 6 | Revisado y cumplido |
| 2 | Mejorar con argmax y repetir hasta estabilidad | Celdas 10 | Revisado y cumplido |
| 3 | Mostrar historia, valores y política | Celdas 11 | Revisado y cumplido |

## Semana_04/03_lab_warehouse_mdp_estudiantes.ipynb

[Notebook resuelto](Semana_04/03_lab_warehouse_mdp_estudiantes.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture4/03_lab_warehouse_mdp_estudiantes.ipynb)

Ejecución registrada: 8/8 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Parte 1: modelar los estados de la imagen 5×6, pisos, recompensas y terminales | Celdas 5 | Revisado y cumplido |
| 2 | Validar que cada distribución de transición sume 1 | Celdas 7 | Revisado y cumplido |
| 3 | Parte 2: valor esperado, Value Iteration y extracción de política | Celdas 9 | Revisado y cumplido |
| 4 | Parte 3: Policy Evaluation, Improvement e Iteration | Celdas 11 | Revisado y cumplido |
| 5 | Parte 4: visualización de valores, flechas y acuerdo de ambos algoritmos | Celdas 14 | Revisado y cumplido |
| 6 | Parte 5.1: destino desde START | Celdas 16 | Revisado y cumplido |
| 7 | Parte 5.2: por qué una recompensa menor puede ser óptima | Celdas 16 | Revisado y cumplido |
| 8 | Parte 5.3: estados afectados por piso resbaloso | Celdas 16 | Revisado y cumplido |
| 9 | Parte 5.4: costo por paso | Celdas 16 | Revisado y cumplido |
| 10 | Parte 5.5: transición dependiente del estado | Celdas 16 | Revisado y cumplido |
| 11 | Experimento A: predicción previa y living_reward=-0.1 | Celdas 18 | Revisado y cumplido |
| 12 | Experimento B: éxito 0.4, desviaciones 0.3 y comparación | Celdas 18 | Revisado y cumplido |
| 13 | Experimento C: gamma=0.99 y ruta completa | Celdas 18 | Revisado y cumplido |
| 14 | Bonus: umbral aproximado del costo por paso | Celdas 18 | Revisado y cumplido |

## Semana_06/challenge/01_data_challenge.ipynb

[Notebook resuelto](Semana_06/challenge/01_data_challenge.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/challenge/01_data_challenge.ipynb)

Ejecución registrada: 9/9 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | TODO 1: leer wine.csv desde data/raw y validar target | Celdas 6 | Revisado y cumplido |
| 2 | TODO 2: forma, tipos, nulos, duplicados y distribución de target | Celdas 7 | Revisado y cumplido |
| 3 | Conclusión de calidad y decisiones | Celdas 8 | Revisado y cumplido |
| 4 | TODO 3: split 80/20, estratificación y semilla 42 | Celdas 10 | Revisado y cumplido |
| 5 | Verificar particiones disjuntas y cobertura | Celdas 11 | Revisado y cumplido |
| 6 | TODO 4: tres visualizaciones exclusivamente de train | Celdas 13 | Revisado y cumplido |
| 7 | Tres hallazgos para modelado | Celdas 14 | Revisado y cumplido |
| 8 | TODO 5: train.csv y test.csv sin índice, contrato con features/target/semilla/test_size | Celdas 16 | Revisado y cumplido |
| 9 | Comprobar los tres artefactos requeridos | Celdas 17 | Revisado y cumplido |

## Semana_06/challenge/02_training_challenge.ipynb

[Notebook resuelto](Semana_06/challenge/02_training_challenge.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/challenge/02_training_challenge.ipynb)

Ejecución registrada: 9/9 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar únicamente train y contrato; no cargar test | Celdas 6 | Revisado y cumplido |
| 2 | TODO 1: imputación por mediana y escalado dentro de pipelines | Celdas 8 | Revisado y cumplido |
| 3 | Explicar fuga de información al escalar antes de CV | Celdas 9 | Revisado y cumplido |
| 4 | TODO 2: DecisionTree, LogisticRegression y KNN | Celdas 11 | Revisado y cumplido |
| 5 | TODO 3: CV estratificada de 5 folds, medias train/val y desviación | Celdas 13 | Revisado y cumplido |
| 6 | TODO 4: GridSearchCV accuracy y espacios para tres modelos | Celdas 15 | Revisado y cumplido |
| 7 | TODO 5: campeón por mayor score CV y persistencia de tres artefactos | Celdas 17 | Revisado y cumplido |
| 8 | Justificación: rendimiento, variabilidad, sobreajuste, complejidad e interpretabilidad | Celdas 19 | Revisado y cumplido |

## Semana_06/challenge/03_evaluation_deployment_challenge.ipynb

[Notebook resuelto](Semana_06/challenge/03_evaluation_deployment_challenge.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/challenge/03_evaluation_deployment_challenge.ipynb)

Ejecución registrada: 8/8 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar campeón, contrato y test después de selección | Celdas 5 | Revisado y cumplido |
| 2 | TODO 1: accuracy, F1 macro, classification_report y matriz | Celdas 7 | Revisado y cumplido |
| 3 | Comparar con CV, identificar clases confundidas y discutir sobreajuste | Celdas 17 | Revisado y cumplido |
| 4 | TODO 2: validar columnas, reordenar y devolver clase y probabilidades | Celdas 10 | Revisado y cumplido |
| 5 | TODO 3: lote de cinco observaciones y batch_predictions.csv | Celdas 12 | Revisado y cumplido |
| 6 | TODO 4: test_metrics.json con modelo, accuracy y F1 macro | Celdas 14 | Revisado y cumplido |
| 7 | Resumen ejecutivo con seis elementos | Celdas 14 | Revisado y cumplido |

## Semana_06/classification/01_data_profiling_and_splitting.ipynb

[Notebook resuelto](Semana_06/classification/01_data_profiling_and_splitting.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/classification/01_data_profiling_and_splitting.ipynb)

Ejecución registrada: 10/10 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar datos originales y revisar estructura/calidad | Celdas 10 | Revisado y cumplido |
| 2 | Crear split estratificado reproducible sin transformaciones | Celdas 12 | Revisado y cumplido |
| 3 | Guardar train, test y contrato | Celdas 13 | Revisado y cumplido |

## Semana_06/classification/02_eda.ipynb

[Notebook resuelto](Semana_06/classification/02_eda.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/classification/02_eda.ipynb)

Ejecución registrada: 10/10 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar únicamente entrenamiento | Celdas 6 | Revisado y cumplido |
| 2 | Distribución de clase y escalas de variables | Celdas 8 | Revisado y cumplido |
| 3 | Relación con clase y correlaciones | Celdas 13 | Revisado y cumplido |
| 4 | Decisiones de modelado justificadas por EDA | Celdas 15 | Revisado y cumplido |

## Semana_06/classification/03_data_processing_and_feature_engineering.ipynb

[Notebook resuelto](Semana_06/classification/03_data_processing_and_feature_engineering.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/classification/03_data_processing_and_feature_engineering.ipynb)

Ejecución registrada: 6/6 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Validar contrato de variables | Celdas 6 | Revisado y cumplido |
| 2 | Definir imputación para árbol e imputación/escalado para otros modelos | Celdas 8 | Revisado y cumplido |
| 3 | Guardar preprocesadores sin ajustarlos fuera de CV | Celdas 8 | Revisado y cumplido |

## Semana_06/classification/04_training.ipynb

[Notebook resuelto](Semana_06/classification/04_training.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/classification/04_training.ipynb)

Ejecución registrada: 10/10 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Entropía binaria y gráfica | Celdas 8 | Revisado y cumplido |
| 2 | Tres candidatos y espacios de hiperparámetros | Celdas 10 | Revisado y cumplido |
| 3 | CV estratificada y optimización por ROC AUC | Celdas 11 | Revisado y cumplido |
| 4 | Guardar campeón, comparación y metadatos | Celdas 12 | Revisado y cumplido |
| 5 | Inspección opcional del árbol correcto, aunque no sea campeón | Celdas 14 | Revisado y cumplido |

## Semana_06/classification/05_evaluation.ipynb

[Notebook resuelto](Semana_06/classification/05_evaluation.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/classification/05_evaluation.ipynb)

Ejecución registrada: 9/9 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Evaluar solo el campeón sobre test | Celdas 6 | Revisado y cumplido |
| 2 | Accuracy, precision, recall, F1, ROC AUC y reporte por clase | Celdas 7, 11 | Revisado y cumplido |
| 3 | Matriz de confusión y curva ROC | Celdas 8 | Revisado y cumplido |
| 4 | Curva de aprendizaje usando únicamente train | Celdas 10 | Revisado y cumplido |
| 5 | Persistir métricas finales | Celdas 11 | Revisado y cumplido |

## Semana_06/classification/06_inference_and_deployment.ipynb

[Notebook resuelto](Semana_06/classification/06_inference_and_deployment.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture6/classification/06_inference_and_deployment.ipynb)

Ejecución registrada: 8/8 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar modelo y contrato originales | Celdas 6 | Revisado y cumplido |
| 2 | Validar faltantes/extras y orden de columnas | Celdas 8 | Revisado y cumplido |
| 3 | Inferencia con nombres de clase y probabilidades | Celdas 8 | Revisado y cumplido |
| 4 | Simular lote y guardar predicciones | Celdas 11 | Revisado y cumplido |

## Semana_07/YourFirstDeepNN_FashionMNIST_Keras3.ipynb

[Notebook resuelto](Semana_07/YourFirstDeepNN_FashionMNIST_Keras3.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture7/YourFirstDeepNN_FashionMNIST_Keras3.ipynb)

Ejecución registrada: 14/14 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Carga completa y normalización Fashion-MNIST | Celdas 5, 6, 24 | Revisado y cumplido |
| 2 | Modelo lineal y FC con 128 unidades ReLU | Celdas 9, 10, 24 | Revisado y cumplido |
| 3 | Adam, pérdida con logits, 10 épocas y batch 64 | Celdas 12, 13 | Revisado y cumplido |
| 4 | Entrenamientos de ambos modelos y comparación real | Celdas 10, 11, 14, 15, 25 | Revisado y cumplido |
| 5 | Curvas y evaluación sobre test | Celdas 21, 22, 24, 25 | Revisado y cumplido |
| 6 | Predicciones y softmax | Celdas 20, 24 | Revisado y cumplido |

## Semana_07/Challenge_Keras3_CIFAR10_Grayscale.ipynb

[Notebook resuelto](Semana_07/Challenge_Keras3_CIFAR10_Grayscale.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture7/Challenge_Keras3_CIFAR10_Grayscale.ipynb)

Ejecución registrada: 18/18 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Carga, split y preprocesamiento según el enunciado | Celdas 5, 7, 10, 11, 13, 22 | Revisado y cumplido |
| 2 | TODO arquitectura: Input, Flatten, Dense ReLU y logits | Celdas 15 | Revisado y cumplido |
| 3 | Validación del número exacto de parámetros | Celdas 16 | Revisado y cumplido |
| 4 | TODO compile: Adam, SparseCategoricalCrossentropy from_logits=True y accuracy | Celdas 19 | Revisado y cumplido |
| 5 | TODO fit con épocas, batch y validación indicados | Celdas 22 | Revisado y cumplido |
| 6 | Curvas de aprendizaje y respuesta empírica a overfitting | Celdas 25, 38 | Revisado y cumplido |
| 7 | TODO evaluate y accuracy real | Celdas 28 | Revisado y cumplido |
| 8 | TODO softmax y argmax; probabilidades normalizadas | Celdas 32 | Revisado y cumplido |
| 9 | Visualizar 12 predicciones | Celdas 36 | Revisado y cumplido |
| 10 | Reflexión final con resultados, limitaciones y estructura espacial | Celdas 37 | Revisado y cumplido |
| 11 | Pregunta conceptual 1: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 8, 37 | Revisado y cumplido |
| 12 | Pregunta conceptual 2: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 17 | Revisado y cumplido |
| 13 | Pregunta conceptual 3: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 17 | Revisado y cumplido |
| 14 | Pregunta conceptual 4: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 17 | Revisado y cumplido |
| 15 | Pregunta conceptual 5: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 20 | Revisado y cumplido |
| 16 | Pregunta conceptual 6: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 23 | Revisado y cumplido |
| 17 | Pregunta conceptual 7: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 23 | Revisado y cumplido |
| 18 | Pregunta conceptual 8: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 26 | Revisado y cumplido |
| 19 | Pregunta conceptual 9: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 29 | Revisado y cumplido |
| 20 | Pregunta conceptual 10: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 34 | Revisado y cumplido |

## Semana_07/Challenge_Keras3_OlivettiFaces.ipynb

[Notebook resuelto](Semana_07/Challenge_Keras3_OlivettiFaces.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture7/Challenge_Keras3_OlivettiFaces.ipynb)

Ejecución registrada: 16/16 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Carga, split y preprocesamiento según el enunciado | Celdas 7, 10, 19, 38 | Revisado y cumplido |
| 2 | TODO arquitectura: Input, Flatten, Dense ReLU y logits | Celdas 12, 38 | Revisado y cumplido |
| 3 | Validación del número exacto de parámetros | Celdas 13 | Revisado y cumplido |
| 4 | TODO compile: Adam, SparseCategoricalCrossentropy from_logits=True y accuracy | Celdas 15, 16, 38 | Revisado y cumplido |
| 5 | TODO fit con épocas, batch y validación indicados | Celdas 19 | Revisado y cumplido |
| 6 | Curvas de aprendizaje y respuesta empírica a overfitting | Celdas 22, 36, 38 | Revisado y cumplido |
| 7 | TODO evaluate y accuracy real | Celdas 25 | Revisado y cumplido |
| 8 | TODO softmax y argmax; probabilidades normalizadas | Celdas 29 | Revisado y cumplido |
| 9 | Visualizar 12 predicciones | Celdas 33 | Revisado y cumplido |
| 10 | Reflexión final con resultados, limitaciones y estructura espacial | Celdas 34 | Revisado y cumplido |
| 11 | Pregunta conceptual 1: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 8 | Revisado y cumplido |
| 12 | Pregunta conceptual 2: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 14 | Revisado y cumplido |
| 13 | Pregunta conceptual 3: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 14 | Revisado y cumplido |
| 14 | Pregunta conceptual 4: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 14 | Revisado y cumplido |
| 15 | Pregunta conceptual 5: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 17 | Revisado y cumplido |
| 16 | Pregunta conceptual 6: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 20 | Revisado y cumplido |
| 17 | Pregunta conceptual 7: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 20 | Revisado y cumplido |
| 18 | Pregunta conceptual 8: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 23 | Revisado y cumplido |
| 19 | Pregunta conceptual 9: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 26 | Revisado y cumplido |
| 20 | Pregunta conceptual 10: respuesta explícita cotejada con ejecución cuando corresponde | Celdas 31 | Revisado y cumplido |

## Semana_08/transfer_learning/CNN_Transfer_Keras3.ipynb

[Notebook resuelto](Semana_08/transfer_learning/CNN_Transfer_Keras3.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture8/transfer_learning/CNN_Transfer_Keras3.ipynb)

Ejecución registrada: 23/23 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Descargar Cats vs Dogs y eliminar archivos no decodificables | Celdas 8 | Revisado y cumplido |
| 2 | Split 80/20 e imágenes 224×224 | Celdas 11 | Revisado y cumplido |
| 3 | Inferencia ImageNet VGG16 y decode top3 | Celdas 16 | Revisado y cumplido |
| 4 | Extractor VGG16 y visualización de mapas 7×7×512 | Celdas 23 | Revisado y cumplido |
| 5 | 800 representaciones y split 700/100; cabeza durante 5 épocas | Celdas 25 | Revisado y cumplido |
| 6 | Modelo completo con backbone congelado y una época | Celdas 32 | Revisado y cumplido |
| 7 | Guardar modelo .keras, pesos .h5 y recargar | Celdas 36 | Revisado y cumplido |
| 8 | Descongelar únicamente block5, recompilar AdamW 1e-5 y entrenar una época | Celdas 41 | Revisado y cumplido |
| 9 | Inspeccionar ResNet50 y explicar BatchNorm | Celdas 44 | Revisado y cumplido |

## Semana_08/transfer_learning/taller_transfer_learning_datos_propios_keras3.ipynb

[Notebook resuelto](Semana_08/transfer_learning/taller_transfer_learning_datos_propios_keras3.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture8/transfer_learning/taller_transfer_learning_datos_propios_keras3.ipynb)

Ejecución registrada: 24/24 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | TODO 1.1: problema visual de tres clases | Celdas 8 | Revisado y cumplido |
| 2 | TODO 1.2: dos o tres consultas por clase | Celdas 7 | Revisado y cumplido |
| 3 | TODO 1.3: hipótesis sobre características visuales | Celdas 8 | Revisado y cumplido |
| 4 | TODO 1.4: sesgos y fuga de información | Celdas 8 | Revisado y cumplido |
| 5 | TODO 2.1: descargar aproximadamente 100–150 imágenes útiles por clase | Celdas 55 | Revisado y cumplido |
| 6 | TODO 2.2: muestras aleatorias y revisión semántica | Celdas 19 | Revisado y cumplido |
| 7 | TODO 2.3: refinar consultas cuando los resultados son pobres | Celdas 8 | Revisado y cumplido |
| 8 | TODO 2.4: eliminar imágenes incorrectas y documentar problemas | Celdas 55 | Revisado y cumplido |
| 9 | TODO 2.5: conteos finales y problema más frecuente | Celdas 55 | Revisado y cumplido |
| 10 | Verificación técnica: cero imágenes no decodificables | Celdas 17 | Revisado y cumplido |
| 11 | Split 70/15/15 y explicación de uso de test | Celdas 55 | Revisado y cumplido |
| 12 | Keras datasets a 224×224, train mezclado y val/test estables | Celdas 25 | Revisado y cumplido |
| 13 | EfficientNetB0 ImageNet, augmentation, base congelada y cabeza | Celdas 5, 24, 26, 27, 32, 55 | Revisado y cumplido |
| 14 | TODO 3: predicción previa de curvas | Celdas 8, 28, 55 | Revisado y cumplido |
| 15 | TODO 3: Adam 1e-3, accuracy, EarlyStopping val_loss y hasta 10 épocas | Celdas 28, 29, 40 | Revisado y cumplido |
| 16 | Cuatro curvas: accuracy/val_accuracy/loss/val_loss | Celdas 31, 53 | Revisado y cumplido |
| 17 | Evaluación inicial, reporte por clase y matriz de confusión | Celdas 55 | Revisado y cumplido |
| 18 | TODO 4.1: mejor clase | Celdas 55 | Revisado y cumplido |
| 19 | TODO 4.2: principal confusión | Celdas 55 | Revisado y cumplido |
| 20 | TODO 4.3: problema por clase oculto por accuracy | Celdas 55 | Revisado y cumplido |
| 21 | TODO 4.4: primera mejora en dataset | Celdas 36 | Revisado y cumplido |
| 22 | TODO 5: decisión de capas por validación y BatchNorm congelada | Celdas 38 | Revisado y cumplido |
| 23 | TODO 5: recompilar Adam 1e-5, 3–8 épocas y EarlyStopping | Celdas 40 | Revisado y cumplido |
| 24 | Comparar antes/después, matriz final y métricas por clase | Celdas 55 | Revisado y cumplido |
| 25 | TODO 6: al menos cinco errores distintos, causas y mejoras | Celdas 55 | Revisado y cumplido |
| 26 | Conclusión 1: aprendizaje al construir dataset | Celdas 46 | Revisado y cumplido |
| 27 | Conclusión 2: principal problema de calidad | Celdas 55 | Revisado y cumplido |
| 28 | Conclusión 3: cambio de desempeño | Celdas 55 | Revisado y cumplido |
| 29 | Conclusión 4: utilidad y límites del fine-tuning | Celdas 55 | Revisado y cumplido |
| 30 | Conclusión 5: qué mejorar primero | Celdas 55 | Revisado y cumplido |

## Semana_08/yolo/Lecture_08_Yolo_Intro.ipynb

[Notebook resuelto](Semana_08/yolo/Lecture_08_Yolo_Intro.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture8/yolo/Lecture_08_Yolo_Intro.ipynb)

Ejecución registrada: 9/9 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar modelo y realizar inferencia base | Celdas 5, 6 | Revisado y cumplido |
| 2 | Inspeccionar clases, confianza y bounding boxes | Celdas 12, 13, 15, 17, 19 | Revisado y cumplido |
| 3 | Visualizar BGR convertido a RGB | Celdas 14, 15, 17, 19 | Revisado y cumplido |
| 4 | Comparar umbrales 0.25, 0.50 y 0.75 | Celdas 17 | Revisado y cumplido |
| 5 | Ejercicio: imagen adicional propia o de internet, inferencia y detecciones | Celdas 19 | Revisado y cumplido |

## Semana_08/yolo/Lecture_08_Yolo_training.ipynb

[Notebook resuelto](Semana_08/yolo/Lecture_08_Yolo_training.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture8/yolo/Lecture_08_Yolo_training.ipynb)

Ejecución registrada: 8/8 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar credencial local sin publicarla | Celdas 3 | Revisado y cumplido |
| 2 | Descargar proyecto y versión indicados por el profesor | Celdas 4 | Revisado y cumplido |
| 3 | YOLO26n preentrenado, 20 épocas | Celdas 5 | Revisado y cumplido |
| 4 | Inferir sobre imagen de test | Celdas 6, 9 | Revisado y cumplido |
| 5 | Inspeccionar cajas, clases y confianza | Celdas 7 | Revisado y cumplido |
| 6 | Mostrar imagen anotada con colores correctos | Celdas 8 | Revisado y cumplido |
| 7 | Guardar evaluación y pesos como evidencia adicional | Celdas 9 | Revisado y cumplido |

## Semana_08/yolo/Lecture_08_Yolo_training_own_data.ipynb

[Notebook resuelto](Semana_08/yolo/Lecture_08_Yolo_training_own_data.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture8/yolo/Lecture_08_Yolo_training_own_data.ipynb)

Ejecución registrada: 8/8 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar credencial local sin publicarla | Celdas 3 | Revisado y cumplido |
| 2 | Descargar proyecto y versión indicados por el profesor | Celdas 4 | Revisado y cumplido |
| 3 | YOLO26n preentrenado, 20 épocas | Celdas 5 | Revisado y cumplido |
| 4 | Inferir sobre imagen de test | Celdas 6, 9 | Revisado y cumplido |
| 5 | Inspeccionar cajas, clases y confianza | Celdas 7 | Revisado y cumplido |
| 6 | Mostrar imagen anotada con colores correctos | Celdas 8 | Revisado y cumplido |
| 7 | Guardar evaluación y pesos como evidencia adicional | Celdas 9 | Revisado y cumplido |

## Semana_08/yolo/deployment/test.ipynb

[Notebook resuelto](Semana_08/yolo/deployment/test.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/lecture8/yolo/deployment/test.ipynb)

Ejecución registrada: 17/17 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Credencial y dataset Logistics versión 2 | Celdas 5, 7 | Revisado y cumplido |
| 2 | Cargar best.pt suministrado | Celdas 8 | Revisado y cumplido |
| 3 | Evaluación de validación completa | Celdas 9 | Revisado y cumplido |
| 4 | Predicción, inspección de cajas y visualización | Celdas 10 | Revisado y cumplido |
| 5 | Evaluación de test completa | Celdas 15 | Revisado y cumplido |
| 6 | Serializar detecciones con clase, confianza y bbox | Celdas 16 | Revisado y cumplido |
| 7 | Prueba adicional del cliente y servidor locales | Celdas 20 | Revisado y cumplido |

## Semana_09/tokenization_Introduction.ipynb

[Notebook resuelto](Semana_09/tokenization_Introduction.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/Lecture9/tokenization_Introduction.ipynb)

Ejecución registrada: 8/8 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Cargar Word2Vec Google News completo y vectores de 300 dimensiones | Celdas 5 | Revisado y cumplido |
| 2 | Explorar king, queen, analogía y similitudes | Celdas 9, 11 | Revisado y cumplido |
| 3 | PCA del ejemplo y discusión de sesgos | Celdas 6, 8, 9, 16, 17, 18, 19 | Revisado y cumplido |
| 4 | Reto 1: animal, vector, diez vecinos y explicación de sorpresas | Celdas 19 | Revisado y cumplido |
| 5 | Reto 2: dog-domestic+wild y eagle-fly+swim | Celdas 17 | Revisado y cumplido |
| 6 | Reto 2: analogía inventada, hipótesis y resultado | Celdas 17, 18, 19 | Revisado y cumplido |
| 7 | Reto 3: PCA 3D de animal, vecinos y operación; interpretación | Celdas 19 | Revisado y cumplido |
| 8 | Verificar vocabulario para prevenir KeyError | Celdas 16, 17 | Revisado y cumplido |

## Semana_09/01_local_chatbot_lab.ipynb

[Notebook resuelto](Semana_09/01_local_chatbot_lab.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/Lecture9/01_local_chatbot_lab.ipynb)

Ejecución registrada: 14/14 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Instalar/iniciar Ollama local y descargar tinyllama:1.1b | Celdas 3, 5, 7 | Revisado y cumplido |
| 2 | Primera llamada, explicación de red neuronal y generación de código | Celdas 11, 13, 14, 19, 21, 24 | Revisado y cumplido |
| 3 | Demostrar interacciones sin memoria | Celdas 21, 26 | Revisado y cumplido |
| 4 | Implementar historial System/Human/AI y repetir pregunta | Celdas 24 | Revisado y cumplido |
| 5 | Explicar contexto y estrategias para conversaciones largas | Celdas 28 | Revisado y cumplido |

## Semana_09/02_local_remote_hf_chatbot_lab.ipynb

[Notebook resuelto](Semana_09/02_local_remote_hf_chatbot_lab.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/Lecture9/02_local_remote_hf_chatbot_lab.ipynb)

Ejecución registrada: 16/26 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | LOCAL: cargar Qwen2.5-1.5B-Instruct y tokenizer | Celdas 7 | Revisado y cumplido |
| 2 | LOCAL: aplicar plantilla, tokenizar, generar y decodificar | Celdas 9, 12 | Revisado y cumplido |
| 3 | LOCAL: función reutilizable y ejemplo de código | Celdas 12 | Revisado y cumplido |
| 4 | LOCAL: historial y prueba del color | Celdas 15 | Revisado y cumplido |
| 5 | LOCAL: pipeline y chatbot con memoria | Celdas 23 | Revisado y cumplido |
| 6 | REMOTO: token con permiso de inferencia y cliente | Celdas 29 | Implementado; servicio bloqueado por HTTP 402 (sin créditos) |
| 7 | REMOTO: primera inferencia real | Celdas 31, 33 | Implementado; servicio bloqueado por HTTP 402 (sin créditos) |
| 8 | REMOTO: función reutilizable | Celdas 33 | Implementado; servicio bloqueado por HTTP 402 (sin créditos) |
| 9 | REMOTO: historial y prueba del color | Celdas 36 | Implementado; servicio bloqueado por HTTP 402 (sin créditos) |
| 10 | REMOTO: streaming real | Celdas 40 | Implementado; servicio bloqueado por HTTP 402 (sin créditos) |
| 11 | Comparativa de modos local, remoto y API | Celdas 2, 42 | Revisado y cumplido |

## Semana_09/03_nvidia_chatbot_lab.ipynb

[Notebook resuelto](Semana_09/03_nvidia_chatbot_lab.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/Lecture9/03_nvidia_chatbot_lab.ipynb)

Ejecución registrada: 22/22 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Configurar cliente NVIDIA con clave local y modelo indicado | Celdas 9 | Revisado y cumplido |
| 2 | Primera llamada y metadatos de uso | Celdas 11, 13, 15, 17, 19, 21, 29, 30, 36, 38 | Revisado y cumplido |
| 3 | Chat sin memoria y con historial | Celdas 15, 20, 21, 26, 31, 38 | Revisado y cumplido |
| 4 | Streaming y streaming con memoria | Celdas 29, 32 | Revisado y cumplido |
| 5 | Roles y gestión de conversaciones largas | Celdas 10, 11, 13, 15, 21, 27, 29, 32, 35, 36, 38 | Revisado y cumplido |

## Semana_09/04_nvidia_gradio_lab.ipynb

[Notebook resuelto](Semana_09/04_nvidia_gradio_lab.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/Lecture9/04_nvidia_gradio_lab.ipynb)

Ejecución registrada: 31/31 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Configurar NVIDIA y dependencias localmente | Celdas 5, 6 | Revisado y cumplido |
| 2 | Interfaz simple de Gradio | Celdas 9, 11, 16, 22, 32 | Revisado y cumplido |
| 3 | Chat básico y streaming | Celdas 20, 21, 22, 26, 36 | Revisado y cumplido |
| 4 | ChatInterface con historial | Celdas 25, 27, 37 | Revisado y cumplido |
| 5 | Generador de menú con múltiples entradas | Celdas 1, 2, 3, 6, 11, 22, 25, 26, 27, 30, 31, 32, 33, 34, 40, 41 | Revisado y cumplido |
| 6 | System prompt personalizable | Celdas 36 | Revisado y cumplido |
| 7 | Pruebas reales de funciones e interfaces construidas | Celdas 41 | Revisado y cumplido |

## Semana_09/05_ejercicio_nvidia_documentos.ipynb

[Notebook resuelto](Semana_09/05_ejercicio_nvidia_documentos.ipynb) · [Original exacto](https://github.com/EAFIT-IA/si3003-artificial-intelligence/blob/336a28e693b53f0a448ba967c5f37287c8c6c8ef/notebooks/Lecture9/05_ejercicio_nvidia_documentos.ipynb)

Ejecución registrada: 7/7 celdas de código; 0 salidas de error.

| Punto | Requisito | Evidencia en notebook | Estado |
|---|---|---|---|
| 1 | Paso 0: PDF local y cliente con credencial protegida | Celdas 3, 6, 12 | Revisado y cumplido |
| 2 | Paso 1: extraer páginas, contemplar None y mostrar primeros 500 caracteres | Celdas 5, 6 | Revisado y cumplido |
| 3 | Paso 2: endpoint NVIDIA y Nemotron 3 Super | Celdas 7, 8 | Revisado y cumplido |
| 4 | Paso 3.1: system prompt delimitado, exclusivo del documento y abstención | Celdas 9, 10 | Revisado y cumplido |
| 5 | Paso 3.2: historial Gradio a roles user/assistant | Celdas 9, 10, 18 | Revisado y cumplido |
| 6 | Paso 3.3: streaming acumulativo y yield | Celdas 10, 18 | Revisado y cumplido |
| 7 | Paso 4: número de páginas/caracteres, ChatInterface, documento oculto y ejemplos | Celdas 11, 12 | Revisado y cumplido |
| 8 | Paso 4: interfaz iniciada y probada localmente | Celdas 20 | Revisado y cumplido |
| 9 | Paso 5.1: arquitectura principal | Celdas 19 | Revisado y cumplido |
| 10 | Paso 5.2: atención | Celdas 19 | Revisado y cumplido |
| 11 | Paso 5.3: seis capas | Celdas 19, 20 | Revisado y cumplido |
| 12 | Paso 5.4: autores | Celdas 19 | Revisado y cumplido |
| 13 | Paso 5.5: WMT 2014 y distinción base/big | Celdas 19 | Revisado y cumplido |
| 14 | Paso 5.6: pregunta trampa GPT-4 y observación | Celdas 19 | Revisado y cumplido |
| 15 | Reflexión 1: enviar documento completo | Celdas 16 | Revisado y cumplido |
| 16 | Reflexión 2: por qué no es RAG | Celdas 16 | Revisado y cumplido |
| 17 | Reflexión 3: comprobar fundamento documental | Celdas 16 | Revisado y cumplido |
| 18 | Reflexión 4: riesgos del prompt | Celdas 16 | Revisado y cumplido |
| 19 | Mejoras opcionales A y C: contexto y citas, con límites medidos | Celdas 16 | Revisado y cumplido |

## Correcciones de esta revisión

- Ollama instalado y ejecutado realmente; se adaptó el arranque local y se analizó críticamente el código generado.
- Hugging Face local ejecutado realmente; se unificó HF_TOKEN/HF_ACCESS_TOKEN y se corrigió el argumento del proveedor remoto.
- Se sustituyeron respuestas vagas de Olivetti por resultados concretos, diferenciando fallo de aprendizaje y sobreajuste.
- Checklist de la fase inicial de flores marcado a partir de evidencia ya existente.
- Diagramas ausentes reconstruidos y guardados localmente, identificados como reconstrucciones.
- Gatos/perros se ejecutó con el dataset completo y TensorFlow/Metal en un entorno separado, sin alterar la muestra para acelerar.

Total: **27 notebooks y 234 puntos documentados**. El estado pendiente de un proveedor externo no debe confundirse con una respuesta simulada ni con una ejecución completa.
