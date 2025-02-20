#Corte de cadenas
nombre = "Fatima Arguello"
primer_nombre = nombre[0:6]
apellido = nombre[7:15]

print(primer_nombre)
print(apellido)

#Dependiendo del tercer argumento va devolviendo caracteres de acuerdo al numero establecido
nombre2 = nombre[0:15:2]
print(nombre2)

#Revertir cadena 
nombre_invertido = nombre[::-1]
print(nombre_invertido)

#Creacion de objeto de corte
website = "http://www.google.com"
slice = slice(11,-4)

print(website[slice])