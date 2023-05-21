"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def delta(a, b, c):
    return b * b - 4 * a * c


# ENTRADA DE DADOS
print("Calcula as raízes de equação de 2º grau na forma ax^2 + bx + c")
a = float(input("Entre com o primeiro termo a: "))
b = float(input("Entre com o segundo  termo b: "))
c = float(input("Entre com o terceiro termo c: "))

# PROCESSAMENTO E SAÍDA
d = delta(a, b, c)
print("O delta é ", d)
if d < 0:
    print("A equação não possui raízes reais.")
if d == 0:
    print("A raíz é ", -b + d ** (1 / 2.0) / 2 * a)
if d > 0:
    print("Raízes:", -b - d ** (1 / 2.0) / 2 * a, ",", -b + d ** (1 / 2.0) / 2 * a)
