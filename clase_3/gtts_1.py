from gtts import gTTS

from pydub import AudioSegment

texto = """
En este sábado gris la lluvia escribe lento
sobre los techos viejas cartas de agua y viento,
el café humea tibio mientras calla la ciudad,
y el tiempo, entre las gotas, aprende a descansar.
"""

#tts = gTTS(text=texto, lang="es", slow=False, tld="es")
#tts = gTTS(text=texto, lang="es", slow=True, tld="com.mx")
tts = gTTS(text=texto, lang="es", slow=True, tld="com")

tts.save("gtts1.mp3")

# Convertir mp3 a wav (usando pydub)
audio = AudioSegment.from_mp3("gtts1.mp3")
audio.export("gtts1.wav", format="wav")

print("Archivo guardado como gtts1.mp3")