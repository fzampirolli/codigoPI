"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


n = int(input("Digite no número de posições: "))
v1 = [0] * n
v2 = [0] * n
for j in range(n):
    v1[j] = int(input())
for i in range(n):
    if i != 0 and i != n - 1:
        if v1[i - 1] <= v1[i] and v1[i - 1] <= v1[i + 1]:
            v2[i] = v1[i - 1]
        elif v1[i] <= v1[i - 1] and v1[i] <= v1[i + 1]:
            v2[i] = v1[i]
        else:
            v2[i] = v1[i + 1]
    else:
        if i == 0:
            if v1[i] <= v1[i + 1]:
                v2[i] = v1[i]
            else:
                v2[i] = v1[i + 1]
        if i == (n - 1):
            if v1[i] <= v1[i - 1]:
                v2[i] = v1[i]
            else:
                v2[i] = v1[i - 1]
print(*v1)
print(*v2)
