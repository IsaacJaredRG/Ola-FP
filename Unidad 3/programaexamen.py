#Desarrollar un programa que guarde a todos los integrantes del grupo como objetos
#con los siguientes atributos: Edad, Calificacion de los diferentes materias, promedio, 
#calificacion de la prepa y lugares de residencia. 
#Imprimir o mostrar los siguientes reportes:
#5 alumnos con mayor edad (dias incluidos)
#Promedio de toda la preparatoria 
#Alumnos que viven mas cerca y mas lejos
#Materia con mejor rendimiento.

#crear clase
class Alumno():
 	def __init__ (self,edad,nombre,cd,fp,fi,it,te,ing,md,calprep,lugaresidencia,distanciatec):
 		self.nombre= nombre
 		self.edad = edad
 		self.cd = cd
 		self.fp = fp
 		self.fi = fi
 		self.it = it
 		self.te = te
 		self.ing = ing
 		self.md = md
 		self.calprep = calprep
 		self.lugaresidencia = lugaresidencia
 		self.distanciatec=distanciatec

#crear objetos
reyna = Alumno(18,"Reyna", 9, 8, 10, 10, 9, 6, 7, 9, "Emiliano Zapata", 13)
mirozlava = Alumno(18,"Mirozalva",9, 8, 10, 7, 9, 6, 7, 8, "Cosio", 27)
mely = Alumno (18,"Melany", 5, 5, 7, 5, 5, 5, 5, 9, "pabellon", 5)
diego = Alumno(19,"Diego", 8, 9, 9, 10, 8, 8, 10, 10, "rincón", 13) 
britzy = Alumno(18,"Britzy", 10, 9, 10, 10, 8, 8, 10, 10, "rincón", 13) 
fernando = Alumno(17, "Fernando", 8, 8, 7, 9, 10, 8, 10, 9, "pabellon", 5)
alejandra = Alumno(18,"Alejandra", 10, 10, 10, 10, 10, 10, 10, 8, "jesus maria", 27)
alejandro= Alumno(19, "Alejandro", 10, 9, 8, 9, 8, 9, 8, 9, "Ejido Fresnillo", 17)
donaldo= Alumno(18, "Donaldo", 8, 9, 10, 9, 8, 6, 8, 8, "pabellon", 5)
austin= Alumno(18, "Austin", 10, 9, 8, 9, 10, 9, 8, 8, "pabellon", 5)
paola=Alumno(18,"Paola", 10, 9, 8, 9, 10, 9, 8, 8, "carboneras", 8)
isaac=Alumno(19, "Isaac", 10, 9, 10, 9, 10, 10, 10, 9, "rincon", 13)
areli=Alumno(19, "Areli", 10, 9, 10, 9, 10, 9, 10, 8, "rincon", 13)
alain=Alumno(18, "Alain", 10, 9, 10, 9, 10, 9, 10, 8, "asientos", 11)
alexis=Alumno(19, "Alexis", 10, 9, 10, 8, 7, 8, 7, 8, "rincon", 13)
#alumnos con mayor edad
print ("los alumnos con mayor edad son ", diego.nombre,",",alejandro.nombre,",",isaac.nombre,",",areli.nombre,"y",alexis.nombre )
#alumnos con su promedio
print ("los alumnos y sus calificaciones se presentaran a continuación\n", reyna.nombre,"con promedio de",reyna.calprep,",\n",mirozlava.nombre,"con promedio de",mirozlava.calprep)
print(mely.nombre,"con promedio de",mely.calprep,",\n",diego.nombre,"con promedio de",diego.calprep,",\n",britzy.nombre,"con promedio de",britzy.calprep)
print(fernando.nombre,"con promedio de",fernando.calprep,",\n",alejandra.nombre,"con promedio de",alejandra.calprep,",\n",alejandro.nombre,"con promedio de",alejandro.calprep)
print(donaldo.nombre,"con promedio de",donaldo.calprep,",\n",austin.nombre,"con promedio de",austin.calprep,",\n",paola.nombre,"con promedio de",paola.calprep)
print(isaac.nombre,"con promedio de",isaac.calprep,",\n",areli.nombre,"con promedio de",areli.calprep,",\n",alain.nombre,"con promedio de",alain.calprep,",\n",alexis.nombre,"con promedio de",alexis.calprep)
#alumnos que viven mas cerca y mas lejos
print("Los alumnos que viven mas lejos del tec son:\n",mirozlava.nombre,"es de ",mirozlava.lugaresidencia, "con una distancia de", mirozlava.distanciatec, "y\n", alejandra.nombre, "es de", alejandra.lugaresidencia, "con una distancia de",alejandra.distanciatec )
print("Los alumnos que viven mas cerca del tec son:\n",mely.nombre,"es de ",mely.lugaresidencia, "con una distancia de", mely.distanciatec, "y\n", donaldo.nombre, "es de", donaldo.lugaresidencia, "con una distancia de",donaldo.distanciatec )
#alumnos y su mejor calificacion de materia
print ("los alumnos y sus mejoras se presentaran a continuación\n", reyna.nombre,"con la meteria de fundamentos de la programacion",",\n",mirozlava.nombre,"con la meteria de fundamentos de la investigación")
print(mely.nombre,"con la materia de fundamentos de la investigacion",",\n",diego.nombre,"con la materia de fundamentos de mates discretas",",\n",britzy.nombre,"con la materia de calculo diferencial")
print(fernando.nombre,"con la materia de matematicas discretas",",\n",alejandra.nombre,"con la materia de introduccion a las tics",",\n",alejandro.nombre,"con la materia de calculo diferencial")
print(donaldo.nombre,"con la materia de calculo diferencial",",\n",austin.nombre,"con la materia de ingles ",",\n",paola.nombre,"con la materia de calculo diferencial ")
print(isaac.nombre,"con la materia de calculo diferencial",",\n",areli.nombre,"con la materia de fundamentos de la investigacion",",\n",alain.nombre,"con la materia de ingles",",\n",alexis.nombre,"con la materia de calculo diferencial ")
