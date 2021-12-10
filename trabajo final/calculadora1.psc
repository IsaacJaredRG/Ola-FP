Algoritmo calculadora
	a=2
	Mientras a=2 Hacer
		//restablecer valores
		num2=0
		sum=0
		e=0
		mul=1
		div=1
		//eleccion
		Escribir "a continuacion se le daran una serie de opciones a elegir, para elegir una opcion, escriba correctamente la operacion a elegir"
		Escribir "-Suma"
		Escribir "-Resta"
		Escribir "-Multiplicacion"
		Escribir "-Division "
		Escribir "para salir escriba: esc"
		leer b
		c= longitud(b)
		
		Segun c Hacer
			//suma
			4:
				Escribir "ingrese la cantidad de digitos a sumar"
				leer d
				Mientras e<d Hacer
					e=e+1
					escribir "ingrese el ",e, "° numero "
					leer num1
					sum=num1+sum
					
				Fin Mientras
				escribir "el resultado es ", sum
				
			//resta	
			5:
				Escribir "ingrese la cantidad a la cual se le va a hacer la resta"
				leer num2
				Escribir "ingrese la cantidad de digitos a restar"
				leer d
				
				res=num2
				Mientras e<d Hacer
					e=e+1
					escribir "ingrese el ",e, "° numero "
					leer num1
					res=res-num1
					
				Fin Mientras
				escribir "el resultado es ", res	
				
			//multiplicación
			14:
				Escribir "ingrese la cantidad de numeros a multiplicar"
				leer d
				Mientras e<d Hacer
					e=e+1
					escribir "ingrese el ",e, "° numero "
					leer num1
					mul=mul*num1
					
				Fin Mientras
				escribir "el resultado es ", mul
				
			//division	
			8:
				Escribir "ingrese la cantidad la cual va a ser dividida"
				leer num2
				Escribir "ingrese la cantidad de numeros que lo van a dividir"
				leer d
				div=num2
				Mientras e<d Hacer
					e=e+1
					escribir "ingrese el ",e, "° numero "
					leer num1
				div=(div/num1)
					
				Fin Mientras
				escribir "el resultado es ", div
			3:
				a=1
			De Otro Modo:
				escribir "no escribiste la opcion valida"
		Fin Segun
	Fin Mientras
	
	
FinAlgoritmo
