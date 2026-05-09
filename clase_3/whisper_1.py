import whisper

# Cargar el modelo 
# small, base, tiny, medium, large

model = whisper.load_model("base")

# Transcribir un archivo de audio
resultado = model.transcribe("gtts1.mp3")

print(f"Texto detectado en el audio: {resultado['text']}")