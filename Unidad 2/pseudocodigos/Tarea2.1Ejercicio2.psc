//Ejercicio 1 Tarea 2.1
//Isaac Jared
//ITPA
//TICs
//Ejercicio 2: Hacer un programa que te pida las calificaciones (5 calificaciones) y que te de el promedio.
Algoritmo CalificacionesPromedio
	cal1=0;
	cal2=0;
	cal3=0;
	cal4=0;
	cal5=0;
	suma=0;
	promedio=0;
	ESCRIBIR ("Dame la primera calificaci�n");
	LEER cal1;
	ESCRIBIR ("Dame la segunda calificaci�n");
	LEER cal2;
	ESCRIBIR ("Dame la tercera calificaci�n");
	LEER cal3;
	ESCRIBIR ("Dame la cuarta calificaci�n");
	LEER cal4;
	ESCRIBIR ("Dame la quinta calificaci�n");
	LEER cal5;
	suma=cal1+cal2+cal3+cal4+cal5;
	promedio= suma/5;
	ESCRIBIR "Tu promedio es: ", promedio;
FinAlgoritmo
