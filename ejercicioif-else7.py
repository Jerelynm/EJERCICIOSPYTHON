from datetime import datetime
año = int(input("Ingresa tu año de nacimiento: "))
actual = datetime.now().year
if 1900 < año < actual:
    print("Año válido.")
else:
    print("Año inválido.")
