"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def Delta(a, b, c):
    """
    Função para calcular o delta de uma equação de 2o. grau
    com coeficientes a, b e c
    """
    d = b * b - 4 * a * c
    return d


def Raiz1(a, b, c):
    """
    Função para calcular raiz1 de a, b e c
    """
    r1 = (-b + Delta(a, b, c) ** 0.5) / (2 * a)
    return r1


def Raiz2(a, b, c):
    """
    Função para calcular raiz1 de a, b e c
    """
    r2 = (-b - Delta(a, b, c) ** 0.5) / (2 * a)
    return r2
