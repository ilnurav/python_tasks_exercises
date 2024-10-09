# a = 10
# b = 15.3
# c = 'hello'
# d = bool

# Структуры данных. Списки, множества и кортежи

# СПИСКИ----------------

# Primes = [2, 3, 5, 7, 11, 13]
# print(type(Primes))
# a = [12, 34.6, True, 'Hello']
# print(a[1], a[-1])

# Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# print(Rainbow[3:])
# print(Rainbow[0])
# Rainbow[0] = 'красный'
# print(Rainbow[0])
# print(Rainbow)
# print(len(Rainbow))
# print('Выведем радугу')
# for i in range(len(Rainbow)):
#     print(Rainbow[i], end=' ')
# for element in Rainbow:
#     print(element)
# print(Rainbow)
# print(*Rainbow)

# s = 'hello'
# s = list(s)
# print(s)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)
# print([7, 8] + [9])
# print([0] * 3)

# b = [] # b = list()
# b.append(1)
# b.append(2)
# b.append(3)
# print(b)

# b = []
# n = int(input('Введите количество элементов: '))
# for i in range(n):
#     b.append(int(input('Введите новый элемент: ')))
# print(b)

# s = '23 45  21   67     89'
# print(s.split())

# s = '23, 45, 21, 67, 89'
# print(s.split(', '))

# a = input().split()
# print(a)
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)
# a = [int(i) for i in input().split()]
# print(a)


# a = [0] * 5
# a = [0 for i in range(5)]
# a = []
# for i in range(5):
#     a.append(0)
# a = [i * i for i in range(5)]
# a = []
# for i in range(5):
#     a.append(i * i)
# from random import randrange
# n = 10
# a = [randrange(1, 10) for i in range(n)]
# print(a)

# a = [int(input('Введите новый элемент: ')) for i in range(int(input('Введите количество элементов: ')))]
# print(a)

# a = [12, 45, 67, 23, 9]
# print(12 in a)
# print(13 in a)
# print(15 not in a)

# a = ['red', 'green', 'blue']
# s = ' '.join(a)
# s = ''.join(a)
# s = ', '.join(a)
# print(type(s), s)
# print(s)

# a = [1, 2, 3]
# s = '***'.join([str(i) for i in a])
# print(s)

# a = [12, 64, 1, 23, 90, 6, 1]
# print(max(a), min(a))
# print(a.count(1))
# print(a)
# print(a.pop(3))
# print(a.pop())
# print(a)
# print(a.copy())
# a.insert(5, 30)
# print(a)
# print(a.index(1))
# a.remove(1)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.clear()
# print(a)

# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

# a = [23, 45, 67, 89, 0, -1, 3]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(i, a[i])

# Выведите все четные элементы списка. При этом используйте цикл for,
# перебирающий элементы списка, а не их индексы!

# a = [2, 3, 6, 7, 89, 90, 101]
# for i in a:
#     if i % 2 == 0:
#         print(i)

# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# a = [4, 2, 6, 5, 9, 15]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])

# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей
# несколько — выведите первую пару.

# a = [4, -2, 6, -5, -9, 15, 20]
# for i in range(1, len(a)):
#     if a[i] * a[i - 1] > 0:
#         print(a[i - 1], a[i])
#         break

# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих
# соседей,
# и выведите количество таких элементов. Крайние элементы списка никогда не учитываются,
# поскольку у них недостаточно соседей.

# a = [1, 3, 2, 6, 5, 7, 9, 8]
# k = 0
# for i in range(1, len(a) - 1):
#     if a[i - 1] < a[i] > a[i + 1]:
#         k += 1
# print(k)

# Дан список чисел. Выведите значение наибольшего элемента в списке,
# а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

# a = [1, 3, 2, 10, 6, 5, 7, 9, 8, 10]

# print(max(a), a.index(max(a)))
# #
# index_of_max = 0
# for i in range(1, len(a)):
#     if a[i] > a[index_of_max]:
#         index_of_max = i
# print(a[index_of_max], index_of_max)

# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
# Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю.
# После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети,
# то он должен встать после них.

# a = [190, 180, 175, 165, 160]
# x = 177
# pos = 0
# while pos < len(a) and a[pos] >= x:
#     pos += 1
# print(pos + 1)

# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

# a = [int(i) for i in input('Введите список чисел в одну строку через пробел: ').split()]
# k = 1
# for i in range(1, len(a)):
#     if a[i] != a[i - 1]:
#         k += 1
# print(k)

# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i], a[i - 1] = a[i - 1], a[i]
# print(*a)

# В списке все элементы различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.

# a = [int(i) for i in input().split()]
# a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
# print(*a)

# a = [int(i) for i in input().split()]
# index_max = 0
# index_min = 0
# for i in range(1, len(a)):
#     if a[i] > a[index_max]:
#         index_max = i
#     if a[i] < a[index_min]:
#         index_min = i
# a[index_max], a[index_min] = a[index_min], a[index_max]
# print(*a)

# Дан список из чисел и индекс элемента в списке k.
# Удалите из списка элемент с индексом k, сдвинув влево все элементы,
# стоящие правее элемента с индексом k.
#
# Программа получает на вход список, затем число k. Программа сдвигает все элементы,
# а после этого удаляет последний элемент списка при помощи метода pop() без параметров.
#
# Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при
# выводе элементов. Также нельзя использовать дополнительный список.
# Также не следует использовать метод pop(k) с параметром.

# 1 2 3 5 6 7
# k = 3

# a = [int(i) for i in input().split()]
# k = int(input())
# a.pop(k)
# # for i in range(k + 1, len(a)):
# #     a[i - 1] = a[i]
# # a.pop()
# print(*a)

# Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию
# с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
#
# Поскольку при этом количество элементов в списке увеличивается, после считывания списка
# в его конец нужно будет добавить новый элемент, используя метод append.
#
# Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и
# не создавая дополнительного списка.
# 1 2 3 10 4 5 6 7
# k = 3
# c = 10
# 1 2 3 10 4 5 6 7

# a = [int(i) for i in input().split()]
# k = int(input())
# c = int(input())
# # a.insert(k, c)
# a.append(0)
# for i in range(len(a) - 1, k, -1):
#     a[i] = a[i - 1]
# a[k] = c
# print(*a)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую
# необходимо посчитать.
# 1 2 3 1 4 3 5 2 6

# a = [int(i) for i in input().split()]
# k = 0
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             k += 1
# print(k)

# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# 1 2 3 1 4 3 5 2 6

# a = [int(s) for s in input().split()]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')

# дан список. Найти количество элементов, которые меньше 0.

# a = [int(s) for s in input().split()]
# k = 0
# for i in a:
#     if i < 0:
#         k += 1
# print(k)

# Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
# print([1] + [0] * 5 + [1])

# Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
# print([0, 1] * 5)

# Заполнить массив последовательными нечетными числами, начиная с единицы.
# a = []
# for i in range(1, 10, 2):
#     a.append(i)
# print(*a)

# Сформировать массив из элементов арифметической прогрессии с заданным первым элементом x и разностью d.
# 1 4 7 10 13 16 19
# 12 17 22 27 32 37

# a = []
# x = int(input('Первый элемент прогрессии: '))
# d = int(input('Разность: '))
# n = int(input('Количество элементов: '))
# k = 1
# while k <= n:
#     a.append(x)
#     x += d
#     k += 1
# print(a)

# Сформировать возрастающий массив из четных чисел.

# a = []
# x = int(input('Введите первое четное число: '))
# if x % 2 == 0:
#     n = int(input('Количество чисел: '))
#     k = 1
#     while k <= n:
#         a.append(x)
#         x += 2
#         k += 1
#     print(a)
# else:
#     print('Введите четное число!')

