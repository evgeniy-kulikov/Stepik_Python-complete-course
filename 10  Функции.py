# 10 Функции
""""""


"""   T A S K S   """


# Task 01
""" 
«Длина отрезка»
https://stepik.org/lesson/1055920/step/1?unit=1065229
Input:  0
        0
        1
        1
Output: 1.4142135623730951
"""
x1, y1, x2, y2 = (int(input())for _ in range(4))

def fanc(x1, y1, x2, y2):
    res = (pow(x2 - x1, 2) + pow(y2 - y1, 2))**0.5
    return res

print(fanc(x1, y1, x2, y2))


# Task 02
""" 
«Отрицательная степень»
https://stepik.org/lesson/1055920/step/2?unit=1065229
Дано действительное положительное число a и целоe число n. 
Вычислите a ** n. 
Решение оформите в виде функции power(a, n)
Input:  2
        -3
Output: 0.125
"""
# Ожидаемое решение
def power(a: float, n: int):
    res = 1
    for _ in range(abs(n)):
        res *= a
    if n == 0:
        return 1
    if n > 0:
        return float(res)
    return 1 / res

a, n = float(input()), int(input())
print(power(a, n))


# Короче
def power(a: float, n: int):
    res = a**n
    if n == 0:
        return res
    return float(res)

a, n = float(input()), int(input())
print(power(a, n))