#Desarrollar un algoritmo para realizar sorteos.
import random
a=int(input("ingrese el número inicial del sorteo "))
b=int(input("ingrese el ultimo numero del sorteo "))
 
print("el ganador del sorteo es ",random.randint(a,b))