# # Сформировать убывающий массив из чисел, которые делятся на 3.
#
# a = []
# x = int(input('Введите число, которое делится на 3: '))
# if x % 3 == 0:
#     n = int(input('Количество чисел: '))
#     k = 1
#     while k <= n:
#         a.append(x)
#         x -= 3
#         k += 1
#     print(a)
# else:
#     print('Введите число, которое делится на 3!')

# # Заполнить массив заданной длины различными простыми числами.
# # Натуральное число, большее единицы, называется простым, если оно делится только на себя и на единицу.
#
# a = [2]
# n = int(input('Количество простых чисел: '))
# k = 2
# p = 3
# while k <= n:
#     for i in range(2, p):
#         if p % i == 0:
#             break
#     else:
#         a.append(p)
#         k += 1
#     p += 1
# print(a)

# # # Создать массив, каждый элемент которого равен квадрату своего номера.
# #
# n = int(input('Количество элементов массива: '))
# a = []
# for i in range(n):
#     a.append(i * i)
# print(a)

# # Создать массив, на четных местах в котором стоят единицы, а на нечетных местах - числа, равные остатку от деления своего номера на 5.
#
# n = int(input('Количество элементов массива: '))
# a = []
# for i in range(n):
#     if (i + 1) % 2 == 0:
#         a.append(1)
#     else:
#         a.append((i + 1) % 5)
# print(a)

# # Создать массив, который одинаково читается как слева направо, так и справа налево.
#
# # [1, 2, 3, 4, 3, 2, 1]
# # [1, 2, 3, 3, 2, 1]
#
# n = int(input('Количество элементов массива: '))
# a = []
# for i in range(1, n // 2 + 1):
#     a.append(i)
# if n % 2 == 0:
#     print(a + a[::-1])
# else:
#     print(a + [n // 2 + 1] + a[::-1])

# # Составить массив случайных чисел
#
# from random import randint
#
# a = []
# n = int(input('Количество элементов списка: '))
# for i in range(n):
#     a.append(randint(1, 100))
# print(a)

# # Найти количество чисел в массиве, которые делятся на 3, но не делятся на 7.
#
# from random import randint
#
# a = []
# n = int(input('Количество элементов списка: '))
# k = 0
# for i in range(n):
#     r = randint(1, 100)
#     a.append(r)
#     if r % 3 == 0 and r % 7 != 0:
#         k += 1
#         print(r, end=' ')
# if k != 0: print()
# print(k)
# print(a)

# # Найдите сумму и произведение элементов массива.
# from random import randint
# #
# a = []
# n = int(input('Количество элементов списка: '))
# s = 0
# p = 1
# for i in range(n):
#     r = randint(1, 10)
#     a.append(r)
#     s += r
#     p *= r
# print(a)
# print(s, p)

# # Найдите наименьший четный элемент массива.
#
# from random import randint
#
# a = []
# n = int(input('Количество элементов списка: '))
# for i in range(n):
#     a.append(randint(1, 100))
# print(a)
# min_a = a[0]
# for i in range(1, n):
#     if a[i] < min_a and a[i] % 2 == 0:
#         min_a = a[i]
# if min_a % 2 == 0:
#     print(min_a)
# else:
#     print('таких нет')

from random import randint
from math import inf

# a = []
# n = int(input('Количество элементов списка: '))
# min_a = inf
# for i in range(n):
#     a.append(randint(1, 100))
#     if a[i] < min_a and a[i] % 2 == 0:
#         min_a = a[i]
# print(a)
# if min_a != inf:
#     print(min_a)
# else:
#     print('таких нет')

# Кортежи

# Пустой кортеж
# empty_tuple = ()
# print(empty_tuple)
# print(type(empty_tuple))

# # Кортеж целых чисел
# first_tuple = (1, 2, 3, 4, 5, 3, 2, 1, 4)
# print(first_tuple)
# print(1 in first_tuple, 4 not in first_tuple)
#
# # Кортеж может содержать в себе данные
# # разных типов - любых, которые изучены выше
# second_tuple = (1, 2, 3.14, "Hello", True, 43, False, 'bla bla')
# print(second_tuple)
#
# # Кортеж может содержать в себе другие кортежи
# ndim_tuple = (12, 23, first_tuple, second_tuple)
# print(ndim_tuple)

# third_tuple = (1, )
# print(type(third_tuple))
#
# wrong_tuple = (1)
# print(type(wrong_tuple))

# first_list = [1, 3, 5]
# print('Дан список:', first_list)
# first_list[1] = 5
# print('Список после замены элемента:', first_list)

# print('Дан кортеж:', first_tuple)
# first_tuple[1] = 5
# print('Кортеж после замены элемента:', first_tuple)

# first_tuple = (1, 2, 3, 4, 5, 3, 2, 1, 4)
# print(len(first_tuple))
# for i in range(len(first_tuple)):
#     print(first_tuple[i], end=' ')

# for i in first_tuple:
#     print(i, end=' ')

# print(first_tuple.index(5))
# print(first_tuple[:7])
# print(first_tuple.count(3))

# print(list('hello'))
# print(tuple('hello'))

# a = []
# a.append(12)
# a.append(13)
# a.append(14)
# print(a)
# print(type(a))
# a = tuple(a)
# print(a)
# print(type(a))
# a = list(a)
# print(a)
# print(type(a))

# Множества

# A = {1, 2, 3, 2, 1, 2}
# print(A)
# print(type(A))
# A = set('qwerty')
# print(A)

# A = {1, 2, 3}
# B = {3, 2, 3, 1}
# print(A == B)
#
# c = set('Hello')
# print(c)

# primes = {2, 3, 5, 7, 11}
# # for num in primes:
# #     print(num)
# for i in primes:
#     print(i)

# A = {1, 2, 3}
# print(1 in A, 4 not in A)
# A.add(4)
# print(A)
# A.discard(4)
# print(A)
# A.remove(4)
# print(A)
# print(A.pop())

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6, 7}
# C = A | B
# C = A.union(B)
# print(C)
# A |= B
# A.update(B)
# print(A)
# C = A & B
# C = A.intersection(B)
# print(C)
# A &= B
# A.intersection_update(B)
# print(A)
# C = A - B
# C = A.difference(B)
# print(C)
# A -= B
# A.difference_update(B)
# C = A ^ B
# C = A.symmetric_difference(B)
# print(C)
# A ^= B
# A.symmetric_difference_update(B)
# print(A <= B) # A.issubset(B)
# print(A >= B) # A.issuperset(B)
# print(A > B)
# print(A < B)

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# from random import randint
#
# a = []
# for i in range(10):
#     a.append(randint(1, 10))
# print(a)
# print(set(a))
# print(len(set(a)))

# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6]
# a = set(a)
# b = set(b)
# print(a & b) # print(a.intersection(b))
# print(len(a & b))

# Даны два списка чисел. Найдите все числа, которые входят как в первый,
# так и во второй список и выведите их в порядке возрастания.

# a = [9, 4, 3, 7, 2, 0]
# b = [4, 2, 9, 5, 12]
# a = set(a)
# b = set(b)
# c = a & b
# print(c)
# print(*sorted(c))


# # # Во входной строке записана последовательность чисел через пробел.
# # # Для каждого числа выведите слово YES (в отдельной строке),
# # # если это число ранее встречалось в последовательности или NO, если не встречалось.
# #
# # # 1 2 3 1 1 4 2
# # # NO
# # # NO
# # # NO
# # # YES
# # # YES
# # # NO
# # # YES
#
# numbers = [int(i) for i in input().split()]
# a = set()
# for i in numbers:
#     if i in a:
#         print('YES')
#     else:
#         print('NO')
#         a.add(i)

# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор
# и в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались,
# сколько существуют цветов таких, что кубики каждого цвета присутствуют в
# обоих наборах. Для этого они занумеровали все цвета случайными числами от 0 до 10**8.
# На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
#
# В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори.
# В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.
#
# Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков,
# которые есть только у Ани и номера цветов кубиков, которые есть только у Бори. Для каждого из множеств
# выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.
# Вход:
# 4 3
# 0
# 1
# 10
# 9
# 1
# 3
# 0
# Выход:
# 2
# 0 1
# 2
# 9 10
# 1
# 3

# na, nb = [int(i) for i in input().split()]
# a, b = [], []
# for i in range(na):
#     a.append(int(input()))
# for i in range(nb):
#     b.append(int(input()))
# a, b = set(a), set(b)
# print(len(a & b))
# print(*sorted(a & b))
# print(len(a - b))
# print(*sorted(a - b))
# print(len(b - a))
# print(*sorted(b - a))

# # Дан текст: в первой строке записано число строк, далее идут сами строки.
# # Определите, сколько различных слов содержится в этом тексте.
# #
# # Словом считается последовательность непробельных символов идущих подряд,
# # слова разделены одним или большим числом пробелов или символами конца строки.
#
# # Вход:
# # 4
# # She sells sea shells on the sea shore;
# # The shells that she sells are sea shells I'm sure.
# # So if she sells sea shells on the sea shore,
# # I'm sure that the shells are sea shore shells.
#
# # Вывод:
# # 19

# n = int(input())
# set_a = set()
# for i in range(n):
#     list_a = input().split()
#     for word in list_a:
#         set_a.add(word)
# print(len(set_a))


# # # Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# # # Беатриса пытается угадать это число, для этого она называет некоторые множества
# # # натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел
# # # есть задуманное или NO в противном случае. После нескольких заданныъх вопросов
# # # Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и
# # # просит вас помочь ей определить, какие числа мог задумать Август.
# # #
# # # В первой строке задано n - максимальное число, которое мог загадать Август.
# # # Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных
# # # пробелом) и ответ Августа на этот вопрос.
# # #
# # # Вы должны вывести через пробел, в порядке возрастания, все числа, которые
# # # мог задумать Август.
# #
# # # Вход:
# # # 10
# # # 1 2 3 4 5
# # # YES
# # # 2 4 6 8 10
# # # NO
# # # HELP
# # # Выход:
# # # 1 3 5

# n = int(input())
# all_set = set(range(1, n + 1))
# while True:
#     sb = input()
#     if sb != 'HELP':
#         cur_set = set([int(i) for i in sb.split()])
#     else:
#         break
#     sa = input()
#     if sa == 'YES':
#         all_set &= cur_set # all_set = all_set & cur_set
#     else:
#         all_set -= cur_set # all_set = all_set - cur_set
# print(*sorted(all_set))

# Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков.
# Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.
#
# В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков,
# которое он знает, а затем - названия языков, по одному в строке.
#
# В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки -
# список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих строках -
# список таких языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.
# Вход:
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English
# Выход:
# 1
# English
# 3
# English
# Japanese
# Russian

# n = int(input())
# one_set = set()
# for i in range(n):
#     k = int(input())
#     all_set = set()
#     for j in range(k):
#         all_set.add(input())
#     one_set |= all_set
#     all_set &= all_set
# print(len(all_set))
# for i in sorted(all_set):
#     print(i)
# print(len(one_set))
# for i in sorted(one_set):
#     print(i)

# Август и Беатриса продолжают играть в игру, но Август начал жульничать. На каждый из вопросов Беатрисы
# он выбирает такой вариант ответа YES или NO, чтобы множество возможных задуманных чисел оставалось
# как можно больше. Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2,
# то Август ответит NO, а если Беатриса спросит про 1, 2, 3, то Август ответит YES.
#
# Если же Бетриса в своем вопросе перечисляет ровно половину из задуманных чисел, то Август из вредности
# всегда отвечает NO. Наконец, Август при ответе учитывает все предыдущие вопросы Беатрисы и свои ответы
# на них, то есть множество возможных задуманных чисел уменьшается.
#
# Первая строка содержит наибольшее число, которое мог загадать Август. Каждая следующая строка содержит
# очередной вопрос Беатрисы: набор чисел, разделенных пробелами. Последняя строка входных данных содержит
# одно слово HELP.
#
# Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос. После этого выведите через пробел,
# в порядке возрастания, все числа, которые мог загадать Август после ответа на все вопросы Беатрисы.
# Вход:
# 10
# 1 2 3 4 5
# 2 4 6 8 10
# HELP
# Выход:
# NO
# YES
# 6 8 10

# n = int(input())
# all_nums = set(range(1, n + 1))
# possible_nums = all_nums
# while True:
#     guess = input()
#     if guess == 'HELP':
#         break
#     guess = {int(x) for x in guess.split()}
#     if len(possible_nums & guess) > len(possible_nums) / 2:
#         print('YES')
#         possible_nums &= guess
#     else:
#         print('NO')
#         possible_nums &= all_nums - guess
#
# print(' '.join([str(x) for x in sorted(possible_nums)]))

# # Среди элементов с нечетными номерами найдите наибольший элемент массива, который делится на 3
#
# a = [2, 3, 5, 6, 7, 9, 10, 15]
# max_num = a[0]
# for i in range(1, len(a), 2):
#     if a[i] > max_num and a[i] % 3 == 0:
#         max_num = a[i]
# print(max_num)

# # Дан массив. Найдите два соседних элемента, сумма которых минимальна
#
# from random import randint
#
# a = [randint(1, 10) for i in range(10)]
# print(a)
# min_sum = a[0] + a[1]
# i1, i2 = 0, 1
# for i in range(1, len(a) - 1):
#     if a[i + 1] + a[i] < min_sum:
#         min_sum = a[i + 1] + a[i]
#         i1, i2 = i, i + 1
# print(a[i1], a[i2])

# # Дан массив. Найдите три последовательных элемента в массиве, сумма которых максимальна.
#
# from random import randint
#
# a = [randint(1, 10) for i in range(10)]
# print(a)
# max_sum = a[0] + a[1] + a[2]
# i1, i2, i3 = 0, 1, 2
# for i in range(2, len(a) - 1):
#     if a[i - 1] + a[i] + a[i + 1] > max_sum:
#         max_sum = a[i - 1] + a[i] + a[i + 1]
#         i1, i2, i3 = i - 1, i, i + 1
# print(a[i1], a[i2], a[i3])

# # Проверьте, образует ли элементы массива в данном порядке арифметическую или геометрическую прогрессии.
#
# # a = [2, 4, 6, 8, 10]
# # a = [15, 10, 5, 0, -5]
# # a = [2, 4, 8, 16, 32]
# # a = [64, 32, 16, 8, 4]
# a = [1, 3, 10, -5, 4]
# if a[1] - a[0] == a[2] - a[1]:
#     for i in range(2, len(a) - 1):
#         if a[i] - a[i - 1] != a[i + 1] - a[i]:
#             print('Прогрессии нет')
#             break
#     else:
#         print('Арифм. прогрессия')
# elif a[1] / a[0] == a[2] / a[1]:
#     for i in range(2, len(a) - 1):
#         if a[i] / a[i - 1] != a[i + 1] / a[i]:
#             print('Прогрессии нет')
#             break
#     else:
#         print('Геом. прогрессия')
# else:
#     print('Прогрессии нет')

