#Programa en el que pidas un número del 1 al 10 y que haga un sorteo de un número ganador entre ese rango de forma aleatoria
import random
b=random.randint(1,10)
a=int(input("escoge un numero del 1 al 10 para el sorteo "))
		
print ("el ganador del sorteo es ",b)
if b==a:
	print ("felicidades!, ganaste!")
else:
	print("que mal!, suerte para la proxima")




			