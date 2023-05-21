"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def repetidos(v):
    v2 = []
    v3 = []
    for i in v:
        if i not in v2:
            v2.append(i)  # lista sem números repetidos
        else:
            v3.append(i)  # lista dos repetidos
    return v2 + v3


vet = [int(i) for i in input().split(" ") if i]

print(*repetidos(vet))
