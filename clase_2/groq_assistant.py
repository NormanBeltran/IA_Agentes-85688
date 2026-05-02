"""
Ejemplo de como conectarnos a Groq desde Python

Requisitos:
pip install python-dotenv
pip install groq

"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Leer configuración de las variables registradas en .env
API_KEY = os.getenv("API_KEY_GROQ")
MODEL = os.getenv("MODEL_GROQ")

# Validar que existan las variables

if not API_KEY:
    raise ValueError(f"La API_KEY para conectarnos no existe {API_KEY}")
if not MODEL:
    raise ValueError(f"El modelo para conectarnos no existe {MODEL}")

# Inicializar cliente de Groq
client = Groq(api_key=API_KEY)

#_________________________________ Funcion de conexión
def consultar_modelo(mensaje_usuario, system_prompt):
    """
    Envia un mensaje al modelo de Groq y retorna la respuesta

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
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=MODEL,
            temperature=1,
            max_tokens=1024
        )
        return chat_completion.choices[0].message.content
        #return chat_completion.choices
    except Exception as e:
        return f"Error al conectarnos a {MODEL} {e}"

#_________________________________ Main

system = "Eres un asistente útil y conciso. Responde siempre en castellano."

pregunta = "Explicame de una manera muy sencilla que es un LLM en inteligencia artificial."

print(f"El usuario pregunta: {pregunta}")
respuesta = consultar_modelo(pregunta, system)
print(f"El modelo responde {respuesta}")