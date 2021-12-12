print ("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")

matematicas = float(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = float(input(nombre + " ¿Cuál es tu calificación en química?: "))
fisica = float(input(nombre + " ¿Cuál es tu calificación en física?: "))

promedio = (matematicas + quimica + fisica) / 3

if promedio >= 6:
    print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,2))
else:
    print ('Lo sentimos ' + nombre + ' "reprobaste" con un promedio de: ', round(promedio,2))

print("Fin.")
