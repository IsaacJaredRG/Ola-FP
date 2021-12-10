#Programa que saque el área de un círculo, un cuadrado, rectángulo y triángulo.
print ("A continuación se le pediran datos de las figuras a sacar el área")
#area circulo
radio=float(input ("ingrese el radio del circulo para sacar su área (recuerde que el radio es la mitad del diametro) "))
aci=(3.1416)*(radio*radio)
print ("El area del circulo es: ",aci)
	
#area cuadrado
lado=float(input ("Ingrese un lado del cuadrado para sacar su area "))
acu=lado*lado
print ("el área del cuadrado es: ",acu)
	
#area rectangulo
print ("ahora se le sacara el área al rectangulo")
base=float(input ("ingrese la base de la figura "))
altura=float(input("ingrese la altura de la figura "))
are=base*altura
print ("el area del rectangulo es: ",are)
	
#area triangulo
print ("ahora se le sacara el área del triangulo")
basetri=float(input ("ingrese la base de la figura "))

alturatri=float(input ("ingrese la altura de la figura "))
atr=((basetri*alturatri)/2)
print ("el area del rectangulo es: ",atr)

