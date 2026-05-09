from gtts import gTTS
import os

texto = """
El sol derrama oro sobre la playa mientras el mar, tranquilo y eterno, peina la arena con manos de espuma.
"""

#tts = gTTS(text=texto, lang="es", slow=False, tld="es")
#tts = gTTS(text=texto, lang="es", slow=True, tld="com.mx")
tts = gTTS(text=texto, lang="es", slow=True, tld="com")

tts.save("gtts2.mp3")

os.system("start gtts2.mp3")