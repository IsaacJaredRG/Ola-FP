Algoritmo PersonaMayor
	//numeros fibonacci 0,1,1,2,3,5,8
	num1=0
	num2=0
	num3=1
	num4=1
	e=0
	f=0
	
	Escribir "Dame la cantidad de numeros fibonacci a sumar"
	Leer num1;
	
	Mientras (e < num1) Hacer
		//controlador
		e=e+1
		//numero fibonacci
		escribir num2
		//suma de los valores
		f=num2+f
		//operaciones
		num4=num2+num3	
		num2=num3
		num3=num4
		
	FinMientras

	escribir "la suma de los numeros es ",f
FinAlgoritmo
