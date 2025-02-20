import time


#El primer argumento es de donde empezaremos a iterar, el segundo es hasta donde se va a iterar y el tercero seria como se va a ejecutar
for s in range(10, 0, -1):
    print(s)
    #Determina cuantos segundos vamos a esperear antes de la proxima iteracion
    time.sleep(1)
    
print("Feliz Año Nuevo")