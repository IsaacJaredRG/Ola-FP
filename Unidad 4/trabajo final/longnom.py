
#Programa que ingreses el nombre completo de dos personas y te cuente el número de letras de cada nombre. Después que imprima cual es mayor.

a=str(input ("ingrese el primer nombre a medir "))
b=(input ("Ingrese el segundo nombre a medir "))
	
c=len(a)
d=len(b)
	
if c<d:

	print ("El nombre mas largo es ",b)
else:
	print( "El nombre mas largo es ",a)
