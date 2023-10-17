"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)
"""


def sum(a,b):
    if (b == 0):
        return a
    return sum(a, b - 1) + 1

a = 21
b = 18
print(sum(a, b))

