limite = int(input("Ingresa el límite: "))
a, b = 0, 1
while a <= limite:
    print(a)
    a, b = b, a + b
