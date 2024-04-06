"""
Nombre del archivo: proyecto2.py

Autores: Emanuel Antonio Marín Gutiérrez
         Gabriel Chacón Alfaro
         Jose Pablo Esquetini Fallas 

Descripcion: Pendiente

Nota: Para la realización de este proyecto se utilizaron las bibliotecas pandas v2.2.1 y matplotlib v3.8.3
      Si se ocupan instalar puede escribir: pip install pandas, matplotlib
"""

import matplotlib.pyplot as plt

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
def plot_funcion_masa_probabilidad(masa_probabilidad):
    valores = list(range(2, len(masa_probabilidad) + 2))
    
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

# Calcula la función masa de probabilidad y la grafica para los dados ideales
funcion_masa_probabilidad1 = suma_dados(dado_ideal1, dado_ideal2)
#print(funcion_masa_probabilidad1)
plot_funcion_masa_probabilidad(funcion_masa_probabilidad1)

# Calcula la función masa de probabilidad y la grafica para los dados trucados
funcion_masa_probabilidad2 = suma_dados(dado_truco1, dado_truco2)
#print(funcion_masa_probabilidad2)
plot_funcion_masa_probabilidad(funcion_masa_probabilidad2)
