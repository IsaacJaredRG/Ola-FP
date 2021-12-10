Algoritmo sin_titulo
	
		
	escribir "ingrese su nombre"
	leer nombre
		b=longitud(nombre)
		
		Dimension letras[99999999]
		dimension repe[999999]
		
		para i=1 hasta b con paso 1 Hacer
			
			letras[i]=subcadena(nombre,i,i)
			repe[i]=i
			
		FinPara
		u=2
		mientras u=2 Hacer
		
		x=azar(b+1)
		si x>0 y x<=b Entonces
			u=1
		
		Para i<-1 Hasta b-1 Hacer
			// busca el menor entre i y cant
			pos_menor<-i
			Para j<-i+1 Hasta x Hacer
				Si letras[j]<letras[pos_menor] Entonces
					pos_menor<-j
				FinSi
			FinPara
			// intercambia el que estaba en i con el menor que encontro
			aux<-letras[i]
			letras[i]<-letras[pos_menor]
			letras[pos_menor]<-aux
		FinPara   
		
	FinSi
FinMientras

		// mostrar como queda la lista
		Escribir "el nombre desordenado es:"
		Para i<-1 Hasta b Hacer
			Escribir "   ",letras[i]
		FinPara
	
	
	

			

FinAlgoritmo
