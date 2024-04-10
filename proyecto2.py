"""
Nombre del archivo: proyecto2.py

Autores: Emanuel Antonio Marín Gutiérrez
         Gabriel Chacón Alfaro
         Jose Pablo Esquetini Fallas 

Descripcion: Pendiente

Nota: Para la realización de este proyecto se utilizaron la biblioteca matplotlib v3.8.3
      Si se ocupan instalar puede escribir: pip install matplotlib
"""
import math
import matplotlib.pyplot as plt

"""
Nota: Remover despues esto si no es necesario
import numpy as np
from scipy.stats import nbinom

prob = nbinom.pmf(10, 3, funcion_masa_probabilidad1[5])
print(prob)
"""

# Definición de los dados ideales y trucados
dado_ideal1 = [1/6]*6
dado_ideal2 = [1/6]*6
dado_truco1 = [3/50, 3/50, 7/10, 3/50, 3/50, 3/50]
dado_truco2 = [3/50, 3/50, 3/50, 7/10, 3/50, 3/50]

# Color para los puntos en el gráfico
rgba_color = (0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 1.0)

# Función para calcular la suma de las probabilidades de dos dados
def suma_dados(dado1, dado2):
    suma_probabilidades = [0] * (len(dado1) + len(dado2) - 1)
    for i, p1 in enumerate(dado1):
        for j, p2 in enumerate(dado2):
            suma_probabilidades[i + j] += p1 * p2
    return suma_probabilidades

# Función para graficar la función masa de probabilidad
def plot_funcion_masa_probabilidad(masa_probabilidad, n):
    valores = list(range(n, len(masa_probabilidad) + n))
    
    bars = plt.bar(valores, masa_probabilidad, width=0.1)
    for bar in bars:
        height = bar.get_height()
        plt.plot(bar.get_x() + bar.get_width()/2., height, 'o', color=rgba_color, markersize=5)
        
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función masa de probabilidad (fmp)')
    plt.xticks(valores)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Función que calcula la combinacion nCr
def combinacion(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# Función que calcula la probabilidad para la distribución binomial negativa
# x es el número de ensayos totales hasta que se alcanzan r éxitos.
# r es el número de éxitos requeridos.
# p es la probabilidad de éxito en un solo ensayo.
def distribucion_binomial_negativa(x, r, p):
    return combinacion(x - 1, r - 1) * (1 - p)**(x - r) * p**r

# Función que construye la lista que conforma la fmp de acuerdo a la distribucion binomial negativa
def calculo_fmp(x, r, p):
    resultado = [0]*(x - r + 1)
    for i, num_ensayos in enumerate(range(r, x+1)):
        resultado[i] = distribucion_binomial_negativa(num_ensayos, r, p)
        
    return resultado

# Calcula la función masa de probabilidad y la grafica para los dados ideales
funcion_masa_probabilidad1 = suma_dados(dado_ideal1, dado_ideal2)
#print(funcion_masa_probabilidad1)
plot_funcion_masa_probabilidad(funcion_masa_probabilidad1, 2)

# Calcula la función masa de probabilidad y la grafica para los dados trucados
funcion_masa_probabilidad2 = suma_dados(dado_truco1, dado_truco2)
#print(funcion_masa_probabilidad2)
plot_funcion_masa_probabilidad(funcion_masa_probabilidad2, 2)

# Calcula la fmp según la distribución binomial negativa y la grafica para los dados ideales
fmp1 = calculo_fmp(10, 3, funcion_masa_probabilidad1[5])
#print(fmp1)
plot_funcion_masa_probabilidad(fmp1, 3)

# Calcula la fmp según la distribución binomial negativa y la grafica para los dados trucados
fmp2 = calculo_fmp(10, 3, funcion_masa_probabilidad2[5])
#print(fmp2)
plot_funcion_masa_probabilidad(fmp2, 3)
