import matplotlib.pyplot as plt
import numpy as np
import wx

def create_bar_chart():
    # Veri oluşturma
    x = np.arange(1, 6)
    y = np.random.randint(1, 10, size=(5,))
    colors = ['red', 'blue', 'green', 'yellow', 'orange']

    # Grafiği oluşturma
    fig, ax = plt.subplots()
    ax.bar(x, y, color=colors)
    ax.set_title('Sütun Grafiği')
    ax.set_xlabel('X Değerleri')
    ax.set_ylabel('Y Değerleri')

    # Grafiği döndürme
    return fig

def create_sqrt_chart():
    # Veri oluşturma
    x = np.arange(1, 11)
    y = np.sqrt(x)

    # Grafiği oluşturma
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title('Kök Grafiği')
    ax.set_xlabel('X Değerleri')
    ax.set_ylabel('Y Değerleri')

    # Grafiği döndürme
    return fig

def create_scatter_chart():
    # Veri oluşturma
    x = np.random.randn(100)
    y = np.random.randn(100)

    # Grafiği oluşturma
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title('Dağılım Grafiği')
    ax.set_xlabel('X Değerleri')
    ax.set_ylabel('Y Değerleri')

    # Grafiği döndürme
    return fig
