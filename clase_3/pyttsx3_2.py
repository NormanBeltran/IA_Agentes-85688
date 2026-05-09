import pyttsx3

engine = pyttsx3.init()

# Velocidad
rate = engine.getProperty("rate") # Obtener la velocidad
engine.setProperty("rate", 100)

volumen = engine.getProperty("volume")
engine.setProperty("volume", 0.8)

print(f"Velocidad por default {rate}, volumen {volumen}")
engine.say("Hola, soy una voz que funciona sin internet. Bienvenidos a la clase 3 de text to speech")

engine.runAndWait()