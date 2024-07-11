# 09 Списки
""""""


"""   T A S K S   """


# Task 01
""" 
«Четные индексы»
Выведите все элементы списка с четными индексами
Input:  1 2 3 4 5
Output: 1 3 5
"""
lst = input().split()
print(*lst[::2])

# Длинно
lst = input().split()
for i, el in enumerate(lst):
    if not i % 2:
        print(lst[i], end=' ')


# Task 02
""" 
«Четные элементы»
Выведите все четные элементы списка. Рекомендуется использовать цикл for
Input:  1 2 2 3 3 3 4
Output: 2 2 4
"""
lst = input().split()
for el in lst:
    if not int(el) % 2:
        print(el, end=' ')

# Короче
lst = input().split()
print(*filter(lambda x: not int(x) % 2, lst))


# Task 03
""" 
«Больше предыдущего»
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
Input:  1 5 2 4 3
Output: 5 4
"""
lst = [*map(int, input().split())]
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        print(lst[i], end=' ')


# Task 04
""" 
«Соседи одного знака»
Дан список чисел (нуля в нем нет). 
Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. 
Если таких пар соседей несколько — выведите первую пару.
Input:  -1 2 3 -1 -2
Output: 2 3
"""
lst = [*map(int, input().split())]
for i in range(1, len(lst)):
    if lst[i - 1] * lst[i] > 0:
        print(*lst[i - 1:i + 1])
        break


# Длинно
lst = input().split()
for i in range(1, len(lst)):
    if lst[i - 1].isdigit() and lst[i].isdigit():
        print(*lst[i - 1:i + 1])
        break
    elif lst[i - 1][0] == lst[i][0] == '-':
        print(*lst[i - 1:i + 1])
        break


# Task 05
""" 
«Больше своих соседей»
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, 
и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
Input:  1 2 3 4 5
Output: 0
"""
lst = [*map(int, input().split())]
cnt = 0

for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        cnt += 1
print(cnt)

# Короче
lst = list(map(int, input().split()))
print(sum(lst[i - 1] < lst[i] > lst[i + 1] for i in range(1, len(lst) - 1)))


# Task 06
""" 
«Наибольший элемент»
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. 
Если наибольших элементов несколько, выведите индекс первого из них.
Input:  1 2 3 2 1
Output: 3 2
"""
lst = [*map(int, input().split())]
max_num = max(lst)
print(max_num, lst.index(max_num))

# Длинно
lst = [*map(int, input().split())]
max_num = lst[0]
for el in lst[1:]:
    if el > max_num:
        max_num = el
print(max_num, lst.index(max_num))


# Task 07
""" 
«Шеренга»
Петя понадобилось определить своё место в строю. 
Программа получает на вход невозрастающую последовательность натуральных чисел, 
означающих рост каждого человека в строю. После этого вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200. 

Выведите номер, под которым Петя должен встать в строй. 
Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
Input:  165 163 160 160 157 157 155 154
        162
Output: 3
"""
lst = [*map(int, input().split())]
h = int(input())
for i, el in enumerate(lst, 1):
    if h > el:
        print(i)
        break


# Task 08
""" 
«Количество различных элементов»
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
Input:  1 2 2 3 3 3
Output: 3
"""
lst = [*map(int, input().split())]
print(len(set(lst)))


