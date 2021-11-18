#Hacer un programa que pida nombre y edad y que imprima la persona más grande. 
z=int(input("ingrese la cantidad de personas a comparar "))
y=1
x='relleno'
w=0

while z>=y:
	y=y+1
	a=str(input("ingrese su nombre "))
	b=int(input("ingrese su edad "))
	if b>w:
		x=a


print ("La persona con la mayor edad es ",x)
     






