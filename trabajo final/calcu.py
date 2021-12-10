#calculadora
a=2	 
while a==2:
	#restablecer valores
	num2=0
	sum=0
	e=0
	mul=1
	di=1
	suma=0
	resta=0

	#eleccion
	print("a continuacion se le daran una serie de opciones a elegir, para elegir una opcion, escriba correctamente la operacion a elegir")
	print("-Suma")
	print("-Resta")
	print("-Multiplicacion")
	print("-Division ")
	b=str(input("para salir escriba: esc " ))
	c= len(b)

	#suma
	if c==4:
		d= int(input("ingrese la cantidad de digitos a sumar "))
		while e<d:
			e=e+1
			num1=float(input("ingrese el numero "))
			suma=num1+suma		

		print ("el resultado es ", suma)
				
	#resta	
	if c==5:
		num2=float(input ("ingrese la cantidad a la cual se le va a hacer la resta "))		
		d=float(input ("ingrese la cantidad de digitos a restar "))
		res=num2
		while e<d:

			e=e+1
			num1=float(input("ingrese el numero "))
			res=res-num1

		print ("el resultado es ", res)
				
			#multiplicación
	if c==14:
		d=float(input("ingrese la cantidad de numeros a multiplicar "))
		while e<d:
			e=e+1
			num1=float(input ("ingrese el numero "))

			mul=mul*num1
		print ("el resultado es ", mul)
				
	#division	
	if c==8:
		num2=float(input ("ingrese la cantidad la cual va a ser dividida "))
		d=float(input ("ingrese la cantidad de numeros que lo van a dividir "))
		di=num2

		while e<d:
			e=e+1
			num1=float(input ("ingrese el numero "))
			di=(di/num1)
		print ("el resultado es ", di)
					
				
	 
	if c==3:
	    a=1
	 


	 

				

		