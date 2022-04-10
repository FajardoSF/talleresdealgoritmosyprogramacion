# Entrada
P = float(input("\nDimé el valor del Computador pagando de contados\n"))
C = float(input("\nDimé el valor por cada cuota\n "))

# Caja negra
C = C*12
a = (((C*100)/P)-100)
b = (((C*100)/P)-100)/12
# Salida 
print(f"Por recargo el porcentaje es de {a}% y por cuota es de {b}%")