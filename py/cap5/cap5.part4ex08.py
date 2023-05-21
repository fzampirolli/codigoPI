"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

a = [int(i) for i in input().split(" ") if i]
b = [int(i) for i in input().split(" ") if i]
c = []
n = len(a)

for i in range(n):
    c.append(a[i] + b[i])

print(*c)
