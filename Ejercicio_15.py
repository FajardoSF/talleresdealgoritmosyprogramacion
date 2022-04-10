# Entradas
PVP = float(input("\nDime cual es el precio de venta al público "))
Pf = float(input("Dime cual es el precio final "))        

# Caja negra 
D = 100 -((Pf*100)/PVP)

# Salida
print(f"\nTu descuento fue de {D}%\n")