#Ejercicio 2: Hacer un programa que te pida las calificaciones (5 calificaciones) y que te de el promedio.
prom=0;
cal1 = float(input('Ingrese la primer calificación : '))
cal2 = float(input('Ingrese la segunda calificación : '))
cal3 = float(input('Ingrese la tercer calificación : '))
cal4 = float(input('Ingrese la cuarta calificación : '))
cal5 = float(input('Ingrese la quinta calificación : '))
prom= ((cal1+cal2+cal3+cal4+cal5)/5)
print("El promedio de las 5 calificaciones es:",prom)