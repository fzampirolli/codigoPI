"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

v1 = [int(i) for i in input().split(" ") if i]
v2 = [int(i) for i in input().split(" ") if i]


def VECTOR_MULTIPLIER(v1, v2):
    v3 = 0
    for i in range(len(v1)):
        v3 += v1[i] * v2[i]
    return v3


print("{:.2f}".format(VECTOR_MULTIPLIER(v1, v2)))
