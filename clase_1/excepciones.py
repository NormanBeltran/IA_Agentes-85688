a = input("Ingrese su edad:")

try:
    edad = int(a)
    print(f"Ud en su proximo cumple va a tener {edad+1} años")
except Exception as e:
    print(f"Es probable que el valor ingresado no sea numerico: {e.__class__}")