letra = input("Ingresa una letra: ").lower()
if letra in "aeiou":
    print("Es vocal.")
elif letra.isalpha():
    print("Es consonante.")
else:
    print("No es una letra válida.")
