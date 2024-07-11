# 06 Цикл for
""""""


"""   T A S K S   """

# Task 07
"""
«Факториал»
Факториалом числа n называется произведение 1*2*3 * ... *n. 
Обозначение: n!. 
По данному натуральному n вычислите значение n!. 
"""
f = 1
for el in range(1, int(input()) + 1):
    f *= el
print(f)

# рекурсия
def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)

print(fact(int(input())))


# библиотека  math
from math import factorial as f
print(f(int(input())))


# Task 08
"""
«Сумма факториалов»
По данному натуральном n вычислите сумму 1!+2!+…+n! 
Input:  4
Output: 24
"""
n = int(input())
def fact(el):
    f = 1
    for el in range(1, el + 1):
        f *= el
    return f

print(sum(fact(el) for el in range(1, n + 1)))

# Короче
n = int(input())
f, res = 1, 0
for el in range(1, n + 1):
    f *= el
    res += f
print(res)


# Task 09
"""
«Число сочетаний»
Input:  4
        2
Output: 6
"""
from math import factorial as f

n, k = int(input()), int(input())
res = f(n) / (f(k) * f(n - k))
print(int(res))


# рекурсия
def fact(x):
    return x * fact(x - 1) if x > 1 else 1


def func(n, k):
    return fact(n) // (fact(k) * fact(n - k))

print(func(*map(int, open(0))))



# Task 10
"""
«Количество нулей»
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. 
Подсчитайте количество чисел == 0 среди введенных чисел 
Input:  5
        0
        700
        0
        200
        2
Output: 2
"""
itr = (int(input())for _ in range(int(input())))
res = sum(not el for el in itr)
# res = sum(el == 0 for el in itr)
print(res)

# Короче
print(sum(int(input()) == 0 for _ in range(int(input()))))


# Task 11
"""
«Лесенка»
По данному натуральному n≤9 выведите лесенку из n ступенек, 
i-я ступенька состоит из чисел от 1 до i без пробелов.
Input:  3
Output: 1
        12
        123
"""
n = int(input())

for i in range(1, n + 1):
    for k in range(1, i + 1):
        print(k, end='')
    print()


# Вариант
n = int(input())
res = 0
for i in range(1, n + 1):
    res = res * 10 + i
    print(res)


# Task 12
"""
«Числа Фибоначчи»
f0=0, f1=1, f2=f1+f0 ... fn=fn-1 + fn-2
По данному натуральному числу N определите N-е число Фибоначчи Fn
Input:  6
Output: 8

"""
from functools import lru_cache

@lru_cache()
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))

# Короче
from functools import lru_cache
@lru_cache()
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))

# Просто
n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = a + b, a
print(a)


# Task 13
"""
«Остатки»
Даны целые неотрицательные числа a, b, c, d где   0 <= c < d
Определите количество чисел от a до b включительно, 
которые дают остаток  c  при делении на  d
"""
a, b, c, d = (int(input())for _ in range(4))

res = sum(el % d == c for el in range(a, b + 1))
print(res)


# Task 14
"""
«Диофантово уравнение»
https://stepik.org/lesson/1055721/step/14?unit=1065000
"""
a, b, c, d = (int(input())for _ in range(4))

for x in range(1000):
    res = a * x**3 + b * x**2 + c * x + d
    if res == 0:
        print(x)


# Task 15
"""
«Потерянная карточка»
https://stepik.org/lesson/1055721/step/15?unit=1065000
Для настольной игры используются карточки с номерами от 1 до N. 
Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек. 
"""
n = int(input())
ls = [int(input()) for _ in range(n - 1)]

for el in range(1, n + 1):
    if el not in ls:
        print(el)
        break

# Вариант
res = set(range(1, n + 1)) - set(ls)
print(*res)

# Вариант
n = int(input())
res = sum(range(1, n + 1))
for _ in range(1, n):
    res -= int(input())
print(res)



# Task 16
"""
«ГНЧЭ»
https://stepik.org/lesson/1055721/step/16?unit=1065000
Последовательность 1, 2, 2, 3, 3, 3, 4, 4, 4, 4 ....
Вводится число n. Вывести n чисел последовательности.
Input:  5
Output: 1 2 2 3 3
"""
n, k = int(input()), 0

while n:
    k += 1
    for _ in range(k):
        print(k, end=' ')
        n -= 1
        if not n:
            break


# Вариант
n = cnt = int(input())

for el in range(1, n + 1):
    if not cnt:
        break
    for i in range(el):
        print(el, end=' ')
        cnt -= 1
        if not cnt:
            break



