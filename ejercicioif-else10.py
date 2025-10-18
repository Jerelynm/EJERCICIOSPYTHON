precio = float(input("Precio del artículo: "))
descuento = float(input("Porcentaje de descuento: "))
final = precio * (1 - descuento / 100)
print(f"Precio final: Q{final:.2f}")
