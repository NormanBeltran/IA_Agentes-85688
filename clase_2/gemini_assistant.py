"""
Ejemplo de como conectarnos a Gemini desde Python

Requisitos:
pip install python-dotenv
pip install google-genai

"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Leer configuración de las variables registradas en .env
API_KEY = os.getenv("API_KEY_GEMINI")
MODEL = os.getenv("MODEL_GEMINI")

# Validar que existan las variables

if not API_KEY:
    raise ValueError(f"La API_KEY para conectarnos no existe {API_KEY}")
if not MODEL:
    raise ValueError(f"El modelo para conectarnos no existe {MODEL}")

# Inicializar cliente de Groq
client = genai.Client(api_key=API_KEY)

#_________________________________ Funcion de conexión
def consultar_modelo(mensaje_usuario, system_prompt):
    """
    Envia un mensaje al modelo de Groq y retorna la respuesta

    """
    try:
        #model_kwargs = {"model_name": MODEL}
        #if system_prompt:
        #    model_kwargs["system_instruction"] = system_prompt

        response = client.models.generate_content(
            model=MODEL,
            contents = mensaje_usuario,
            config = types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=1,
                max_output_tokens=1024
            )
        )
        return response.text
        
    except Exception as e:
        return f"Error al conectarnos a {MODEL} {e}"

#_________________________________ Main

system = "Eres un asistente útil y conciso. Responde siempre en castellano."

pregunta = "Explicame que es la vida."

print(f"El usuario pregunta: {pregunta}")
respuesta = consultar_modelo(pregunta, system)
print(f"El modelo responde {respuesta}")