import speech_recognition as sr
    
r = sr.Recognizer()

# Cargar un archivo de audio
with sr.AudioFile("gtts1.wav") as source:
    audio_data = r.record(source)

    try:
        texto = r.recognize_google(audio_data, language="es-AR")
        print(f"Contenido del audio: {texto}")
    except Exception as e:
        print(f"Error {e}")