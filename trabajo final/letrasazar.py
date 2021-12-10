#Programa que pida el nombre de una persona y lo imprima con las letras de forma aleatoria
import random
from random import shuffle

a=str(input ("ingrese su nombre "))
b=len(a)

letras=[]

for i in range (b):
	letra=a[i]
	letras.append(letra)
	
random.shuffle(letras)
print (letras)














