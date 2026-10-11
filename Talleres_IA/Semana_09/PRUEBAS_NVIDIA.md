# Pruebas reales de NVIDIA

- Modelo: nvidia/nemotron-3-super-120b-a12b.
- Endpoint: https://integrate.api.nvidia.com/v1.
- Autenticación comprobada con respuesta real.
- Notebook 03: todas las celdas ejecutadas; chat sin memoria, con memoria y streaming.
- Notebook 04: interfaces creadas y abiertas localmente; funciones reales de chat, streaming, memoria, menú y personalización probadas. La prueba de memoria recordó “girasol”.
- Notebook 05: seis preguntas ejecutadas; cinco respuestas de contenido correctas y abstención ante GPT-4. Dos respuestas omitieron cita; una respondió en inglés. Ver nvidia_answers.json para las respuestas literales.
- Interfaz del notebook 05 probada en navegador: respondió “6 layers [Página 3]”.
- Clave solo en .env local, con permisos de archivo restrictivos. Excluida explícitamente del ZIP y del manifiesto de entrega.

Esta validación comprueba los casos descritos; no garantiza que cada respuesta futura sea correcta o respete el formato.
