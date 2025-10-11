numero = input("Ingrese el primer número: ");
numero2 = input("Ingrese el segundo número: ");
numero3 = input("Ingrese el tercer número: ");

if numero >= numero2 and numero >= numero3:
    print ("El primer número es el mayor:", numero);
elif numero2 >= numero and numero2 >= numero3:
    print ("El segundo número es el mayor:", numero2);
else:
    print ("El tercer número es el mayor:", numero3);
