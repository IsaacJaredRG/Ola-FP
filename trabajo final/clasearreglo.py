#Programa que te pida el nombre de una clase y sus atributos y los guarde en un arreglo.
nombclass=str(input("ingrese el nombre de la clase "))
atri=int(input("ingrese la cantidad de atributos a agregar "))

clases=[]
for i in range (atri):
	clase=str(input ("ingrese el atributo {i + 1 }"))
	clases.append(clase)

print ("te mostraré los atributos que ingrsaste: ")
print ("tu clase es ")

for clase in clases:
	print(clase)

   


