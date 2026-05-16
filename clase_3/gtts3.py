# IMPORTANTE:
# audioop fue removido en Python 3.13
# este parche hace que pydub pueda seguir funcionando

import sys
import audioop_lts

# reemplaza el módulo faltante
sys.modules["audioop"] = audioop_lts

from gtts import gTTS
from pydub import AudioSegment

texto = """
En este sábado gris la lluvia escribe lento
sobre los techos viejas cartas de agua y viento,
el café humea tibio mientras calla la ciudad,
y el tiempo, entre las gotas, aprende a descansar.
"""

# Generar MP3 con Google TTS
tts = gTTS(
    text=texto,
    lang="es",
    slow=True,
    tld="com"
)

tts.save("gtts1.mp3")

# Convertir MP3 a WAV
audio = AudioSegment.from_mp3("gtts1.mp3")
audio.export("gtts1.wav", format="wav")

print("Archivos generados:")
print("- gtts1.mp3")
print("- gtts1.wav")