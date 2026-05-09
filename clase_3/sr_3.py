import speech_recognition as sr  
import os
    

def ejecutar_comando():    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Comandos disponibles 'abrir editor' 'abrir calculadora' 'salir'")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        # Reconocimiento usando google
        texto = r.recognize_google(audio, language="es-AR").lower()
        print(f"Comando recibido: {texto}")

        if "abrir editor" in texto:
            os.system("notepad.exe")
        elif "abrir calculadora" in texto:
            os.system("calc.exe")
        elif "salir"  in texto:
            raise False
    except Exception as e:
        print(f"Tuvimos un inconveniente {e} ... {e.__class__}")

#____________________main
# 

ejecutar_comando()        