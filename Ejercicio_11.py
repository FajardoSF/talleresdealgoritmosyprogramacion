# Entradas
nombre = str(input("\n¿Cuál es tu nombre? "))
horas = float(input("¿Cuantas horas normales has trabajado? ")) 
Ph = float(input("¿Cuanto te pagan por hora normal? "))
ex = float(input("¿Cuantas horas extra has trabajado? "))
hijos = int(input("¿Cuantos hijos tienes? ")) 

# Caja negra
Base = horas * Ph
ex = ex * (Ph + Ph * 0.25)
Sueldob = Base + ex 
Dec = Sueldob * 0.14
x = 430000 + 173000 * hijos
Sueldo = Sueldob - Dec + x 

# Salidas
print(f"\n{nombre} Por asignaciones tienes un total de {x}\nTus deducciones son un total de: {Dec}\ntu sueldo neto es de: {Sueldo}\n")