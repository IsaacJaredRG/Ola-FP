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
	ESCRIBIR ("Dame la primera calificación");
	LEER cal1;
	ESCRIBIR ("Dame la segunda calificación");
	LEER cal2;
	ESCRIBIR ("Dame la tercera calificación");
	LEER cal3;
	ESCRIBIR ("Dame la cuarta calificación");
	LEER cal4;
	ESCRIBIR ("Dame la quinta calificación");
	LEER cal5;
	suma=cal1+cal2+cal3+cal4+cal5;
	promedio= suma/5;
	ESCRIBIR "Tu promedio es: ", promedio;
FinAlgoritmo
