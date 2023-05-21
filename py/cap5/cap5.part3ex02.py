"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

v1 = [5, 23, 6, 3, -1, 6, 3, 6, 9]
m = 4
n = len(v1)
v2 = [0] * n
for i in range(n):
    min = v1[i]
    for j in range(-m, m + 1):
        vizinho = i + j
        if j and 0 <= vizinho < n and min > v1[vizinho]:
            min = v1[vizinho]
    v2[i] = min
print(*v1)
print(*v2)
