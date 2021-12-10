Algoritmo areasfiguras
	//Programa que saque el área de un círculo, un cuadrado, rectángulo y triángulo.
	escribir "A continuación se le pediran datos de las figuras a sacar el área"
	//area circulo
	Escribir "ingrese el radio del circulo para sacar su área (recuerde que el radio es la mitad del diametro)"
	Leer radio
	aci=(3.1416)*(radio^2)
	Escribir "El area del circulo es: ",aci
	
	//area cuadrado
	escribir "Ingrese un lado del cuadrado para sacar su area"
	leer lado
	acu=lado*lado
	escribir "el área del cuadrado es: ",acu
	
	//area rectangulo
	escribir "ahora se le sacara el área al rectangulo"
	escribir "ingrese la base de la figura"
	leer base
	escribir "ingrese la altura de la figura"
	leer altura
	are=base*altura
	escribir "el area del rectangulo es: ",are
	
	//area triangulo
	escribir "ahora se le sacara el área del triangulo"
	escribir "ingrese la base de la figura"
	leer basetri
	escribir "ingrese la altura de la figura"
	leer alturatri
	atr=(basetri*alturatri)/2
	escribir "el area del rectangulo es: ",atr
	
FinAlgoritmo
