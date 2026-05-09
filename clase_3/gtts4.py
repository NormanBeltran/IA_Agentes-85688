from gtts import gTTS

def crear_audio(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()

        tts = gTTS(text=contenido, lang="es")

        tts.save("gtts4.mp3")
        print("Lectura completada en gtts4.mp3")
    except Exception as e:
        print("El archivo no se pudo leer")

#________________________ Main
crear_audio("articulo.txt")