# # Найти наиболее часто встречающийся элемент в массиве целых чисел.
#
# from random import randint
#
# a = [randint(1, 10) for i in range(10)]
# print(a)
# max_count = 0
# for i in a:
#     if a.count(i) > max_count:
#         max_count = a.count(i)
#         max_i = i
# print(max_i)

# # Проверьте, является ли данный массив возрастающим или убывающим.
#
# # a = [1, 3, 7, 10, 15, 20]
# # a = [100, 90, 75, 10, 5, 0]
# # a = [1, 5, 4, 2, 8]
# if a[1] > a[0]:
#     for i in range(1, len(a) - 1):
#         if a[i + 1] <= a[i]:
#             print('ни возр. ни убыв.')
#             break
#     else:
#         print('Возраст. посл-ть')
# elif a[1] < a[0]:
#     for i in range(1, len(a) - 1):
#         if a[i + 1] >= a[i]:
#             print('ни возр. ни убыв.')
#             break
#     else:
#         print('Убыв. посл-ть')
# else:
#     print('ни возр. ни убыв.')

# # Определите, есть ли в массиве повторяющиеся элементы.
#
# # a = [1, 2, 3, 4, 5]
# a = [1, 2, 3, 4, 5, 1]
# if len(a) == len(set(a)):
#     print('Повторов нет')
# else:
#     print('есть повторы')

# # Найдите минимальный по модулю элемент массива
#
# from random import randint
#
# a = [randint(-10, 10) for i in range(10)]
# print(a)
# min_num = abs(a[0])
# for i in range(1, len(a)):
#     if abs(a[i]) < min_num:
#         min_num = abs(a[i])
# print(min_num)

#  СЛОВАРИ!!!!!!

# capitals = dict()
# # print(type(capitals))
# capitals['Russia'] = 'Moscow'
# capitals['France'] = 'Paris'
# capitals['USA'] = 'Washington'
# print(capitals)
#
# countries = ['Russia', 'France', 'USA', 'Italy']
#
# for i in countries:
#     if i in capitals:
#         print('Столица страны ' + i + ': ' + capitals[i])
#     else:
#         print('В базе нет страны с названием ' + i)
#
# capitals = {'Russia': 'Moscow', 'USA': 'Washington', 'France': 'Paris'}
# print(capitals)
# print(capitals['USA'])
# print(capitals['Italy'])
# print(capitals.get('USA'))
# print(capitals.get('Italy'))
# print(capitals.get('Italy', 0))
# print(capitals.get('Italy', 'NO'))
# print('USA' in capitals)
# print('Italy' in capitals)

# del capitals['USA']
# print(capitals)
# del capitals['USA2']
# print(capitals)

# print(capitals.pop('USA'))
# print(capitals)
# print(capitals.pop('USA2', 'NO'))
# print(capitals)

# for key in capitals:
#     print(key, capitals[key])

# for key, val in capitals.items():
#     print(key, val)

# print(capitals.items())

# print(capitals.values())
#
# print(capitals.keys())

# # В единственной строке записан текст. Для каждого слова из данного текста подсчитайте,
# # сколько раз оно встречалось в этом тексте ранее.
# #
# # Словом считается последовательность непробельных символов идущих подряд, слова разделены
# # одним или большим числом пробелов или символами конца строки.
#
# # one two one tho three
# # 0 0 1 0 0
#
# d = {}
# line = input().split()
# for word in line:
#     d[word] = d.get(word, 0) + 1
#     print(d[word] - 1, end=' ')

# # Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом
# # к парному ему слову. Все слова в словаре различны.
# #
# # Для слова из словаря, записанного в последней строке, определите его синоним.
#
# # Вход:
# # 3
# # Hello Hi
# # Bye Goodbye
# # List Array
# # Goodbye
# # Выход:
# # Bye
#
# n = int(input())
# d = {}
# for i in range(n):
#     first, second = input().split()
#     d[first] = second
#     d[second] = first
# s = input()
# print(d[s])

# # Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования.
# # Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате.
# # Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов —
# # число выборщиков от этого штата. На практике, все выборщики от штата голосуют в соответствии с
# # результами голосования внутри штата, то есть на заключительной стадии выборов в голосовании
# # участвуют штаты, имеющие различное число голосов.
# #
# # В первой строке дано количество записей. Далее, каждая запись содержит фамилию кандидата и число
# # голосов, отданных за него в одном из штатов. Подведите итоги выборов: для каждого из участника
# # голосования определите число отданных за него голосов. Участников нужно выводить в алфавитном порядке.
#
# # Вход:
# # 5
# # McCain 10
# # McCain 5
# # Obama 9
# # Obama 8
# # McCain 1
# # Выход:
# # McCain 16
# # Obama 17
#
# n = int(input())
# num_votes = {}
# for i in range(n):
#     candidate, votes = input().split()
#     num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)
# a = sorted(num_votes.keys())
# for i in a:
#     print(i, num_votes[i])

# # Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово,
# # которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то,
# # которое меньше в лексикографическом порядке.
#
# # Вход:
# # 3
# # qем w e r t y u i o p
# # a s d f g h j kеме l
# # z x c v b n mме
# # Выход:
# # a
#
# n = int(input())
# d = {}
# for i in range(n):
#     line = input().split()
#     for word in line:
#         d[word] = d.get(word, 0) + 1
# max_count = max(d.values())
# a = sorted(d.keys())
# for key in a:
#     if d[key] == max_count:
#         print(key)
#         break

# # # # В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за
# # # # правами доступа к файлам.
# # # # Для каждого файла известно, с какими действиями можно к нему обращаться:
# # # #
# # # # запись W,
# # # # чтение R,
# # # # запуск X.
# # # # В первой строке содержится число N — количество файлов содержащихся в данной файловой системе.
# # # # В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные
# # # # пробелами.
# # # # Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида
# # # # Операция Файл. К одному и тому же файлу может быть применено любое колличество запросов.
# # # #
# # # # Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого
# # # # запроса должна будет возвращать OK если над файлом выполняется допустимая операция, или же
# # # # Access denied, если операция недопустима.
# # #
# # # # Вход:
# # # # 4
# # # # helloworld.exe R X
# # # # pinglog W R
# # # # nya R
# # # # goodluck X W R
# # # # 5
# # # # read nya
# # # # write helloworld.exe
# # # # execute nya
# # # # read pinglog
# # # # write pinglog
# # # # Выход:
# # # # OK
# # # # Access denied
# # # # Access denied
# # # # OK
# # # # OK
#
# n = int(input())
# d = {}
# for i in range(n):
#     line = input().split()
#     d[line[0]] = line[1:]
# n = int(input())
# for i in range(n):
#     action, file = input().split()
#     if action == 'read':
#         if 'R' in d[file]:
#             print('OK')
#         else:
#             print('Access denied')
#     elif action == 'write':
#         if 'W' in d[file]:
#             print('OK')
#         else:
#             print('Access denied')
#     elif action == 'execute':
#         if 'X' in d[file]:
#             print('OK')
#         else:
#             print('Access denied')

