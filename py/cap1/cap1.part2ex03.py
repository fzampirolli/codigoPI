"""
Copyright(C) 2022 - 2023 Francisco de Assis Zampirolli - All Rights Reserved
Purpose : Examples and some exercises from the Information Processing book
Language : Python
"""

a = 2
b = 3
c = -5

delta = b**2 - 4 * a * c

print("delta =", delta)

raiz1 = (-b + (delta**0.5)) / (2 * a)
raiz2 = (-b - (delta**0.5)) / (2 * a)

print(f"raiz1 = {raiz1}\nraiz2 = {raiz2}")
