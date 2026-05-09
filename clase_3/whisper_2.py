import whisper

# Cargar el modelo 
model = whisper.load_model("small")

# Transcribir un archivo de audio
resultado = model.transcribe("pyttsx3_4.wav", task="translate")

print(f"Texto detectado en el audio: {resultado['text']}")