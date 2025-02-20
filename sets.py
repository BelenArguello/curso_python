#Los elementos de un set son unicos, no puede haber duplicados

utensilios = {"tenedor", "cuchara", "cuchillo"}
platos = {"plato", "bol", "taza", "cuchara"}

#Sirve para agregar un elemento al conjunto
#utensilios.add("cucharita")

#utensilios.remove("cuchara")

#Remueve elementos al azar
#utensilios.pop()

#utensilios.clear()

#Une dos conjuntos
#utensilios.update(platos)

#Remueve del primer conjunto un elemento parecido que tiene en común con el segundo conjunto
#print(utensilios.difference(platos))

#Devuelve el elemento repetido en ambos conjuntos
print(utensilios.intersection(platos))


#for x in utensilios:
 #   print(x)
    
