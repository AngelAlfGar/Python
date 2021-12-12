print ("----Asignacion----")

mensaje = "Hola"
mensaje += " "
mensaje += "Angel"
print (mensaje) 

print ("----Concatenacion----")

mensaje = "Hola"
espacio = " "
nombre = "Angel"
print (mensaje + espacio + nombre)

print ("----Concatenacion String con Int----")

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str (resultado)
print ("El resultado de la suma es: " + resultado)

print ("----Busqueda----")

mensaje = "Hola Angel"
buscar_subCadena = mensaje.find("Angel")
print(buscar_subCadena)

print ("----Extraccion----")

mensaje = ( "Hola Angel" )
extraer_cadena = mensaje [1:8]
print (extraer_cadena)

print ("----Comparacion verdadera----")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print (mensaje_uno == mensaje_dos)

mensaje_uno = "Hola"
mensaje_dos = "Angel"
print (mensaje_uno != mensaje_dos)

print ("----Comparacion falsa----")

mensaje_uno = "Hola"
mensaje_dos = "Angel"
print (mensaje_uno == mensaje_dos)

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print (mensaje_uno != mensaje_dos)




