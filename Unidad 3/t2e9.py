#Hacer un programa que  pida calificaciones y que muestre si está aprobado o reprobado el alumno.
a=int(input("ingrese la cantidad de claificaciones a ingresar "))
b=1
d=0
while a>=b:
	b=b+1
	c=int(input("ingrese su calificacion "))
	d=c+d
	e=d/a
	if e>=7:
		print ("felicidades, aprobaste")



