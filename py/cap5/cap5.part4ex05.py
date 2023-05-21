"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

import string
import random

v = []
number_of_strings = 50
length_of_string = 2

nome = "".join(random.choice(string.ascii_letters) for _ in range(length_of_string))
print(nome.upper())

for x in range(number_of_strings):
    v.append(
        "".join(
            random.choice(string.ascii_letters) for _ in range(length_of_string)
        ).upper()
    )
# print(*v)


def buscaVetor(v, nome):
    for i in v:
        if nome == i:
            return "ACHEI"
    return "NÃO ACHEI"


buscaVetor(v, nome)
