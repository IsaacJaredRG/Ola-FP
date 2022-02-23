Algoritmo becas
	
	Escribir "cuanto alumnos se tomaran en cuenta?"
	Leer a
	mientras a > 0 hacer
		posibilidad=3
		oportunidad=0
		Escribir "ingrese el nombre del alumno"
		Leer b
		Escribir "¿vive afeura de Pabellon?"
		Leer c
		Si c= "si" entonces
			
			oportunidad=oportunidad+1
		SiNo
			
		FinSi
		Escribir "ingrese el promedio"
		Leer prom
		si prom>=9 Entonces
			
			oportunidad=oportunidad+1
			
			Escribir "tine una beca?"
			leer beca
			si beca ="si" Entonces
				Escribir "es federal?"
				Leer federal
				si federal= "si" entonces
					oportunidad=oportunidad+1
				SiNo
					oportunidad=0
					
				FinSi
			SiNo
				oportunidad =oportunidad+1
			FinSi
			
		sino
			si prom>=8 y prom <=9 Entonces
				Escribir "debe alguna materia?"
				Leer deber
				si deber = "si" Entonces
					oportunidad=0
				SiNo
					oportunidad=oportunidad+1
					Escribir "tine una beca?"
					leer beca
					si beca ="si" Entonces
						Escribir "es federal?"
						Leer federal
						si federal= "si" entonces
							oportunidad=oportunidad+1
						SiNo
							oportunidad=0
							
						FinSi
					SiNo
						oportunidad=oportunidad+1
					FinSi
				FinSi
			SiNo
				
				oportunidad=0
			FinSi
			
		FinSi
		Escribir b
		Escribir "las posibilidades son: ",oportunidad, "/3"
	FinMientras

		
	
	
	
	
FinAlgoritmo
