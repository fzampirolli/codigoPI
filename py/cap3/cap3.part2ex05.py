"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Author : Francisco de Assis Zampirolli
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


# DEFINIÇÕES DOS MÉTODOS
def leia():
    a = float(input("Digite a 1a nota: "))
    b = float(input("Digite a 2a nota: "))
    c = float(input("Digite a 3a nota: "))
    return a, b, c


# programa principal
# ENTRADA
nota1, nota2, nota3 = leia()

# PROCESSAMENTO E SAÍDA
media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10
print(media)
if media >= 9:
    print("Conceito A")
elif media >= 7.5:
    print("Conceito B")
elif media >= 6:
    print("Conceito C")
elif media >= 5:
    print("Conceito D")
else:
    print("Reprovado! Conceito F")
