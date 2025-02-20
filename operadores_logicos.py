temperatura = int(input("Cuál es la temperatura afuera? "))

#El operador not cambia de falso a verdadero las condiciones
if not(temperatura >= 0 and temperatura <= 30):
    print("La temperatura esta mal hoy. Quedate adentro!")
elif not(temperatura < 0 or temperatura > 30):
    print("La temperatura esta bien hoy, Sal afuera!")