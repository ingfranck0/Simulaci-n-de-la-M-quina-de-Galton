#importacion de librerias
import random
import matplotlib.pyplot as plt

#funcion de simulacion de canicas
def simular_canicas(num_canicas, num_niveles):
    contadores = [0] * (num_niveles+1)
    for i in range(num_canicas):
        contador = 0
        for j in range(num_niveles):
            if random.random() < 0.5:
                contador += 1
        contadores[contador] += 1
    return contadores

#funcion de graficar 
def graficar_histograma(contadores):
    plt.bar(range(len(contadores)), contadores)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de canicas')
    plt.title('Distribución de canicas en la máquina de Galton')
    plt.show()

num_canicas = 3000
num_niveles = 12
contadores = simular_canicas(num_canicas, num_niveles)
graficar_histograma(contadores)
