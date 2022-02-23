a=int(input("ingrese la cantidad de alumnos solicitantes "))
while a>0:
    posibilidad=3
    oportunidad=0
    b=(input("ingrese el nombre "))
    c=(input ("vive afuera de pabellon "))
    if c=="si":
        oportunidad=oportunidad+1

    prom=float(input("ingrese el promedio "))
    if prom>=9:
        oportuidad=oportunidad+1
        beca=(input("tiene beca ?"))
        if beca=="si":
            federal=(input("es federal? "))
            if federal=="si":
                oportunidad=oportunidad+1
            else:
                oportunidad=0
        else:
            oportunidad=oportunidad+1
    else:
        if prom >=8 and prom <=9:
            deber=(input("debe alguna materia? "))
            if deber == "no":
                beca=(input("tiene beca ?"))
                if beca=="si":
                    federal=(input("es federal? "))
                    if federal=="si":
                      oportunidad=oportunidad+1
                    else:
                      oportunidad=0
                else:
                    oportunidad=oportunidad+1
            else:
              oportunidad=0
    print("las posibilidades del alumno ",b, "son ",oportunidad, "/3" )
                
    