# # Дан текст: в первой строке записано количество строк в тексте, а затем сами строки.
# # Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# # Слова должны быть отсортированы по убыванию их количества появления в тексте,
# # а при одинаковой частоте появления — в лексикографическом порядке.
# #
# # Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать
# # его по частоте встречаемости слова. Желаемого можно добиться, если создать список,
# # элементами которого будут кортежи из двух элементов: частота встречаемости слова и
# # само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка
# # будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
# # а если они равны — то по второму. Это почти то, что требуется в задаче.
#
# # 9
# # hi
# # hi
# # what is your name
# # my name is bond
# # james bond
# # my name is damme
# # van damme
# # claude van damme
# # jean claude van damme
# #
# # damme
# # is
# # name
# # van
# # bond
# # claude
# # hi
# # my
# # james
# # jean
# # what
# # your
#
# n = int(input())
# d = {}
# for i in range(n):
#     line = input().split()
#     for word in line:
#         d[word] = d.get(word, 0) + 1
# a = []
# for key in d:
#     a.append((d[key], key))
# a.sort(key=lambda x: (-x[0], x[1]))
# for i in a:
#     print(i[1])

# # В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# # В случае с английским алфавитом очки распределяются так:
# # A, E, I, O, U, L, N, S, T, R – 1 очко;
# # D, G – 2 очка;
# # B, C, M, P – 3 очка;
# # F, H, V, W, Y – 4 очка;
# # K – 5 очков;
# # J, X – 8 очков;
# # Q, Z – 10 очков.
# # А русские буквы оцениваются так:
# # А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# # Д, К, Л, М, П, У – 2 очка;
# # Б, Г, Ё, Ь, Я – 3 очка;
# # Й, Ы – 4 очка;
# # Ж, З, Х, Ц, Ч – 5 очков;
# # Ш, Э, Ю – 8 очков;
# # Ф, Щ, Ъ – 10 очков.
#
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# # Будем считать, что на вход подается только одно слово, которое содержит либо
# # только английские, либо только русские буквы.
# #
# # Пример ввода:
# # ноутбук
# #
# # Пример вывода:
# # 12
#
# d = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2,
#      'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
#      'Q': 10, 'Z': 10, 'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2,
#      'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4,
#      'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
# word = input()
# s = 0
# for i in word:
#     s += d[i.upper()]
# print(s)

# # Данные об email-адресах студентов хранятся в словаре:
#
# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#       	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#       	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#       	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#       	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#       	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
#
# # Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен.
#
# email_list = []
# for domen in emails:
#     for email in emails[domen]:
#         email_list.append(email + '@' + domen)
# email_list.sort()
# for email in email_list:
#     print(email)

# Двумерные массивы ##############

# a = [[1, 2, 3],
#      [4, 5, 6]]
# print(a)
# print(a[0])
# print(a[1])
# print(a[0][2])
# print(a[1][1])
# b = a[0]
# print(b)
# a[0][1] = 7
# print(a)
# print(b)
# b[2] = 9
# print(a[0])
# print(b)

# a = [[1, 2, 3, 4],
#      [5, 6],
#      [7, 8, 9]]
# # print(len(a))
# # print(len(a[0]))
# # print(len(a[1]))
# # print(len(a[2]))
# print(a)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# a = [[1, 2, 3, 4],
#      [5, 6],
#      [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# a = [[1, 2, 3, 4],
#      [5, 6],
#      [7, 8, 9]]
# for row in a:
#     print(*row)

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s += a[i][j]
# print(s)

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for row in a:
#     for elem in row:
#         s += elem
# print(s)

# n = 3
# m = 4
# a = [[0] * m] * n
# print(a)
# a[0][0] = 5
# a[0][1] = 7
# print(a)

# n = 3
# m = 4
# a = [0] * n
# for i in range(n):
#     a[i] = [0] * m
# print(a)
# a[0][0] = 5
# print(a)

# n = 3
# m = 4
# a = []
# for i in range(n):
#     a.append([0] * m)
# print(a)
# a[0][0] = 5
# print(a)

# n = 3
# m = 4
# a = [[0] * m for _ in range(n)]
# print(a)
# a[0][0] = 5
# print(a)

# n = int(input())
# a = []
# for _ in range(n):
#     a.append([int(j) for j in input().split()])
# for row in a:
#     print(*row)

# n = int(input())
# a = []
# for _ in range(n):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)
# for row in a:
#     print(*row)

# n = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]
# for row in a:
#     print(*row)

# 1 2 3 4
# 5 6 7 8

# 1 2 3
# 4 5 6
# 7 8 9

# import random
#
# n = int(input())
# m = int(input())
# a = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(random.randint(1, 10))
#     a.append(row)
# for row in a:
#     print(*row)

# import random
#
# n, m = 3, 3
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(1, 10)
# for row in matrix:
#     print(*row)

# 1 2 3
# 4 5 6
# 7 8 9

# главная диагональ: 1 5 9
# побочная диагональ: 3 5 7

# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i > j:
#             a[i][j] = 2
#         elif i == j:
#             a[i][j] = 1
# for row in a:
#     print(*row)

# # # Найдите индексы первого вхождения максимального элемента. Выведите два числа:
# # # номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# # # Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
# # # а если номера строк равны то тот, у которого меньше номер столбца.
# # #
# # # Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
#
# n = int(input())
# m = int(input())
# a = [[int(j) for j in input().split()] for _ in range(n)]
# max_elem = a[0][0]
# i_max = 0
# j_max = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > max_elem:
#             max_elem = a[i][j]
#             i_max = i
#             j_max = j
# print(i_max, j_max)

# # # # Cоздать матрицу 3 x 4, в цикле заполнить ее числами 0 и 1 так, чтобы в одной строке
# # # # была ровно одна единица, и вывести на экран.
#
# matrix = [[0] * 4 for _ in range(3)]
# for row in matrix:
#     index_row = matrix.index(row)
#     row[index_row] = 1
# for row in matrix:
#     print(*row)

# Создать и вывести на экран матрицу 2 x 3, заполненную случайными числами из [0, 9].

# import random
#
# n, m = 2, 3
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(0, 9)
# for row in matrix:
#     print(*row)

# Дана матрица. Вывести на экран первый и последний столбцы.

# import random
#
# n, m = 3, 3
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(0, 9)
# for row in matrix:
#     print(*row)
# print()
# for row in matrix:
#     print(row[0], row[-1])

# # Дана матрица. Вывести на экран первую и последнюю строки.
#
# import random
#
# n, m = 3, 3
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(0, 9)
# for row in matrix:
#     print(*row)
# print()
# print(*matrix[0])
# print(*matrix[-1])

# # Дана матрица. Вывести на экран все четные строки, то есть с четными номерами.
#
# import random
#
# n, m = 4, 4
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(0, 9)
# for row in matrix:
#     print(*row)
# print()
# for i in range(n):
#     if i % 2 == 0:
#         print(*matrix[i])

# # # Дана матрица. Вывести на экран все нечетные столбцы, у которых первый элемент
# # # больше последнего.

# import random
#
# n, m = 4, 6
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(0, 9)
# for row in matrix:
#     print(*row)
# print()
# for j in range(1, m, 2):
#     if matrix[0][j] > matrix[n - 1][j]:
#         for i in range(n):
#             print(matrix[i][j], end=' ')
#         print()

# # Дан двухмерный массив 5×5. Найти сумму модулей отрицательных нечетных элементов.
#
# import random
#
# n, m = 5, 5
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(-9, 9)
# for row in matrix:
#     print(*row)
# print()
# s = 0
# for row in matrix:
#     for elem in row:
#         if elem % 2 != 0 and elem < 0:
#             s += abs(elem)
# print(s)

# # # # Дан двухмерный массив n×m элементов.
# # # # Определить, сколько раз встречается число 7 среди элементов массива.
#
# import random
#
# n, m = 5, 5
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(1, 9)
# for row in matrix:
#     print(*row)
# print()
# count_7 = 0
# for row in matrix:
#     for elem in row:
#         if elem == 7:
#             count_7 += 1
# print(count_7)

