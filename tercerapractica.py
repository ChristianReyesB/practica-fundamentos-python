import random #importar libreria para aleatorios

#Instalar con comando:
#python -m pip install -U pip
#python -m pip install -U matplotlib
import matplotlib.pyplot as plt #Graficos

#Generar aleatorio
print(random.randint(1,20)) #inicio 1 - Fin 20
print(random.randint(20,25))
print(random.randrange(10,100, 2)) #Avanza en dos(Pares)

#Reacomodar una lista al azar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print('Lista original ', lista)

random.shuffle(lista)
print('Lista mezclada', lista)

#Genera grafico Gauss
campana = [random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()