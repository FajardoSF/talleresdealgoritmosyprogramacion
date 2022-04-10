# Entradas
a = float(input("Dime el los lados de triángulo\n"))
b = float(input())
c = float(input())

# Caja negra
s = (a+b+c)/2
Area = (s*(s-a)*(s-b)*(s-c))**0.5

# Salida
print(Area)