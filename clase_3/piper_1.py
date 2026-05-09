import wave, os
from piper.voice import PiperVoice

# 1. Configuración de rutas
#model_path = "es_MX-ald-medium.onnx"
#config_path = "es_MX-ald-medium.onnx.json"

model_path = "es_AR-daniela-high.onnx"
config_path = "es_AR-daniela-high.onnx.json"

output_wav = "piper1.wav"

# 2. Cargar el modelo

voice = PiperVoice.load(model_path, config_path)
texto = """
En este sábado gris la lluvia escribe lento... 
sobre los techos viejas cartas de agua y viento...
el café humea tibio mientras calla la ciudad...
y el tiempo, entre las gotas, aprende a descansar...
"""

print("Generando el audio ...")

# 3. Usamos wave para setear frames
with wave.open(output_wav, "wb") as wav_file:
    voice.synthesize_wav(texto, wav_file)

# 4. Verificar el peso del archivo generado
if os.path.exists(output_wav):
    size = os.path.getsize(output_wav)
    print(f"La generación del archivo fue satisfactoria {output_wav}, el tamaño es {size /1024:2f} KB")
else:
    print("El archivo no se creo")    