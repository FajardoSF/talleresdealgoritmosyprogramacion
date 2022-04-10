# Entrada
Ph = float(input("Dime el precio por cada hora trabajada\n"))
h = float(input("Dime el numero de horas trabajadas\n"))

# Caja negra
a = Ph*h
Neto = a - a * 0.20

# Salida
print("El salario Neto es",Neto)