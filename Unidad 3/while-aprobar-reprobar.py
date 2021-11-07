
a = True

while a:
    cal = int(input('Dame una calificación Bro : '))

    if cal >= 7:
        print('Felicidades, no se como le hiciste pero aprobaste')
        # Esto causa que el ciclo termine
        a = False
    else:
     print('Nah, Reprobaste :(')
     a= False
