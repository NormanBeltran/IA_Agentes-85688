import os
from dotenv import load_dotenv
from groq import Groq

# Cargar variables desde el archivo .env
load_dotenv()

# Leer configuración externa
API_KEY = os.getenv("API_KEY_GROQ")
MODEL = os.getenv("MODEL_GROQ")

print(f"Modelo: {MODEL}")

# Validar que existan las variables
if not API_KEY:
    raise ValueError("❌ API_KEY_GROQ no está definida en el archivo .env")
if not MODEL:
    raise ValueError("❌ MODEL_GROQ no está definida en el archivo .env")

# Inicializar cliente
client = Groq(api_key=API_KEY)


def consultar_modelo(historial: list, system_prompt: str = None) -> str:
    """
    Envía el historial completo al modelo de Groq y retorna la respuesta.
    
    Args:
        historial: Lista de mensajes con la conversación acumulada.
        system_prompt: (Opcional) Instrucciones de comportamiento del sistema.
    
    Returns:
        El contenido de la respuesta del modelo.
    """
    messages = []
    
    # Agregar system prompt solo al inicio si existe
    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })
    
    # Agregar todo el historial de conversación
    messages.extend(historial)
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=MODEL,
            temperature=0.7,
            max_tokens=1024
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        return f"Error al consultar Groq: {e}"


# --- Chatbot interactivo con memoria ---
if __name__ == "__main__":
    # Prompt de sistema opcional
    system = "Eres un asistente útil y conciso. Responde siempre en español."
    
    # Historial de conversación (memoria)
    historial = []
    
    print("🤖 Chatbot iniciado. Escribe 'salir' para terminar la conversación.\n")
    
    while True:
        # Leer input del usuario
        pregunta = input("🧑 Tú: ").strip()
        
        # Condición de salida
        if pregunta.lower() == "salir":
            print("\n👋 ¡Hasta luego! La conversación ha terminado.")
            break
        
        # Ignorar mensajes vacíos
        if not pregunta:
            continue
        
        # Agregar mensaje del usuario al historial
        historial.append({
            "role": "user",
            "content": pregunta
        })
        
        # Consultar al modelo enviando todo el historial
        respuesta = consultar_modelo(historial, system_prompt=system)
        
        # Agregar respuesta del asistente al historial
        historial.append({
            "role": "assistant",
            "content": respuesta
        })
        
        print(f"🤖 {MODEL}: {respuesta}\n")