print ("SISTEMA PARA CALCULAR EL PROMEDIO DE UN ALUMNO")

nombre = input ("Para comenzar, ¿Cual es tu nombre? ")

matematicas = int(input (nombre + "¿Cual es tu calificación en matemáticas: "))
quimica = int(input (nombre + "¿Cual es tu calificación en química: "))
biologia = int(input(nombre + "¿Cual es tu calificación en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print ('Felicidades' + nombre + ' Usted esta "APROBADO" con un promedio de ',promedio)

print ("Fin.")
    