# Task 09
""" 
«Переставить соседние»
Переставьте соседние элементы списка. 
Если элементов нечетное число, то последний элемент остается на своем месте.
Input:  1 2 3 4 5
Output: 2 1 4 3 5
"""
# Ожидаемое решение
lst = [*map(int, input().split())]
for i in range(0, len(lst)-1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
print(*lst)

# Длинно
lst = [*map(int, input().split())]
res = []
for el in zip(lst[1::2], lst[::2]):
    res += el
if len(lst) % 2:
    res.append(lst[-1])
print(*res)

# Оригинальное решение
lst = list(map(int, input().split()))
lst[:-1:2], lst[1::2] = lst[1::2], lst[:-1:2]
print(*lst)


# Task 10
""" 
«Переставить min и max»
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
Input:  3 4 5 2 1
Output: 3 4 1 2 5
"""
# lst = [3, 4, 5, 2, 1]
lst = list(map(int, input().split()))

n_min, n_max = lst.index(min(lst)), lst.index(max(lst))
lst[n_min], lst[n_max] = lst[n_max], lst[n_min]
print(*lst)

# Не проходит второй тест
ls = sorted(lst.copy())
n_min, n_max = ls[0], ls[-1]
lst[lst.index(n_min)], lst[lst.index(n_max)] = n_max, n_min
print(*lst)


# Task 11
""" 
«Удалить элемент»
Дан список из чисел и индекс элемента в списке k. 
Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k. 
Программа получает на вход список, затем число k. 
Программа сдвигает все элементы, а после этого удаляет последний элемент списка 
при помощи метода pop() без параметров. 

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. 
Также нельзя использовать дополнительный список. 
не следует использовать метод pop(k) с параметром.
Input:  7 6 5 4 3 2 1
        2
Output: 7 6 4 3 2 1
"""
# lst = [7, 6, 5, 4, 3, 2, 1]

lst = list(map(int, input().split()))
k = int(input())

for i in range(k, len(lst) - 1):
    lst[i] = lst[i + 1]
print(*lst[:-1])

# Короче
lst[k:] = lst[k + 1:]
print(*lst)

del lst[k]
print(*lst)


# Task 12
""" 
«Вставить элемент»
Дан список целых чисел, число k и значение C. 
Необходимо вставить в список на позицию с индексом k элемент, равный C, 
сдвинув все элементы, имевшие индекс не менее k, вправо. 

Поскольку при этом количество элементов в списке увеличивается, 
после считывания списка в его конец нужно будет добавить новый элемент, используя метод append. 

Вставку необходимо осуществлять уже в считанном списке, 
не делая этого при выводе и не создавая дополнительного списка.
Input:  7 6 5 4 3 2 1
        2 0
Output: 7 6 0 5 4 3 2 1
"""
# lst = [7, 6, 5, 4, 3, 2, 1]

lst = list(map(int, input().split()))
k, c = int(input()), int(input())
# [*_], k, c = [[*map(int, input().split())] for _ in '12']
# *lst, k, c = list(map(int, open(0).read().split()))

lst.insert(k, c)
print(*lst)


# Task 13
""" 
«Количество совпадающих пар»
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Input:  1 2 3 2 3
Output: 2
"""
# lst = [1, 2, 3, 2, 3]  # 2
# lst = [0, 0, 6, 1, 1, 4, 2, 1, 2, 2]  # 7

lst = list(map(int, input().split()))
count = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            count += 1
print(count)


# Вариант Counter
from collections import Counter as c
# lst = list(map(int, input().split()))
res = sum(i * (i - 1) for i in c(lst).values()) // 2
print(res)


# Вариант permutations
from itertools import permutations as p
lst = list(map(int, input().split()))
res = len([i for i in p(lst, 2) if len(set(i)) == 1]) // 2
print(res)


# Task 14
""" 
«Кегельбан»
https://stepik.org/lesson/1055919/step/14?unit=1065228
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. 
Определите, какие кегли остались стоять на месте. 
Программа получает на вход количество кеглей N и количество бросков K.
Далее идет K пар чисел li, ri, при этом:  1<= li <= ri <= N
Вывести последовательность из N символов, где j-й символ есть I, если j-я кегля осталась стоять, 
или ., если j-я кегля была сбита.
Input:  10 3
        8 10
        2 5
        3 6
Output: I.....I...
"""
# n, k = 10, 3
# ls = [[8, 10], [2, 5], [3, 6]]
n, k, = list(map(int, input().split()))
ls = [list(map(int, input().split())) for _ in range(k)]
skittles = ['I'] * n

for el in ls:
    for i in range(el[0] - 1, el[1]):
        skittles[i] = '.'

print(''.join(skittles))


# Task 15
""" 
«Ферзи»
https://stepik.org/lesson/1055919/step/15?unit=1065228
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 

Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES
Input:  1 7
        2 4
        3 2
        4 8
        5 6
        6 1
        7 3
        8 5
Output: NO
"""
# ls = [[1, 7], [2, 4], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]
ls = [list(map(int, input().split())) for _ in range(8)]
flag = False

for k in ls:
    for i in ls[ls.index(k) + 1:]:
        if abs(k[0] - i[0]) == abs(k[1] - i[1]) or k[0] == i[0] or k[1] == i[1]:
            flag = True
            break
print(('NO', 'YES')[flag])


# Длинно
ls = [list(map(int, input().split())) for _ in range(8)]
flag = False

for k in range(len(ls) - 1):
    for i in range(k+1, len(ls)):
        if abs(ls[k][0] - ls[i][0]) == abs(ls[k][1] - ls[i][1]) \
                or ls[k][0] == ls[i][0] or ls[k][1] == ls[i][1]:
            flag = True
            break
print(('NO', 'YES')[flag])


# Task 16
""" 
«Циклический сдвиг вправо»
https://stepik.org/lesson/1055919/step/16?unit=1065228
Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1] на место A[2], ..., 
последний элемент переходит на место A[0]). 
Вводится список чисел. Все числа списка находятся на одной строке.
Input:  1 2 3 4 5
Output: 5 1 2 3 4
"""
# ls = [1, 2, 3, 4, 5]
ls = list(map(int, input().split()))
res = ls[-1:] + ls[:-1]
print(*res)

# Ожидаемое решение
ls = list(map(int, input().split()))
res = [ls[i % len(ls) - 1] for i in range(len(ls))]
print(*res)







