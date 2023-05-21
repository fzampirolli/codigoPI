"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import matplotlib.pyplot as plt
import numpy as np

import myBiblioteca as my

x = np.arange(-5, 0, 0.1)
a, b, c = 1, 5, 4
y1 = a * x * x + b * x + c
plt.plot(x, y1, "g")
plt.title("Meu gráfico")
plt.text(my.Raiz2(1, 5, 4), 0, "r1", bbox=dict(facecolor="red", alpha=0.4), fontsize=12)
plt.text(my.Raiz1(1, 5, 4), 0, "r2", bbox=dict(facecolor="red", alpha=0.4), fontsize=12)
plt.grid()
plt.savefig("meuGrafico.png")
