import speech_recognition as sr  
    
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Ajustando ruido de fondo ... espere un momento...")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Ya puede hablar ...")

    # Tiempo maximo de silencio antes de considerar que la frase termino
    r.pause_threshold = 2

    # Capturar el audio
    audio = r.listen(source) # timeout = 5 

    try:
        # Reconocimiento usando google
        texto = r.recognize_google(audio, language="es-AR")
        print(f"Tu has dicho: {texto}")

    except Exception as e:
        print(f"Tuvimos un inconveniente {e} ... {e.__class__}")

