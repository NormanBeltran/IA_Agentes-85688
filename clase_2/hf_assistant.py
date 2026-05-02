"""
Ejemplo de como conectarnos a Hugging Face desde Python

Requisitos:
pip install python-dotenv
pip install huggingface_hub

"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

# Leer configuración de las variables registradas en .env
API_KEY = os.getenv("API_KEY_HF")
MODEL = os.getenv("MODEL_HF")

# Validar que existan las variables

if not API_KEY:
    raise ValueError(f"La API_KEY para conectarnos no existe {API_KEY}")
if not MODEL:
    raise ValueError(f"El modelo para conectarnos no existe {MODEL}")

# Inicializar cliente de Groq
client = InferenceClient(token=API_KEY, model=MODEL)

#_________________________________ Funcion de conexión
def consultar_modelo(mensaje_usuario, system_prompt):
    """
    Envia un mensaje al modelo de Hugging Face y retorna la respuesta

    """
    messages = []
    if system_prompt:
        messages.append(
            {
                "role": "system",
                "content": system_prompt
            }
        )

    messages.append(
        {
        "role": "user",
        "content": mensaje_usuario
        }
    )

    try:
        chat_completion = client.chat_completion(
            messages=messages,
            temperature=0,
            max_tokens=1024
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error al conectarnos a {MODEL} {e}"

#_________________________________ Main

system = ""
pregunta = "Dame unicamente y solo la estructura JSON de palabra y definición de: Gravedad, IA, LLM"

print(f"El usuario pregunta: {pregunta}")
respuesta = consultar_modelo(pregunta, system)
print(f"El modelo responde {respuesta}")