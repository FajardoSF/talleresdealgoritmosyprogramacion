# Entradas
H = int(input("Dime la cantidad de hombres\n"))
M = int(input("Dime la cantidad de mujeres\n"))

# Caja negra
Ph = (H*100)/(H+M)
Pm = (M*100)/(H+M)
 
# Salida
print("El porcentaje de hombres es",Ph,"%","El porcentaje de mujeres es",Pm,"%\n")