# # Дана квадратная матрица. Вывести на экран элементы, стоящие на главной и побочной диагоналях.
#
# import random
#
# n, m = 5, 5
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(1, 9)
# for row in matrix:
#     print(*row)
# print()
# glav = []
# poboch = []
# for i in range(n):
#     for j in range(m):
#         if i == j:
#             glav.append(matrix[i][j])
#         if i + j == n - 1:
#             poboch.append((matrix[i][j]))
# print(*glav)
# print(*poboch)

# # # Дана матрица. Вывести k-ю строку и p-й столбец матрицы.
#
# import random
#
# n, m = 5, 5
# k, p = 2, 3
# matrix = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = random.randint(1, 9)
# for row in matrix:
#     print(*row)
# print()
# print(*matrix[k])
# for i in range(n):
#     print(matrix[i][p], end=' ')

# # # # Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его
# # # # символами "." (каждый элемент массива является строкой из одного символа).
# # # # Затем заполните символами "*" среднюю строку массива, средний столбец массива,
# # # # главную диагональ и побочную диагональ. В результате единицы в массиве должны
# # # # образовывать изображение звездочки. Выведите полученный массив на экран, разделяя
# # # # элементы массива пробелами.
# # #
# # # n = 5
# # # * . * . *
# # # . * * * .
# # # * * * * *
# # # . * * * .
# # # * . * . *
#
# n = int(input('Введите нечетное число: '))
# a = []
# for _ in range(n):
#     a.append(['.'] * n)
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1 or i == n // 2 or j == n // 2:
#             a[i][j] = '*'
#         print(a[i][j], end=' ')
#     print()

# # # Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его
# # # символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
# #
# # # . * . *
# # # * . * .
# # # . * . *
#
# n = int(input())
# m = int(input())
# a = []
# for _ in range(n):
#     a.append(['.'] * m)
# for i in range(n):
#     for j in range(m):
#         if (i + j) % 2 != 0:
#             a[i][j] = '*'
#         print(a[i][j], end=' ')
#     print()

# # Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
# # На главной диагонали должны быть записаны числа 0. На двух диагоналях,
# # прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
#
# # 0 1 2 3 4
# # 1 0 1 2 3
# # 2 1 0 1 2
# # 3 2 1 0 1
# # 4 3 2 1 0
#
# n = int(input())
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         a[i][j] = abs(i - j)
#         print(a[i][j], end=' ')
#     print()

# # Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# # Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# # Числа, стоящие выше этой диагонали, равны 0.
# # Числа, стоящие ниже этой диагонали, равны 2.
# # Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
#
# # 0 0 0 1
# # 0 0 1 2
# # 0 1 2 2
# # 1 2 2 2
#
# n = int(input())
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i + j == n - 1: a[i][j] = 1
#         if i + j > n - 1: a[i][j] = 2
#         print(a[i][j], end=' ')
#     print()

# Функции

# n! = 1 ⋅ 2 ⋅ ... ⋅ n
# 5! = 1 ⋅ 2 ⋅ 3 ⋅ 4 ⋅ 5 = 120

# # вычислим 3!
# res = 1
# for i in range(1, 4):
#     res *= i
# print(res)
#
# # вычислим 5!
# res = 1
# for i in range(1, 6):
#     res *= i
# print(res)

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# factorial(3)
# print(factorial(5))

# import math
#
# print(math.sqrt(9))

# def my_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# print(my_max(3, 5))
# print(my_max(5, 3))
# print(my_max(int(input()), int(input())))

# def my_max3(a, b, c):
#     if c < a > b:
#         return a
#     elif a < b > c:
#         return b
#     else:
#         return c
#
# print(my_max3(3, 5, 7))
# print(my_max3(5, 3, 1))

# def my_max(*a):
#     res = a[0]
#     for val in a[1:]:
#         if val > res:
#             res = val
#     return res
#
# print(my_max(3, 5, 42, 10))

# def print_hello():
#     print('hello')
#
# print_hello()
# print_hello()
# print_hello()

# def print_hello(message):
#     print(message)
#
# print_hello('hello')
# print_hello(15)
# print_hello('good')

# def kvadr(a, b, c):
#     d = b * b - 4 * a * c
#     if d > 0:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         print('x1 =', x1, 'x2 =', x2)
#     elif d == 0:
#         print('x =', -b / (2 * a))
#     else:
#         print('действ. корней нет')
#
# kvadr(1, 2, 1)
# kvadr(4, 5, 1)
# kvadr(10, 5, 1)

# def kvadr(a, b, c):
#     d = b * b - 4 * a * c
#     if d > 0:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         return 'x1 = ' + str(x1) + ' x2 = ' + str(x2)
#     elif d == 0:
#         return 'x = ' + str(-b / (2 * a))
#     else:
#          return 'действ. корней нет'
#
# print(kvadr(1, 2, 1))
# print(kvadr(4, 5, 1))
# print(kvadr(10, 5, 1))

# # # # Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# # # # вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа
# # # # и выведите результат работы этой функции.
# #
#
# def distance(x1, y1, x2, y2):
#     a = abs(x2 - x1)
#     b = abs(y2 - y1)
#     c = (a * a + b * b) ** 0.5
#     return c
#
# print(distance(0, 0, 3, 4))
# print(distance(-1, -2, 10, 5))

# # # Дано действительное положительное число a и целоe число n.
# # # Вычислите a**n. Решение оформите в виде функции power(a, n).
# # # Стандартной функцией возведения в степень пользоваться нельзя.
#
# def power(a, n):
#     p = 1
#     for i in range(n):
#         p *= a
#     return p
#
# print(power(2, 5))
# print(power(3, 4))

# # Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и
# # возвращает его же, меняя первую букву на большую.
# # Например, print(capitalize('word')) должно печатать слово Word.
# #
# # На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят
# # из маленьких латинских букв. Напечатайте исходную строку, сделав так, чтобы каждое
# # слово начиналось с большой буквы. При этом используйте вашу функцию capitalize().
# #
# # Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в
# # таблице ASCII, и функция chr(), которая по коду символа возвращает сам символ.
# # Например, ord('a') == 97, chr(97) == 'a'.

# def capitalize(word):
#     return word[0].upper() + word[1:]
#
# s = input()
# s = s.split()
# for i in range(len(s)):
#     s[i] = capitalize(s[i])
# print(' '.join(s))

# print(ord('a'))
# print(ord('A'))
# print(ord('z'))
# print(ord('Z'))

# print(ord('а'))
# print(ord('А'))
# print(ord('я'))
# print(ord('Я'))

# print(chr(ord('a') - 32))

# def capitalize(word):
#     return chr(ord(word[0]) - 32) + word[1:]
#
# s = input()
# s = s.split()
# for i in range(len(s)):
#     s[i] = capitalize(s[i])
# print(' '.join(s))

# # Написать функцию, которая возвращает среднее арифметическое двух переданных ей аргументов
# # (параметров).

# def average(a, b):
#     s = (a + b) / 2
#     return s
#
# print(average(2, 3))
# print(average(10, 20))

# # Написать функцию, которая возвращает среднее арифметическое нескольких переданных ей аргументов
# # (параметров).

# a = [1, 2, 3, 4]
# print(sum(a))
#
# a = (1, 2, 3, 4, 5)
# print(sum(a), len(a))

# def average(*a):
#     return sum(a) / len(a)
#
# print(average(1, 2, 3, 4, 10))

# # Напишите функцию, находящую наименьшее из четырех данных чисел.
#
# def min4(a, b, c, d):
#     if b >= a <= c and a <= d:
#         return a
#     elif a >= b <= c and b <= d:
#         return b
#     elif a >= c <= b and c <= d:
#         return c
#     else:
#         return d
#
# print(min4(1, 2, 3, 4))
# print(min4(2, 1, 3, 4))
# print(min4(3, 2, 1, 4))
# print(min4(4, 2, 3, 1))
# print(min4(1, 2, 3, 1))

