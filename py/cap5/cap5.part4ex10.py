"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""


def myorder(v):
    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[i] > v[j]:
                T = v[i]
                v[i] = v[j]
                v[j] = T
    return v


v = [int(i) for i in input().split(" ") if i]
n = len(v)
novo = int(input())

v = myorder(v)
print(*v)
aux = []
for i in v:
    # print(i,*aux)
    if i < novo:
        aux.append(i)
    elif i > novo:
        aux.append(novo)
    else:
        aux.append(i)

print(*aux)
