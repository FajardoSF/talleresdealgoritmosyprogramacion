# Entradas
x = float(input("¿De cuantos bolivares fue el prestamo?"))
i = float(input("¿Cuánto se pago por intereses?"))

# Caja negra
a = ((i*100)/x)/4

# Salida 
print(f"El interes anual fue de {a}%")