# # # Напишите "функцию голосования", возвращающую то значение (true или false),
# # # которое среди значений ее аргументов x, y, z встречается чаще.
#
# def golos(x, y, z):
#     a = [x, y, z]
#     if a.count(True) > a.count(False):
#         return True
#     else:
#         return False
#
# print(golos(True, False, False))
# print(golos(True, False, True))
# print(golos(True, True, False))

# Функция, которая проверят число на простоту

# def prime(x):
#     for i in range(2, x // 2 + 1):
#         if x % i == 0:
#             return False
#     else:
#         return True

# def prime(x):
#     for i in range(2, round(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     else:
#         return True
#
# print(prime(7))
# print(prime(10))
# print(prime(101))
# print(prime(10000000121))

# # Назовем автобусный билет несчастливым, если сумма цифр его шестизначного номера делится на 13.
# # # Функция, которая определяет является ли билет несчастливым
#
# def bilet(x):
#     s = 0
#     while x > 0:
#         s += x % 10
#         x //= 10
#     if s % 13 == 0:
#         return True
#     else:
#         return False
#
# print(bilet(123456))
# print(bilet(623456))

# # Два числа называются дружественными, если каждое из них равно сумме всех делителей второго
# # не считая самого этого числа. Функция, которая определяет дружественность чисел
#
# # 220 и 284

# s = 0
# for i in range(1, 220):
#     if 220 % i == 0:
#         print(i, end=' ')
#         s += i
# print(s)
# s = 0
# for i in range(1, 284):
#     if 284 % i == 0:
#         print(i, end=' ')
#         s += i
# print(s)

# def drug(a, b):
#     sa = 0
#     sb = 0
#     s = max(a, b)
#     for i in range(1, s // 2 + 1):
#         if a % i == 0:
#             sa += i
#         if b % i == 0:
#             sb += i
#     if sa == b and sb == a:
#         return True
#     else:
#         return False
#
# a = [1, 2, 3]
# print(sum(a))
# a = {1, 2, 3}
# print(sum(a))

# def drug(a, b):
#     sa = [1]
#     sb = [1]
#     s = max(a, b)
#     for i in range(2, round(s ** 0.5) + 1):
#         if a % i == 0:
#             sa.append(i)
#             sa.append(a / i)
#         if b % i == 0:
#             sb.append(i)
#             sb.append(b / i)
#     if sum(set(sa)) == b and sum(set(sb)) == a:
#         return True
#     else:
#         return False
#
# print(drug(220, 284))
# print(drug(220, 240))

# # # функция, которая переводит число из десятичного вида в систему счисления
# # с основанием n (1 < n < 10):
#
# # 4 = 100
# # 6 = 110
#
# # def syst(x, n):
# #     s = ''
# #     while x > 0:
# #         s += str(x % n)
# #         x //= n
# #     return s[::-1]
# #
# # print(syst(4, 2))
# # print(bin(4))
# # print(syst(6, 2))
# # print(syst(40, 7))
# # print(syst(7, 3))
#
# # # функция, которая переводит число из n-го вида в систему счисления с основанием 10
#
# # print(int('55', 7))
# # print(int('21', 3))
# # print(int('AB12C', 16)) # 700716
#
# def syst(x, n):
#     s = ''
#     while x > 0:
#         if x % n == 10:
#             s += 'A'
#         elif x % n == 11:
#             s += 'B'
#         elif x % n == 12:
#             s += 'C'
#         elif x % n == 13:
#             s += 'D'
#         elif x % n == 14:
#             s += 'E'
#         elif x % n == 15:
#             s += 'F'
#         else:
#             s += str(x % n)
#         x //= n
#     return s[::-1]
#
# print(syst(700716, 16)) # AB12C

# # # Напишите функцию, которая подсчитывает количество гласных русских букв в строке.
# # # а, я, у, ю, о, е, ё, э, и, ы
#
# def count_a(s):
#     count = 0
#     for i in s:
#         if i.lower() in ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']:
#             count += 1
#     return count
#
# print(count_a(input()))

# # # Напишите функцию, которая проверяет, является ли строка палиндромом
# # (читается одинаково справа налево и слева направо).
#
# def palindrom(s):
#     if s.lower() == s[::-1].lower():
#         return True
#     else:
#         return False
#
# print(palindrom('Алла'))
# print(palindrom('дед'))
# print(palindrom('мама'))

# # Напишите функцию, которая определяет, является ли строка анаграммой другой строки
# (содержит те же буквы, но в другом порядке).
#
# # иностранка - санаторник
# # пенсионерка - покраснение

# def anagram(s1, s2):
#     if len(s1) == len(s2) and set(s1) == set(s2):
#         return True
#     else:
#         return False
#
# print(anagram('пенсионерка', 'покраснение'))
# print(anagram('пенсионерка', 'погода'))

# # Напишите функцию, которая принимает число и возвращает его факториал
#
# # 5! = 1 * 2 * 3 * 4 * 5 = 125
# # 4! = 1 * 2 * 3 * 4 = 24
#
# def factorial(x):
#     p = 1
#     for i in range(1, x + 1):
#         p *= i
#     return p
#
# print(factorial(4))
# print(factorial(5))

# # # Напишите функцию, которая принимает два списка и возвращает список, содержащий
# # только уникальные элементы из обоих списков.
# #
#
# def unik(a, b):
#     c = []
#     for i in a:
#         if a.count(i) == 1:
#             c.append(i)
#     for i in b:
#         if b.count(i) == 1:
#             c.append(i)
#     return c
#
# print(unik([1, 2, 2, 3, 4, 4], [5, 6, 6, 7, 7, 8]))

# # Напишите функцию, которая принимает два аргумента (строку и символ) и возвращает число,
# # сколько раз символ встречается в строке.
#
# def povtor(s, a):
#     return s.lower().count(a.lower())
#
# print(povtor('мама мыла рАму', 'а'))


# def f():
#     print(a)
#
# a = 1
# f()

# def f():
#     a = 1
#
# f()
# print(a)

# def f():
#     a = 1
#     print(a)
#
# a = 0
# f()
# print(a)

# def f():
#     global a
#     a = 1
#     print(a)
#
# a = 0
# f()
# print(a)

# def hello():
#     return 'hello'

# print(hello())

# def say_hello(message):
#     print(message)

# say_hello('hello')

# say_hello(hello())

# def hello():
#     return 'hello'
#
# def say_hello():
#     print(hello())
#
# say_hello()

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(3))

# def qvadr(x):
#     return x * x
#
# print(qvadr(3))

# def proiz(x, y):
#     return x * y
#
# print(proiz(2, 3))

# qvadr = lambda x: x * x
#
# print(qvadr(5))

# proiz = lambda x, y: x * y
# print(proiz(2, 3))

# def tr():
#     return True
#
# print(tr())
#
# tr = lambda: True
# print(tr())

# Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число
# Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.

# 1 1 2 3 5 8 13 21 ...

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(8))

# # Напишите рекурсивную функцию для вычисления суммы цифр числа n.
#
# def sum_of_digits(n):
#     if n <= 9:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
# print(sum_of_digits(123))

# # Напишите рекурсивную функцию для возведения числа x в степень y.
#
# def power(x, y):
#     if y == 1:
#         return x
#     else:
#         return x * power(x, y - 1)
#
# print(power(2, 3))

