numero = input("Ingrese un número: ")
try:
        numero_int = int(numero);
        if numero_int % 2 == 0:
            print ("El número es par");
        else:
            print ("El número es impar");
except ValueError:
        print ("Por favor, ingrese un número entero válido.");
