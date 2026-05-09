import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")

for index, voice in enumerate(voices):
    # Forzar la inicializacion de las voces en cada vuelta
    engine = pyttsx3.init()

    engine.setProperty("voice", voice.id)
    print(f"Probando con la voz {voice.name} - {voice.id}")
    engine.say("Hola, soy una voz que funciona sin internet. Bienvenidos a la clase 3 de text to speech")
    engine.runAndWait()
    del engine

