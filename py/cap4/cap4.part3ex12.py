"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

a = int(input())
b = int(input())

while b != 0:
    temp = a
    a = b
    b = temp % b
print(a)
