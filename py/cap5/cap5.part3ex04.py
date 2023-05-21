"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

# v1[::-1] # não pode usar esse comando

print("Insira o vetor")
v = [int(i) for i in input().split(" ") if i]
n = len(v)

for i in range(n // 2):
    t = v[i]
    v[i] = v[n - 1 - i]
    v[n - 1 - i] = t

print(*v)