# # Напишите рекурсивную функцию для определения количества разрядов числа n.
#
# def count_digits(n):
#     if n <= 9:
#         return 1
#     else:
#         return 1 + count_digits(n // 10)
#
# print(count_digits(12345))

# # Напишите рекурсивную функцию для вычисления суммы чисел от 1 до n.
#
# def sum_n(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_n(n - 1)
#
# print(sum_n(5))

# # Проверьте, является ли число n числом Армстронга (сумма цифр числа в степени,
# # равной количеству цифр, равна самому числу).

# 153 = 1 ** 3 + 5 ** 3 + 3 ** 3

# def armstrong(n):
#     count = len(str(n))
#     s = 0
#     for i in str(n):
#         s += int(i) ** count
#     return n == s
#
# # print(armstrong(153))
# # print(armstrong(155))
# for i in range(1, 101):
#     if armstrong(i):
#         print(i)

# # # Переведите градусы по шкале Цельсия в градусы по шкале Фаренгейта и наоборот
#
# # def c_to_f(c):
# #     return c * 9 / 5 + 32
# #
# # def f_to_c(f):
# #     return (f - 32) * 5 / 9
#
# c_to_f = lambda c: c * 9 / 5 + 32
# f_to_c = lambda f: (f - 32) * 5 / 9
#
# print(c_to_f(25))
# print(f_to_c(77))

# # Проверьте, является ли строка панграммой (содержит все буквы алфавита)
#
# # print(ord('a')) # 97
# # print(ord('z')) # 122
# # a = set()
# # for i in range(97, 123):
# #     a.add(chr(i))
# # # print(a)
# # a = list(a)
# # a.sort()
# # print(*a)
# # print(len(a))
#
# def pangramma(s):
#     a = set()
#     for i in range(97, 123):
#         a.add(chr(i))
#     s_set = set()
#     for i in s:
#         if 'a' <= i.lower() <= 'z':
#             s_set.add(i.lower())
#     return a == s_set
#
# print(pangramma('The quick brown fox jumps over the lazy dog'))
# print(pangramma('The quick brown fox jumps over the lazy do'))

# # Проверьте, является ли число палиндромом в двоичной системе.
#
# # 1001 1100011
#
# # print(bin(10), bin(10)[2:])
# # print(bin(20))
#
# def palindrom_bin(x):
#     x = bin(x)[2:]
#     return x == x[::-1]
#
# for i in range(1, 101):
#     if palindrom_bin(i):
#         print(bin(i)[2:])

# # Вывести на экран числа от 1000 до 9999 такие, что все цифры различны
#
# def f(a, b):
#     s = []
#     for i in range(a, b + 1):
#         if len(str(i)) == len(set(str(i))):
#             s.append(i)
#     return s
#
# for i in f(1000, 9999):
#     print(i)

# # Вывести на экран числа от 1000 до 9999 такие, что среди цифр нет
# # цифр 5 и цифры 6.
#
# # print('5' in '12345')
# # print('5' not in '1234')
#
# def f(a, b):
#     s = []
#     for i in range(a, b + 1):
#         if '5' not in str(i) and '6' not in str(i):
#             s.append(i)
#     return s
#
# for i in f(1000, 9999):
#     print(i)

# # Вывести все пятизначные числа, которые делятся на 2, у которых средняя
# # цифра нечетная, и сумма всех цифр делится на 4.
#
# def f(a, b):
#     s = []
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             if int(str(i)[2]) % 2 != 0:
#                 if sum([int(j) for j in str(i)]) % 4 == 0:
#                     s.append(i)
#     return s
#
# for i in f(10000, 100000):
#     print(i)

# # Вывести на экран числа от 1000 до 9999 такие, что среди цифр есть цифра 3.
#
# def f(a, b):
#     s = []
#     for i in range(a, b + 1):
#         if '3' in str(i):
#             s.append(i)
#     return s
#
# for i in f(1000, 9999):
#     print(i)

# # Найдите трехзначные числа, равные сумме кубов своих цифр
#
# def f(a, b):
#     s = []
#     for i in range(a, b + 1):
#         if i == sum([int(j) ** 3 for j in str(i)]):
#             s.append(i)
#     return s
#
# for i in f(100, 999):
#     print(i)

# # # Сколько существует четырехзначных чисел, которые в 600 раз больше
# # суммы своих цифр?
#
# def f(a, b):
#     s = []
#     for i in range(a, b + 1):
#         if i == 600 * sum([int(j) for j in str(i)]):
#             s.append(i)
#     return s
#
# for i in f(1000, 9999):
#     print(i)

# # # Найдите хотя одно натуральное число, которое делится на 11,
# # # а при делении на 2, 3, 4, ..., 10 дает в остатке 1
#
# def f():
#     i = 11
#     while True:
#         for j in range(2, 11):
#             if i % j != 1:
#                 break
#         else:
#             print(i)
#             break
#         i += 11
#
# f()

# # # Вывести ряд чисел: десять десяток, девять девяток, восемь восьмерок, ... ,
# # одну единицу.
# # # Найти сумму всех этих чисел.
#
# def f():
#     s = 0
#     for i in range(10, 0, -1):
#         a = [i] * i
#         # print(*a)
#         print(*a, end=' ')
#         s += sum(a)
#     print()
#     print(s)
#
# f()

# # # Выведите  на экран строки (в последней строке n звездочек):
# # *
# # **
# # ***
# # ****
# # *****
#
# def f(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print('*', end='')
#         print()
#
# f(5)

# # # Выведите на экран строки вида:
# # # *******
# # # ****
# # # *******
# # # ****
# # # *******
# # # ****
# # # (всего n строк, звездочек или 7, или 4 по очереди)
#
# def f(n):
#     for i in range(1, n + 1):
#         if i % 2 != 0:
#             print('*' * 7)
#         else:
#             print('*' * 4)
#
# f(7)

# # Определить четверть точки с координатами x и y
#
# def chetv(x, y):
#     if x > 0 and y > 0:
#         return 'I'
#     elif x < 0 and y > 0:
#         return 'II'
#     elif x < 0 and y < 0:
#         return 'III'
#     else:
#         return 'IV'
#
# print(chetv(5, 6))
# print(chetv(-5, 6))
# print(chetv(-5, -6))
# print(chetv(5, -6))

# # # Найдите наибольшую цифру в данном натуральном числе.
# #
# # def max_digit(x):
# #     return max([int(i) for i in str(x)])
#
# max_digit = lambda x: max([int(i) for i in str(x)])
#
# print(max_digit(12397))
# print(max_digit(6437))

# # Вывести квадрат 7 на 7 из случайных букв
#
# # print(ord('а')) # 1072
# # print(ord('я')) # 1103
# # print(ord('ё')) # 1105
#
# import random
#
# def f(n):
#     a = set()
#     for i in range(1072, 1104):
#         a.add(chr(i))
#     a = list(a)
#     a.sort()
#     a.insert(6, 'ё')
#     # print(*a)
#     # print(len(a))
#     for i in range(n):
#         for j in range(n):
#             print(a[random.randint(0, 32)], end=' ')
#         print()
#
# f(10)

# Найдите, сколько точек с целочисленными координатами попадает в круг
# радиуса r  с центром в точке (x0, y0).
# https://ru.paste.pics/95bf9b97f0bfd3fc2f01a8947079da8e

# def f(x0, y0, r):
#     k = 0
#     for x in range(x0 - r, x0 + r + 1):
#         for y in range(y0 - r, y0 + r + 1):
#             if (x - x0) ** 2 + (y - y0) ** 2 <= r:
#                 k += 1
#     return k
#
# print(f(5, 6, 5))

