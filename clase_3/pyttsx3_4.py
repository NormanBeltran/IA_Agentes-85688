import pyttsx3

engine = pyttsx3.init()

engine.save_to_file("Hola, soy una voz que funciona sin internet. Bienvenidos a la clase 3 de text to speech", "pyttsx3_4.wav")

engine.runAndWait()