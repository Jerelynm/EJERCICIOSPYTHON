total = 0
contador = 0
while True:
    num = input("Ingresa un número (o 'fin' para terminar): ")
    if num.lower() == "fin":
        break
    total += float(num)
    contador += 1
if contador > 0:
    print(f"Media: {total / contador}")
else:
    print("No se ingresaron números.")
