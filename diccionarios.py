capitales = {'EE.UU': 'Washington D.C.',
             'Argentina': 'Buenos Aires',
             'Chile': 'Santiago de Chile',
             'Brasil': 'Brasilia',
             'Cursos': ['Python', "C++"]
             }

#Para agregar un valor
#capitales.update({'Alemania': 'Berlin'})

#capitales.pop('EE.UU')

#capitales.clear()

#Sirve para buscar un elemento dentro de un diccionario
#print(capitales.get('Argentina'))

#Sirve para visualizar las llaves
#print(capitales.keys())

#Devuelve los valores que almacenas las llaves
#print(capitales.values())

#Para la informacion por completo
#print(capitales.items())


for key,value in capitales.items():
    print(key,value)