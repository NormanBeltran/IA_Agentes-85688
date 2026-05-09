import whisper
import numpy as np 
import sounddevice as sd

# Cargar el modelo 
# small, base, tiny, medium, large

model = whisper.load_model("small")

def callback(indata, frames, time, status):
    # Convertir el audio capturado para Whisper lo entienda
    audio_data = indata.flatten().astype(np.float32)

    resultado = model.transcribe(audio_data, fp16=False, language="es", task="transcribe")
    if resultado['text'].strip():
        print(f"Escuchando {resultado['text']}")

# Escuchar rafagas de 3 segundos
with sd.InputStream(samplerate=16000, channels=1, callback=callback, blocksize=64000):
    print("Escuchando ... Presiona Ctrl-C para terminar")
    sd.sleep(100000)
