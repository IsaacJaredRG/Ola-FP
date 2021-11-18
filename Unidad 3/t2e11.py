#Desarrollar un algoritmo que te pida dos palabras y que te imprima la palabra con el mayor número de letras
print("a proximación agragará 2 palabras para comparar su longitud")
a=str(input("Ingrese la primer palabra "))
b=str(input("Ingrese la segunda palabra "))
c=len(a)
d=len(b)

if c>d:
	print("la palabra con mayor longitud es",a)
else:
	print("la palabra con mayor longitud es",b)