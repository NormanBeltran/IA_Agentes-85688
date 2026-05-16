import os
from  dotenv import load_dotenv

from groq import Groq 

load_dotenv()

API_KEY = os.getenv("API_KEY_GROQ")
MODEL = os.getenv("MODEL_GROQ")

client = Groq(api_key=API_KEY)

def consultar_modelo(mensaje_usuario, system_prompt):
    messages = []

    # Rol del sistema, ej. Eres un experto ...
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
            temperature=0.9,
            max_tokens=1024
        )
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return f"Error al consultar le modelo {e}"

#______________________ main
system = "Eres un escritor creativo, especializado en poemas romanticos"
pregunta = "Escribi un poema de 2 estrofas de un raton mirando la luna desde una montaña"
respuesta = consultar_modelo(pregunta, system)
print(f"Modelo usado: {MODEL}\n{respuesta}")
    
