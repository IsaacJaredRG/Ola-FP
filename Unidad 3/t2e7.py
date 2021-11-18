#Hacer un programa que te de 5 opciones de peliculas y al momento de seleccionar una te imprima el nombrre de la película.
print("las peliculas son: \n 1.Shrek \n 2. Shrek 2 \n 3. Shrek 3 \n 4.Shrek para siempre \n 5. Kung fu panda \n")
a=int(input("Seleccione por su numero una de las peliculas anteriores " ))


if a == 1:
    print("La pelicula es Shrek")
elif a == 2:
    print("La pelicula es Shrek 2")
elif a == 3:
   print("La pelicula es Shrek 3, que mal gusto tienes, pero bueno")
elif a == 4:
    print("La pelicula es Shrek para siempre")
elif a == 5:
    print("La pelicula es Kung fu panda")
else:
   print("No escogió un valor valido")

