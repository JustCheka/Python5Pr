""" Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a
"""

def f(a, b):
    if b == 1:
        return a
    return f(a, b - 1) * a

a = 3
b = 5
print(f(a, b))