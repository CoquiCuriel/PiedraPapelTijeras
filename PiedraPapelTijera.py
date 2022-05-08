"""
Created on Sat May  7 22:01:50 2022

@author: Ricardo Curiel
"""
import random
print("*"*10+"BIENVENIDO"+"*"*10)

opcion = input("¿Piedra (1), Papel (2) o Tijera (3)?")
while(opcion.isdigit()==False or int(opcion)<1 or int(opcion)>3):
    opcion = input("Ingrese una opcion válida")
opcion = int(opcion)

maquina = random.randint(1, 3)
print("Opción de máquina: ",maquina)

if(opcion == maquina):
    print("empate")
if(opcion==1 and maquina==2):
    print("gana papel(maquina)")
if(opcion==1 and maquina==3):
    print("Gana piedra(player)")
if(opcion==2 and maquina==1):
    print("gana papel(player)")
if(opcion==2 and maquina==3):
    print("gana tijeras(maquina)")
if(opcion==3 and maquina==1):
    print("gana piedra(maquina)")
if(opcion==3 and maquina==2):
    print("Gana tijera(player)")

