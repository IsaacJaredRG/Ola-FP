Algoritmo clasearreglo
	//Programa que te pida el nombre de una clase y sus atributos y los guarde en un arreglo.
	Escribir "ingrese el nombre de la clase"
	leer nombclass
	Escribir "ingrese la cantidad de atributos a agregar"
	leer xd
	dimension class[900000];
	
	Para i<-1 hasta xd con paso 1 hacer
		escribir "ingrese el atributo"	
		leer class[i]
	FinPara
	escribir "es la clase ",nombclass
	escribir "con los atributos "
	Para i=1 hasta xd con paso 1 Hacer
		escribir "el atributo que hay en la posicion ",i," es: ",class[i]
	FinPara
	
	
	
FinAlgoritmo
