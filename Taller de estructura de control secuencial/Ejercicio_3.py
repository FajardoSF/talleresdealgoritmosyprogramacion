# Entradas
Base = float(input("Dime tu sueldo base\n"))
V_0 = float(input("Dime el valor de la venta 1\n"))
V_1 = float(input("Dime el valor de la venta 2\n"))
V_2 = float(input("Dime el valor de la venta 3\n"))

# Caja negra
Comisiones = (V_0+V_1+V_2) * 0.1
Total = (Comisiones + Base)

# Salidas
print(f"Tu valor por comisines de ventas es {Comisiones} Y el total es {Total}")