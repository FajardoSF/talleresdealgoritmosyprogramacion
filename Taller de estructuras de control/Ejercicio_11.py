"""
Entradas
temperatura en grados farenheit-->float-->t
Salidas
Deporte-->str-->d
"""
#Entradas
t=float(input("digite temperatura: "))
#Caja negra
d=""
if(t>85 and t<=120):
    d="Natacion"
elif(t>70 and t<=85):
    d="tenis"
elif(t>33 and t<=70):
    d="golf"
elif(t>10 and t<=32):
    d="esqui"
elif(t>=0 and t<=10):
    d="marcha"
else:
    d="La temperatura no pertenece a ningun deporte"
#Salida
print(f"El deporte a practicar es: {d}")
