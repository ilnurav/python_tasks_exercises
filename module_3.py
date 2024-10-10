# Работа с текстовыми данными

# f = open('test.txt', encoding='utf-8')
# print(f.read())
# file = f.read()
# print(file)
# print(f.read(3))
# print(f.read(10))
# f.seek(0)
# print(f.read(10))
# f.close()
# print(f.read())

# f = open('test.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

# f = open('test.txt', 'r', encoding='utf-8')
# for line in f:
#     line = line.replace('\n', '')
#     print(line)
# s = f.readlines()
# print(s)
# for i in s:
#     i = i.replace('\n', '')
#     print(i)

# f = open('test123.txt', 'w', encoding='utf-8')
# f.write('123' + '\n')
# f.write('hello')
# f.close()

# f = open('test.txt', 'a', encoding='utf-8')
# f.write('\nhello world')
# f.close()

# with open('test.txt', 'a', encoding='utf-8') as f:
#     f.write('\nhello world')
# print(f.read())

# # # # Во входном файле записано два целых числа, каждое в отдельной строке.
# # # # Выведите в выходной файл их сумму.
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = 0
#     for line in f:
#         s += int(line)
# with open('output.txt', 'w', encoding='utf-8') as f:
#     f.write(str(s))

# # # Во входном файле записано два целых числа, которые могут быть разделены пробелами
# # # и концами строк. Выведите в выходной файл их сумму.
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = 0
#     for line in f:
#         s += int(line)
# with open('output.txt', 'w', encoding='utf-8') as f:
#     f.write(str(s))

# Во входном файле записана одна текстовая строка, возможно, содержащая пробелы.
# Выведите эту строку в обратном порядке.

# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#     print(s[::-1])

# with open('input.txt', 'r', encoding='utf-8') as f:
#     print(f.read()[::-1])

# with open('input.txt', 'r', encoding='utf-8') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

# with open('input.txt', 'r', encoding='utf-8') as f:
#     print(f.readline()[::-1])

# # # Выведите все строки данного файла в обратном порядке. Для этого считайте список
# # всех строк при помощи метода readlines().
# #
# # # входные данные
# # Beautiful is better than ugly.
# # Explicit is better than implicit.
# # Simple is better than complex.
# # Complex is better than complicated.
#
# # # выходные данные
# # # Complex is better than complicated.
# # # Simple is better than complex.
# # # Explicit is better than implicit.
# # # Beautiful is better than ugly.
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.readlines()
#     for i in range(len(s) - 1, -1, -1):
#         s[i] = s[i].replace('\n', '')
#         print(s[i])

# # Выведите в обратном порядке содержимое всего файла полностью.
# # Для этого считайте файл целиком при помощи метода read().
#
# # Beautiful is better than ugly.
# # Explicit is better than implicit.
# # Simple is better than complex.
# # Complex is better than complicated.
#
# # .detacilpmoc naht retteb si xelpmoC
# # .xelpmoc naht retteb si elpmiS
# # .ticilpmi naht retteb si ticilpxE
# # .ylgu naht retteb si lufituaeB

# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#     print(s[::-1])

# with open('input.txt', 'r', encoding='utf-8') as f:
#     print(f.read()[::-1])

# # # В выходной файл выведите все строки наибольшей длины из входного файла,
# # не меняя их порядок.
#
# # One
# # Twenty one
# # Two
# # Twenty two
#
# # Twenty one
# # Twenty two
#
# with open('input.txt', 'r', encoding='utf-8') as f, \
#      open('output.txt', 'w', encoding='utf-8') as f1:
#     s = f.readlines()
#     max_len = 0
#     for i in s:
#         i = i.replace('\n', '')
#         if len(i) > max_len:
#             max_len = len(i)
#     for i in s:
#         i = i.replace('\n', '')
#         if len(i) == max_len:
#             f1.write(i + '\n')

# # Определите, есть ли во входном файле символ '@'. Выведите слово YES или NO.
#
# # with open('input.txt', 'r', encoding='utf-8') as f:
# #     s = f.read()
# #     if s.count('@') > 0:
# #         print('YES')
# #     else:
# #         print('NO')
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#     for i in s:
#         if i == '@':
#             print('YES')
#             break
#     else:
#         print('NO')

# # # Дан файл, каждая строка которого может содержать одно или несколько целых чисел,
# # разделенных одним или несколькими пробелами.
# # # Вычислите сумму чисел в каждой строке и выведите эту сумму (для каждой строки
# # выводится сумма чисел в этой строке).
#
# # 2 4 3
# #  3    4
# #  1       5    4
#
# # 9
# # 7
# # 10
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.readlines()
#     for line in s:
#         summ = 0
#         for i in line.split():
#             summ += int(i)
#         print(summ)

# # # В файле могут быть записаны десятичные цифры и все, что угодно.
# # # Числом назовем последовательность цифр, идущих подряд (т.е. число всегда неотрицательно).
# # # Вычислите сумму всех чисел, записанных в файле. В данной задаче удобно считывать данные посимвольно.
#
# #  123
# # aaa456
# # 1x2y3 4 5 6
#
# # 600
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#     summ = 0
#     sr = ''
#     for i in s:
#         if i.isdigit():
#             sr += i
#         else:
#             if sr != '':
#                 summ += int(sr)
#                 sr = ''
# if sr != '':
#    summ += int(sr)
# print(summ)

# # # Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# # # Выведите три найденных числа в формате, приведенном в примере.
#
# # Beautiful is better than ugly.
# # Explicit is better than implicit.
# # Simple is better than complex.
# # Complex is better than complicated.
#
# # Input file contains:
# # 108 letters
# # 20 words
# # 4 lines
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.readlines()
#     lines = len(s)
#     letters = 0
#     words = 0
#     for line in s:
#         words += len(line.split())
#         for i in line:
#             if i.isalpha():
#                 letters += 1
# print('Input file contains:')
# print(f'{letters} letters')
# print(f'{words} words')
# print(f'{lines} lines')

# # Зашифруйте данный текстовый файл шифром Цезаря, при этом символы первой строки файла
# # должны циклически сдвигаться на 1, второй строки — на 2, третьей строки — на три и т.д.
# # В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
#
# # Hello
# # Hello
# # Hello
# # Hello
#

# # Ifmmp
# # Jgnnq
# # Khoor
# # Lipps
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     s = f.readlines()
#     for i in range(len(s)):
#         s[i] = s[i].replace('\n', '')
#         new_s = ''
#         for j in s[i]:
#             new_s += chr(ord(j) + i + 1)
#         print(new_s)


# # # В олимпиаде по информатике принимало участие несколько человек. Победителем олимпиады становится человек,
# # # набравший больше всех баллов.
# # # Победители определяются независимо по каждому классу. Определите количество баллов, которое набрал победитель
# # # в каждом классе.
# # # Гарантируется, что в каждом классе был хотя бы один участник.
# # # Входные данные
# # # Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:
# # # фамилия имя класс балл.
# # # Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из трех чисел 9, 10, 11. Балл - целое число от 0 до 100.
# # # В этой задаче файл необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком.
# # # Выходные данные
# # # Выведите три числа: баллы победителя олимпиады по 9 классу, по 10 классу, по 11 классу. Входной файл в кодировке utf-8
#
# # Иванов Сергей 9 90
# # Сергеев Петр 10 91
# # Петров Василий 11 92
# # Васильев Иван 9 93
# # Сергеев Петр 10 90
# # Петров Василий 11 87
#
# # 93 91 92
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     class9, class10, class11 = [], [], []
#     for line in f:
#         s = line.split()
#         if s[2] == '9': class9.append(int(s[3]))
#         elif s[2] == '10': class10.append(int(s[3]))
#         elif s[2] == '11': class11.append(int(s[3]))
#     print(max(class9), max(class10), max(class11))

# # В условиях предыдущей задачи определите и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11 классе.
#
# # # Иванов Сергей 9 90
# # # Сергеев Петр 10 91
# # # Петров Василий 11 92
# # # Васильев Иван 9 93
# # # Сергеев Петр 10 90
# # # Петров Василий 11 87
#
# # 91.5 90.5 89.5
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     class9, class10, class11 = [], [], []
#     for line in f:
#         s = line.split()
#         if s[2] == '9': class9.append(int(s[3]))
#         elif s[2] == '10': class10.append(int(s[3]))
#         elif s[2] == '11': class11.append(int(s[3]))
#     print(sum(class9) / len(class9),
#           sum(class10) / len(class10),
#           sum(class11) / len(class11))

# # В условиях предыдущей задачи определите количество школьников, ставших победителями в каждом классе.
# # Победителями объявляются все, кто набрал наибольшее число баллов по данному классу. Гарантируется,
# # что в каждом классе был хотя бы один участник.
#
# # Иванов Сергей 9 80
# # Сергеев Петр 10 80
# # Петров Василий 11 81
# # Васильев Андрей 9 81
# # Андреев Александр 10 80
# # Александров Роман 9 81
# # Романов Иван 11 80
#
# # 2 2 1
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     class9, class10, class11 = [], [], []
#     for line in f:
#         s = line.split()
#         if s[2] == '9': class9.append(int(s[3]))
#         elif s[2] == '10': class10.append(int(s[3]))
#         elif s[2] == '11': class11.append(int(s[3]))
#     print(class9.count(max(class9)),
#           class10.count(max(class10)),
#           class11.count(max(class11)))

# # Зачет в олимпиаде проводится без деления на классы. Выведите фамилию и имя победителя олимпиады.
# # Если таких несколько - выведите только их количество.
#
# # Иванов Сергей 9 90
# # Сергеев Петр 10 95
# # Петров Иван 11 85
#
# # Сергеев Петр
#
# # Иванов Сергей 9 90
# # Сергеев Петр 10 85
# # Петров Иван 11 90
#
# # 2
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     fio, balls = [], []
#     for line in f:
#         s = line.split()
#         fio.append(s[0] + ' ' + s[1])
#         balls.append(int(s[3]))
#     if balls.count(max(balls)) > 1:
#         print(balls.count(max(balls)))
#     else:
#         print(fio[balls.index(max(balls))])

# import math
# import os


# print(math.pi)
# print(math.factorial(5))

# from math import pi, sqrt
# # from math import sqrt


# print(pi)
# print(sqrt(9))

# from math import *


# print(sin(23))
# print(ceil(2.4))

# import my_module


# print(my_module.summ(2, 3))
# print(my_module.proizv(3, 5))

# from my_module import *
#
#
# print(summ(2, 4))
# print(proizv(10, 7))

# import os


# os.mkdir('hello')
# os.mkdir('D://ilnur/develop/python/reu_modul1/hello2')

# os.rmdir('hello')
# os.rmdir('D://ilnur/develop/python/reu_modul1/hello2')

# D://ilnur/develop/python/reu_modul1/test.txt
# os.rename('test.txt', 'test2.txt')

# print(os.path.exists('test2.txt'))

# if os.path.exists('test.txt'):
#     print('Указанный файл существует')
# else:
#     print('файл не существует')

# import zipfile
# from zipfile import ZipFile

# with ZipFile('hello.zip', 'w') as myzip:
#     myzip.write('input.txt')
#     myzip.write('test2.txt')

# with ZipFile('hello.zip', 'a') as myzip:
#     myzip.write('test123.txt')

# with ZipFile('hello.zip', 'a') as myzip:
#     print(myzip.infolist())
#
# with ZipFile('hello.zip', 'r') as myzip:
#     myzip.extractall()

# # Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники, которые набрали наибольший
# # балл среди всех участников в данном классе.
# # Для каждого класса определите максимальный балл, который набрал школьник, не ставший победителем в данном классе.
# # Выходные данные
# # Выведите три целых числа.
#
# # Примеры
# # входные данные
# # Иванов Сергей 9 80
# # Сергеев Петр 10 82
# # Петров Василий 11 82
# # Васильев Андрей 9 81
# # Андреев Александр 10 81
# # Александров Роман 9 81
# # Романов Иван 11 83
#
# # выходные данные
# # 80 81 82
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     class9, class10, class11 = set(), set(), set()
#     for line in f:
#         s = line.split()
#         if s[2] == '9': class9.add(int(s[3]))
#         if s[2] == '10': class10.add(int(s[3]))
#         if s[2] == '11': class11.add(int(s[3]))
#     class9 = list(class9)
#     class10 = list(class10)
#     class11 = list(class11)
#     class9.sort()
#     class10.sort()
#     class11.sort()
#     print(class9[-2], class10[-2], class11[-2])

# # Результаты олимпиады подводятся без деления на классы. Победителем олимпиады становятся те, кто набрал
# # больше всего баллов. Призерами олимпиады становятся участники, следующие за победителями.
# #
# # Определите наибольший балл, который набрали призеры олимпиады и количество участников олимпиады,
# # набравших такой балл.
# #
# # Выходные данные
# # Выведите два числа: наибольший балл призера и количество участников, имеющий такой балл.
# #
# # Примеры
# # входные данные
# # Иванов Сергей 9 92
# # Сергеев Петр 10 91
# # Петров Василий 11 92
# # Васильев Иван 9 93
# # выходные данные
# # 92 2
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     balls = []
#     for line in f:
#         s = line.split()
#         balls.append(int(s[3]))
#     set_balls = list(set(balls))
#     set_balls.sort()
#     print(set_balls[-2], balls.count(set_balls[-2]))

# # # В условиях предыдущей задачи выведите фамилию и имя участника олимпиады,
# # набравшего наибольший балл,
# # # но не ставшего победителем. Если таких школьников несколько - выведите их количество.
# #
# # # Примеры
# # # входные данные
# # Иванов Сергей 9 93
# # Сергеев Петр 10 91
# # Петров Василий 11 92
# # Васильев Иван 9 93
# # #
# # # выходные данные
# # # Петров Василий
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     fio, balls = [], []
#     for line in f:
#         s = line.split()
#         fio.append(s[0] + ' ' + s[1])
#         balls.append(int(s[3]))
#     ball2 = sorted(set(balls))[-2]
#     if balls.count(ball2) > 1:
#         print(balls.count(ball2))
#     else:
#         print(fio[balls.index(ball2)])

# # # В олимпиаде по информатике принимало участие N
# # #  человек. Определите школы, из которых в олимпиаде принимало участие больше всего участников.
# # # В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех
# # участниках,
# # # а только подсчитывая число участников для каждой школы.
# # #
# # # Входные данные
# # # Информация о результатах олимпиады записана в файле, каждая из строк которого имеет вид:
# # #
# # # фамилия имя школа балл
# # #
# # # Фамилия и имя — текстовые строки, не содержащие пробелов. Школа — целое число от 1 до 99.
# # # Балл — целое число от 0 до 100.
# # #
# # # Выходные данные
# # # Выведите номера этих школ в порядке возрастания.
# # #
# # # Примеры
# # # входные данные
# # Иванов Сергей 14 56
# # Сергеев Петр 23 74
# # Петров Василий 3 99
# # Васильев Андрей 3 56
# # Андреев Роман 14 75
# # Романов Иван 27 68
# # # выходные данные
# # # 3 14
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     schools = {}
#     for line in f:
#         s = line.split()
#         schools[int(s[2])] = schools.get(int(s[2]), 0) + 1
#     max_count = max(schools.values())
#     schools_list = []
#     for key in schools:
#         if schools[key] == max_count:
#             schools_list.append(key)
#     print(*sorted(schools_list))

# # # В условиях предыдущей задачи определите школы, из которых в олимпиаде принимало участие
# # # меньше всего участников (но был хотя бы один участник).
# # #
# # # Выходные данные
# # # Выведите номера этих школ в порядке возрастания.
# # #
# # # Примеры
# # # входные данные
# # # Иванов Сергей 14 56
# # # Сергеев Петр 23 74
# # # Петров Василий 3 99
# # # Васильев Андрей 3 56
# # # Андреев Роман 14 75
# # # Романов Иван 27 68
# # # выходные данные
# # # 23 27
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     schools = {}
#     for line in f:
#         s = line.split()
#         schools[int(s[2])] = schools.get(int(s[2]), 0) + 1
#     min_count = min(schools.values())
#     schools_list = []
#     for key in schools:
#         if schools[key] == min_count:
#             schools_list.append(key)
#     print(*sorted(schools_list))

# # # Известно, что фамилии всех участников — различны. Сохраните в массивах список всех
# # участников и выведите его,
# # # отсортировав по фамилии в лексикографическом порядке.
# # #
# # # При выводе указываете фамилию, имя участника и его балл.
# # #
# # # Примеры
# # # входные данные
# # # Иванов Сергей 14 56
# # # Сергеев Петр 23 74
# # # Петров Василий 3 99
# # # Васильев Андрей 3 56
# # # Андреев Роман 14 75
# # # Романов Иван 27 68
# #
# # # выходные данные
# # # Андреев Роман 75
# # # Васильев Андрей 56
# # # Иванов Сергей 56
# # # Петров Василий 99
# # # Романов Иван 68
# # # Сергеев Петр 74
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     fio = []
#     for line in f:
#         s = line.split()
#         fio.append(s[0] + ' ' + s[1] + ' ' + s[3])
#     fio.sort()
#     for i in fio:
#         print(i)

# # Отсортируйте список участников олимпиады по убыванию набранного балла
#
# # входные данные
# # Иванов Сергей 14 56
# # Сергеев Петр 23 74
# # Петров Василий 3 99
# # Васильев Андрей 3 56
# # Андреев Роман 14 75
# # Романов Иван 27 68
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     fio = []
#     for line in f:
#         s = line.split()
#         fio.append([s[0], s[1], int(s[3])])
#     sorted_fio = sorted(fio, key=lambda x: x[2], reverse=True)
#     for fio in sorted_fio:
#         print(*fio)

# # В условиях предыдущей задачи выведите в порядке возрастания номера школ,
# # в которых есть хотя бы один победитель олимпиады.
# #
# # Примеры
# # входные данные
# # Иванов Сергей 13 80
# # Сергеев Петр 26 70
# # Сергеев Андрей 35 80
# # Петров Василий 13 80
# # Иванов Роман 35 70
# # Иванов Иван 26 70
# # выходные данные
# # 13 35
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     max_ball = 0
#     for line in f:
#         s = line.split()
#         if int(s[3]) > max_ball:
#             max_ball = int(s[3])
#             schools = set()
#             schools.add(int(s[2]))
#         elif int(s[3]) == max_ball:
#             schools.add(int(s[2]))
#     print(*sorted(schools))

# # # В условиях предыдущей задачи выведите в порядке возрастания номера школ,
# # средний балл учащихся
# # # которых выше, чем средний балл всех участников олимпиады (то есть необходимо
# # вычислить средний
# # # балл для каждой школы и средний балл по всем участникам).
# # #
# # # Примеры
# # # входные данные
# # # Иванов Сергей 13 80
# # # Сергеев Петр 26 70
# # # Сергеев Андрей 35 80
# # # Петров Василий 13 80
# # # Иванов Роман 35 70
# # # Иванов Иван 26 70
# # # выходные данные
# # # 13
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     schools = {}
#     balls = []
#     for line in f:
#         s = line.split()
#         if schools.get(int(s[2]), 0) == 0:
#             schools[int(s[2])] = []
#             schools[int(s[2])].append(int(s[3]))
#         else:
#             schools[int(s[2])].append(int(s[3]))
#         balls.append(int(s[3]))
#     a = []
#     for key in schools:
#         if sum(schools[key]) / len(schools[key]) > sum(balls) / len(balls):
#             a.append(key)
#     print(*sorted(a))

# # # В условиях предыдущей задачи выведите в порядке возрастания номера школ,
# # # средний балл учащихся которых максимален (то есть необходимо вычислить
# # # средний балл для каждой школы и вывести те школы, средний балл для которых максимален).
# # #
# # # Примеры
# # # входные данные
# # # Иванов Сергей 13 80
# # # Сергеев Петр 26 70
# # # Сергеев Андрей 35 80
# # # Петров Василий 13 80
# # # Иванов Роман 35 70
# # # Иванов Иван 26 70
# # # выходные данные
# # # 13
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     schools = {}
#     for line in f:
#         s = line.split()
#         if schools.get(int(s[2]), 0) == 0:
#             schools[int(s[2])] = []
#             schools[int(s[2])].append(int(s[3]))
#         else:
#             schools[int(s[2])].append(int(s[3]))
#     max_sr_ball = 0
#     for key in schools:
#         if sum(schools[key]) / len(schools[key]) > max_sr_ball:
#             max_sr_ball = sum(schools[key]) / len(schools[key])
#             a = []
#             a.append(key)
#         elif sum(schools[key]) / len(schools[key]) == max_sr_ball:
#             a.append(key)
#     print(*sorted(a))

# В условиях предыдущей задачи выведите номера школ, из которых был хотя бы один
# участник олимпиады, в порядке убывания количества участников олимпиады из этих школ.
# Если из двух школ было одинаковое число участников, то их номера выводятся в порядке
# возрастания номера школы.
#
# Примеры
# входные данные
# Иванов Сергей 13 45
# Сергеев Петр 70 45
# Сергеев Андрей 20 55
# Петров Василий 14 55
# Иванов Роман 13 40
# Иванов Иван 70 60
# выходные данные
# 13 70 14 20

# with open('input.txt', 'r', encoding='utf-8') as f:
#     schools = {}
#     balls = []
#     for line in f:
#         s = line.split()
#         if schools.get(int(s[2]), 0) == 0:
#             schools[int(s[2])] = []
#             schools[int(s[2])].append(int(s[3]))
#         else:
#             schools[int(s[2])].append(int(s[3]))
#         balls.append(int(s[3]))

# # # Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# # # Определите количество строк таблицы, для чисел которых одновременно выполнены все следующие условия:
# # # — в строке есть повторяющиеся числа;
# # # — максимальное число в строке не повторяется;
# # # — сумма всех повторяющихся чисел в строке меньше максимального числа этой строки. При подсчёте суммы
# # # повторяющихся чисел каждое число учитывается столько раз, сколько оно встречается.
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     count = 0
#     for line in f:
#         a = [int(i) for i in line.split()]
#         if len(a) != len(set(a)):
#             if a.count(max(a)) == 1:
#                 summ = 0
#                 for i in a:
#                     if a.count(i) > 1:
#                         summ += 1
#                 if summ < max(a):
#                     count += 1
#     print(count)

# # В каждой строке электронной таблицы записаны шесть натуральных чисел.
# # Определите количество строк таблицы, содержащих числа, для которых одновременно
# # выполнены все следующие условия:
# # — все числа в строке различны;
# # — среднее арифметическое наибольшего и наименьшего чисел в строке меньше среднего
# # арифметического всех остальных чисел.
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     count = 0
#     for line in f:
#         a = [int(i) for i in line.split()]
#         if len(a) == len(set(a)):
#             if (max(a) + min(a)) / 2 < (sum(a) - max(a) - min(a)) / 4:
#                 count += 1
#     print(count)

# # Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел.
# # Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# # — в строке есть два числа, каждое из которых повторяется дважды, остальные числа различны;
# # — среднее арифметическое всех повторяющихся чисел строки меньше среднего арифметического всех её чисел.
#
# with open('output.txt', 'r', encoding='utf-8') as f:
#     count = 0
#     for line in f:
#         a = [int(i) for i in line.split()]
#         if len(set(a)) == 5:
#             summ = 0
#             for i in a:
#                 if a.count(i) > 1:
#                     summ += 1
#             if summ / 2 < sum(a) / 7:
#                 count += 1
#     print(count)

# # Текстовый файл состоит из символов X, Y и Z. Определите максимальное количество идущих подряд символов,
# # среди которых каждые два соседних различны.
#
# with open('test2.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#     # print(len(s))
#     max_k = 0
#     k = 1
#     for i in range(1, len(s)):
#         if s[i] != s[i - 1]:
#             k += 1
#         else:
#             max_k = max(max_k, k)
#             k = 1
#     max_k = max(max_k, k)
#     print(max_k)

# # Текстовый файл состоит из символов X, Y и Z.
# # Определите длину самой длинной последовательности, состоящей из символов X.
# # Хотя бы один символ X находится в последовательности.
#
# with open('test2.txt', 'r', encoding='utf-8') as f:
#     s = f.read()
#     max_k = 1
#     k = 1
#     for i in range(len(s) - 1):
#         if s[i] == 'X' and s[i + 1] == 'X':
#             k += 1
#         else:
#             max_k = max(max_k, k)
#             k = 1
#     max_k = max(max_k, k)
#     print(max_k)

# import datetime
#
# day = datetime.date(2024, 2, 20)
# print(day)

# from datetime import date
#
# today = date.today()
# print(today)
# print(type(today))
# print(today.day, today.month, today.year)

# from datetime import time
#
# time1 = time()
# print(time1)
# time2 = time(16, 25)
# print(time2)
# time3 = time(16, 25, 45)
# print(time3)
# time4 = time(16, 25, 45, 23)
# print(time4)

# from datetime import datetime
#
# # day1 = datetime(2024, 5, 30)
# # print(day1)
# # day2 = datetime(2024, 5, 30, 4, 37, 50)
# # print(day2)
#
# now = datetime.now()
# # print(now)
# print(now.day, now.month, now.year, now.hour, now.minute, now.second)

# strptime(str, format)
# %d: день месяца в виде числа
# %m: порядковый номер месяца
# %y: год в виде 2-х чисел
# %Y: год в виде 4-х чисел
# %H: час в 24-х часовом формате
# %M: минута
# %S: секунда

# from datetime import datetime
#
# date1 = datetime.strptime('22/05/2024', '%d/%m/%Y')
# print(date1)
#
# date2 = datetime.strptime('22/05/2024 12:30', '%d/%m/%Y %H:%M')
# print(date2)
#
# date3 = datetime.strptime('22/05/2024 12:30:59', '%d/%m/%Y %H:%M:%S')
# print(date3)
#
# date2 = datetime.strptime('05-22-2024 12:30', '%m-%d-%Y %H:%M')
# print(date2)

# # Выведите на консоль текущее время - час, минуту и секунду
# # в следующем виде: 11 : 22 : 21
#
# from datetime import datetime
#
# now = datetime.now()
# print(now.hour, ':', now.minute, ':', now.second)

# # Выведите на консоль текущую дату - день, месяц и год
# # в следующем виде:
# # День:  16
# # Месяц:  1
# # Год:  2024
#
# from datetime import datetime
#
# now = datetime.now()
# print('День: ', now.day)
# print('Месяц: ', now.month)
# print('Год: ', now.year)

# from time import sleep
# from datetime import datetime
#
# while True:
#     now = datetime.now()
#     print(now.hour, ':', now.minute, ':', now.second)
#     sleep(1)

# from datetime import datetime
#
# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))             # 2017-05-03
# print(now.strftime("%d/%m/%Y"))             # 03/05/2017
# print(now.strftime("%d/%m/%y"))             # 03/05/17
# print(now.strftime("%d %B %Y (%A)"))        # 03 May 2017 (Wednesday)
# print(now.strftime("%d/%m/%y %I:%M"))       # 03/05/17 01:36

# from datetime import timedelta, datetime
#
# now = datetime.now()
# twenty_two_may = datetime(2024, 5, 22)
# period = twenty_two_may - now
# print("{} дней  {} секунд   {} микросекунд".format(period.days, period.seconds, period.microseconds))
# print("Всего: {} секунд".format(period.total_seconds()))

# # # В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам.
# # # Каждый избиратель указывает одну партию, за которую он отдает свой голос. В Государственную Думу попадают партии,
# # # которые набрали не менее 7% от числа голосов избирателей.
# # # Дан список партий и список голосов избирателей. Выведите список партий, которые попадут в Государственную Думу.
# # # Входные данные
# # # В первой строке входного файла написано слово PARTIES:. Далее идет список партий, участвующих в выборах.
# # # Затем идет строка, содержащая слово VOTES:. За ним идут названия партий, за которые проголосовали избиратели,
# # # по одному названию в строке. Названия могут быть только строками из первого списка.
# # # Выходные данные
# # # Программа должна вывести названия партий, получивших не менее 7% от числа голосов в том порядке,
# # # в котором они следуют в первом списке.
# # #
# # # Примеры
# # # входные данные
# # PARTIES:
# # Party one
# # Party two
# # Party three
# # VOTES:
# # Party one
# # Party one
# # Party three
# # Party one
# # Party one
# # Party three
# # Party two
# # Party one
# # Party three
# # Party three
# # Party one
# # Party one
# # Party three
# # Party three
# # Party one
# # # выходные данные
# # # Party one
# # # Party three
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     count = 0
#     start = False
#     votes = {}
#     for line in f:
#         if line.strip() == 'VOTES:':
#             start = True
#             continue
#         if start:
#             votes[line.strip()] = votes.get(line.strip(), 0) + 1
#             count += 1
#     for vote in votes:
#         if votes[vote] / count > 0.07:
#             print(vote)

# # # Формат входных данных аналогичен предыдущей задаче. Выведите список всех партий, участвовавших в выборах,
# # # отсортировав его в порядке убывания количества голосов избирателей
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     start = False
#     votes = {}
#     for line in f:
#         if line.strip() == 'VOTES:':
#             start = True
#             continue
#         if start:
#             votes[line.strip()] = votes.get(line.strip(), 0) + 1
#     sorted_votes = sorted(votes.items(), key=lambda item: item[1], reverse=True)
#     for party in sorted_votes:
#         print(party[0])

# # # В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа
# # # голосов избирателей. Если такого кандидата нет, то во второй тур выборов выходят два кандидата,
# # # набравших наибольшее число голосов.
# # # Входные данные
# # # Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель.
# # # Известно, что общее число кандидатов не превосходит 20, но в отличии от предыдущих задач список
# # # кандидатов явно не задан.
# # # Выходные данные
# # # Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя. Если такого
# # # кандидата нет, программа должна вывести имя кандидата, занявшего первое место, затем имя кандидата,
# # # занявшего второе место.
# # #
# # # Примеры
# # # входные данные
# # Полуэкт Варфоломеев
# # Варфоломей Полуэктов
# # Полуэкт Варфоломеев
# # # выходные данные
# # # Полуэкт Варфоломеев
# #
# # # входные данные
# # Полуэкт Варфоломеев
# # Варфоломей Виссарионов
# # Виссарион Полуэктов
# # Варфоломей Виссарионов
# # Варфоломей Виссарионов
# # Полуэкт Варфоломеев
# # # выходные данные
# # # Варфоломей Виссарионов
# # # Полуэкт Варфоломеев
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     count = 0
#     votes = {}
#     for line in f:
#         votes[line.strip()] = votes.get(line.strip(), 0) + 1
#         count += 1
#     sorted_votes = sorted(votes.items(), key=lambda item: item[1], reverse=True)
#     k = 1
#     for vote in sorted_votes:
#         print(vote[0])
#         if k == 2 or vote[1] / count > 0.5:
#             break
#         k += 1

# # # Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ,
# # # каждый из них оценивается целым числом от 0 до 100 баллов. При этом абитуриенты, набравшие
# # # менее 40 баллов (неудовлетворительную оценку) по любому экзамену из конкурса выбывают.
# # # Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.
# # #
# # # В конкурсе участвует N
# # #  человек, при этом количество мест равно K
# # # . Определите проходной балл, то есть такое количество баллов, что количество участников,
# # # набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов,
# # # набравших наибольшее количество баллов среди непринятых абитуриентов, общее число принятых
# # # абитуриентов станет больше K
# # # .
# # #
# # # Входные данные
# # # Программа получает на вход количество мест K
# # # . Далее идут строки с информацией об абитуриентах, каждая из которых состоит из имени
# # # (текстовая строка содержащая произвольное число пробелов) и трех чисел от 0 до 100,
# # # разделенных пробелами.
# # #
# # # Выходные данные
# # # Программа должна вывести проходной балл в конкурсе. Выведенное значение должно быть
# # # минимальным баллом, который набрал абитуриент, прошедший по конкурсу.
# # #
# # # Также возможны две ситуации, когда проходной балл не определен.
# # #
# # # Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок,
# # # программа должна вывести число 0.
# # #
# # # Если количество абитуриентов, имеющих равный максимальный балл больше чем K,
# # # программа должна вывести число 1.
# # #
# # # Примеры
# # # входные данные
# # 5
# # Иванов Сергей 70 70 70
# # Сергеев Петр 100 100 0
# # Петров Василий 70 60 70
# # Васильев Андрей 70 60 70
# # Андреев Денис 100 30 100
# # Денисов Роман 50 50 50
# # Романов Иван 60 70 70
# # Ким Чен Ир 50 50 50
# # Ким Ир Сен 40 40 40
# # # выходные данные
# # # 200
# # входные данные
# # 1
# # Иванов Сергей 40 40 40
# # Сергеев Петр 100 100 39
# # # выходные данные
# # # 0
# # # входные данные
# # # 1
# # Иванов Сергей 60 60 60
# # Сергеев Петр 100 40 40
# # # выходные данные
# # # 1
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     students = []
#     k = int(f.readline())
#     for line in f:
#         s = line.split()
#         if int(s[-1]) >= 40 and int(s[-2]) >= 40 and int(s[-3]) >= 40:
#             students.append(int(s[-1]) + int(s[-2]) + int(s[-3]))
#     if k == len(students):
#         print(0)
#     elif students.count(max(students)) > k:
#         print(1)
#     else:
#         students.sort(reverse=True)
#         if students[k - 1] == students[k]:
#             k -= 1
#         print(students[k - 1])

# # # В условиях предыдущей задачи определите полупроходной балл, то есть такое значение балла,
# # # что количество абитуриентов, набравших балл выше полупроходного, меньше K
# # # , а количество абитуриентов, набравших балл выше или равный полупроходному, больше K
# # #
# # # Выходные данные
# # # Программа должна вывести значение полупроходного балла, если полупроходного балла не существует,
# # # программа должна вывести одно число 0
# # # .
# # #
# # # Примеры
# # # входные данные
# # # 5
# # # Иванов Сергей 70 70 70
# # # Сергеев Петр 100 100 0
# # # Петров Василий 70 60 70
# # # Васильев Андрей 70 60 70
# # # Андреев Денис 100 30 100
# # # Денисов Роман 50 50 50
# # # Романов Иван 60 70 70
# # # Ким Чен Ир 50 50 50
# # # Ким Ир Сен 40 40 40
# # # выходные данные
# # # 150
# # # входные данные
# # # 1
# # # Иванов Сергей 50 50 50
# # # Сергеев Петр 100 100 100
# # # Ким Ир Сен 100 0 100
# # # выходные данные
# # # 0
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     students = []
#     k = int(f.readline())
#     for line in f:
#         s = line.split()
#         if int(s[-1]) >= 40 and int(s[-2]) >= 40 and int(s[-3]) >= 40:
#             students.append(int(s[-1]) + int(s[-2]) + int(s[-3]))
#     students.sort(reverse=True)
#     if students[k - 1] == students[k]:
#         print(students[k - 1])
#     else:
#         print(0)

# # # Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# # # Определите максимальное количество идущих подряд символов,
# # # среди которых не более одной буквы A.
#
# with open('input1.txt', 'r') as f:
#     s = f.read().split('A')
#     k = 0
#     for i in range(len(s) - 1):
#         k = max(len(s[i]) + len(s[i + 1]) + 1, k)
#     print(k)

# # Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# # Определите максимальную длину цепочки вида XYZXYZXYZ...
# # (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
#
# with open('24_demo.txt', 'r') as f:
#     s = f.readline()
#     k = 0
#     m = 0
#     for i in range(len(s)):
#         if (s[i] == 'X' and k % 3 == 0) or (s[i] == 'Y' and k % 3 == 1) or (s[i] == 'Z' and k % 3 == 2):
#             k += 1
#             m = max(m, k)
#         elif s[i] == 'X':
#             k = 1
#         else:
#             k = 0
#     print(m)

# pip install telebot

# import telebot
#
# bot = telebot.TeleBot('7169779737:AAFFAzVpl1LGb599tqEeHNEsLd99nHkV4x8')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'К работе готов! Давайте общаться!')
#
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
#
# bot.polling(none_stop=True, interval=0)

# # pip install wikipedia
#
# import telebot, wikipedia, re
#
# bot = telebot.TeleBot('7169779737:AAFFAzVpl1LGb599tqEeHNEsLd99nHkV4x8')
#
# wikipedia.set_lang('ru')
#
# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         wikitext = ny.content[:1000]
#         wikimas = wikitext.split('.')
#         wikimas = wikimas[:-1]
#         wikitext2 = ''
#         for x in wikimas:
#             if not('==' in x):
#                 if(len(x.strip()) > 3):
#                     wikitext2 += x + '.'
#             else:
#                 break
#         wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
#         return wikitext2
#     except Exception as e:
#         return 'В Википедии нет такой информации!'
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Введите любое слово, чтобы узнать, что это такое!')
#
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id,  getwiki(message.text))
#
# bot.polling(none_stop=True, interval=0)


# import telebot
# import random
# from telebot import types
#
# f = open('facts.txt', 'r', encoding='utf-8')
# facts = f.readlines()
# f.close()
#
# f = open('thinks.txt', 'r', encoding='utf-8')
# thinks = f.readlines()
# f.close()
#
# bot = telebot.TeleBot('7169779737:AAFFAzVpl1LGb599tqEeHNEsLd99nHkV4x8')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('Новость')
#     item2 = types.KeyboardButton('Афоризм')
#     markup.add(item1)
#     markup.add(item2)
#     bot.send_message(message.chat.id,
#                      'Нажми Новость или Афоризм',
#                      reply_markup=markup)
#
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     if message.text.strip().lower() == 'новость':
#         answer = random.choice(facts)
#     elif message.text.strip().lower() == 'афоризм':
#         answer = random.choice(thinks)
#     else:
#         answer = 'Неправильная команда!'
#     bot.send_message(message.chat.id, answer)
#
# bot.polling(none_stop=True, interval=0)


# import telebot
# import time
#
# bot = telebot.TeleBot('7169779737:AAFFAzVpl1LGb599tqEeHNEsLd99nHkV4x8')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     f = open('facts.txt', 'r', encoding='utf-8')
#     facts = f.readlines()
#     f.close()
#     for fact in facts:
#         bot.send_message(message.chat.id, fact)
#         time.sleep(5)
#
# bot.polling(none_stop=True, interval=0)


# # u: Привет!
# # Ну привет!
# #
# # u: Как дела?
# # Да помаленьку.
# #
# # u: Пойдем гулять.
# # Я пока не могу, работы много.
#
# # pip install fuzzywuzzy
#
# import telebot
# from fuzzywuzzy import fuzz
#
# bot = telebot.TeleBot('7169779737:AAFFAzVpl1LGb599tqEeHNEsLd99nHkV4x8')
#
# mas = []
# f = open('dialog.txt', 'r', encoding='utf-8')
# for x in f:
#     if len(x.strip()) > 2:
#         mas.append(x.strip().lower())
# f.close()
#
# def answer(text):
#     try:
#         text = text.strip().lower()
#         a = 0
#         n = 0
#         nn = 0
#         for q in mas:
#             if 'u: ' in q:
#                 aa = (fuzz.token_sort_ratio(q.replace('u: ',''), text))
#                 if aa > a and aa != a:
#                     a = aa
#                     nn = n
#                 n += 1
#         s = mas[nn + 1]
#         return s
#     except:
#         return 'Ошибка'
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Давай поболтаем!')
#
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     s = answer(message.text)
#     bot.send_message(message.chat.id, s)
#
# bot.polling(none_stop=True, interval=0)


# # pip install bs4
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# quotes = soup.find_all('span', class_='text')
# for quote in quotes:
#     print(quote.text)

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# for i in range(len(quotes)):
#     print(quotes[i].text)
#     print(authors[i].text)
#     print()

# # import requests
# # from bs4 import BeautifulSoup
# #
# # k = 1
# # for p in range(1, 11):
# #     url = f'https://quotes.toscrape.com/page/{p}'
# #     response = requests.get(url)
# #
# #     soup = BeautifulSoup(response.text, 'html.parser')
# #     quotes = soup.find_all('span', class_='text')
# #     authors = soup.find_all('small', class_='author')
# #     for i in range(len(quotes)):
# #         print(k, quotes[i].text)
# #         print(authors[i].text)
# #         print()
# #         k += 1
#
# # import requests
# # from bs4 import BeautifulSoup
# #
# # k = 1
# # for p in range(1, 11):
# #     url = f'https://quotes.toscrape.com/page/{p}'
# #     response = requests.get(url)
# #
# #     soup = BeautifulSoup(response.text, 'html.parser')
# #     quotes = soup.find_all('span', class_='text')
# #     authors = soup.find_all('small', class_='author')
# #     tags = soup.find_all('div', class_='tags')
# #
# #     for i in range(len(quotes)):
# #         print(f'{k}) Quote: {quotes[i].text}')
# #         print(len(f'{k}) ') * ' ' + f'Author: {authors[i].text}')
# #         my_tags = tags[i].find_all('a', class_='tag')
# #         print(len(f'{k}) ') * ' ' + f'Tags: ', end='')
# #         for my_tag in my_tags:
# #             print(my_tag.text, end=' ')
# #         print('\n')
# #         k += 1
#
# # import requests
# # from bs4 import BeautifulSoup
# #
# # with open('quotes.txt', 'w', encoding='utf-8') as f:
# #     k = 1
# #     for p in range(1, 11):
# #         url = f'https://quotes.toscrape.com/page/{p}'
# #         response = requests.get(url)
# #
# #         soup = BeautifulSoup(response.text, 'html.parser')
# #         quotes = soup.find_all('span', class_='text')
# #         authors = soup.find_all('small', class_='author')
# #         tags = soup.find_all('div', class_='tags')
# #
# #         for i in range(len(quotes)):
# #             f.write(f'{k}) Quote: {quotes[i].text}\n')
# #             f.write(len(f'{k}) ') * ' ' + f'Author: {authors[i].text}\n')
# #             my_tags = tags[i].find_all('a', class_='tag')
# #             f.write(len(f'{k}) ') * ' ' + f'Tags: ')
# #             for my_tag in my_tags:
# #                 f.write(my_tag.text)
# #             f.write('\n\n')
# #             k += 1
#
#
# import requests
# from bs4 import BeautifulSoup
#
# with open('quotes.txt', 'w', encoding='utf-8') as f:
#     k = 1
#     tags_dict = {}
#     for p in range(1, 11):
#         url = f'https://quotes.toscrape.com/page/{p}'
#         response = requests.get(url)
#
#         soup = BeautifulSoup(response.text, 'html.parser')
#         quotes = soup.find_all('span', class_='text')
#         authors = soup.find_all('small', class_='author')
#         tags = soup.find_all('div', class_='tags')
#
#         for i in range(len(quotes)):
#             f.write(f'{k}) Quote: {quotes[i].text}\n')
#             f.write(len(f'{k}) ') * ' ' + f'Author: {authors[i].text}\n')
#             my_tags = tags[i].find_all('a', class_='tag')
#             f.write(len(f'{k}) ') * ' ' + f'Tags: ')
#             for my_tag in my_tags:
#                 f.write(my_tag.text)
#                 if tags_dict.get(my_tag.text, 0) == 0:
#                     tags_dict[my_tag.text] = []
#                     tags_dict[my_tag.text].append(quotes[i].text)
#                 else:
#                     tags_dict[my_tag.text].append(quotes[i].text)
#             f.write('\n\n')
#             k += 1
# with open('tags.txt', 'w', encoding='utf-8') as f:
#     k = 1
#     for tag in tags_dict:
#         f.write(f'{k}) Tag: {tag}\n')
#         f.write(len(f'{k}) ') * ' ' + f'Quotes: \n')
#         n = 1
#         for quote in tags_dict[tag]:
#             f.write(len(f'{k}) ') * ' ' + f'{n}. {quote}\n')
#             n += 1
#         f.write('\n')
#         k += 1

# import requests
# from bs4 import BeautifulSoup
#
# with open('quotes.txt', 'w', encoding='utf-8') as f:
#     k = 1
#     tags_dict = {}
#     authors_url_dict = {}
#     authors_quote_dict = {}
#     for p in range(1, 11):
#         url = f'https://quotes.toscrape.com/page/{p}'
#         response = requests.get(url)
#
#         soup = BeautifulSoup(response.text, 'html.parser')
#         quotes = soup.find_all('span', class_='text')
#         authors = soup.find_all('small', class_='author')
#         tags = soup.find_all('div', class_='tags')
#         divs = soup.find_all('div', class_='quote')
#
#         for i in range(len(quotes)):
#             if authors_url_dict.get(authors[i].text, 0) == 0:
#                 authors_url_dict[authors[i].text] = 'https://quotes.toscrape.com' + divs[i].a['href']
#             if authors_quote_dict.get(authors[i].text, 0) == 0:
#                 authors_quote_dict[authors[i].text] = []
#                 authors_quote_dict[authors[i].text].append(quotes[i].text)
#             else:
#                 authors_quote_dict[authors[i].text].append(quotes[i].text)
#             f.write(f'{k}) Quote: {quotes[i].text}\n')
#             f.write(len(f'{k}) ') * ' ' + f'Author: {authors[i].text}\n')
#             my_tags = tags[i].find_all('a', class_='tag')
#             f.write(len(f'{k}) ') * ' ' + f'Tags: ')
#             for my_tag in my_tags:
#                 f.write(my_tag.text)
#                 if tags_dict.get(my_tag.text, 0) == 0:
#                     tags_dict[my_tag.text] = []
#                     tags_dict[my_tag.text].append(quotes[i].text)
#                 else:
#                     tags_dict[my_tag.text].append(quotes[i].text)
#             f.write('\n\n')
#             k += 1
# with open('tags.txt', 'w', encoding='utf-8') as f:
#     k = 1
#     for tag in tags_dict:
#         f.write(f'{k}) Tag: {tag}\n')
#         f.write(len(f'{k}) ') * ' ' + f'Quotes: \n')
#         n = 1
#         for quote in tags_dict[tag]:
#             f.write(len(f'{k}) ') * ' ' + f'{n}. {quote}\n')
#             n += 1
#         f.write('\n')
#         k += 1
# with open('authors.txt', 'w', encoding='utf-8') as f:
#     k = 1
#     for author in authors_quote_dict:
#         response = requests.get(authors_url_dict[author])
#         soup = BeautifulSoup(response.text, 'html.parser')
#         born_date = soup.find('span', class_='author-born-date')
#         born_location = soup.find('span', class_='author-born-location')
#         author_description = soup.find('div', class_='author-description')
#         f.write(f'{k}) Author: {author}\n')
#         f.write(len(f'{k}) ') * ' ' + f'Born date: {born_date.text}\n')
#         f.write(len(f'{k}) ') * ' ' + f'Born location: {born_location.text}\n')
#         f.write(len(f'{k}) ') * ' ' + f'Description: {author_description.text.strip()}\n')
#         f.write(len(f'{k}) ') * ' ' + f'Quotes: \n')
#         n = 1
#         for quote in authors_quote_dict[author]:
#             f.write(len(f'{k}) ') * ' ' + f'{n}. {quote}\n')
#             n += 1
#         f.write('\n')
#         k += 1


# import requests
# from bs4 import BeautifulSoup
# import os
# import gdown # pip install gdown
#
# k = 1
# cwd_path = os.getcwd()
# for page in range(1, 2):
#     url = f'https://2krossovka.ru/katalog/?page={page}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         products = soup.find_all('div', class_='caption')
#         for product in products:
#             title = product.h4.a.text.strip()
#             price = product.p.text.strip()
#             url_product = product.h4.a['href'].strip()
#             print(k, title, price, url_product)
#             response_product = requests.get(url_product)
#             if response_product.status_code == 200:
#                 soup_product = BeautifulSoup(response_product.text, 'html.parser')
#                 table_info = soup_product.find('table', class_='table')
#                 info_names = table_info.find_all(attrs={'itemprop': 'name'})
#                 info_values = table_info.find_all(attrs={'itemprop': 'value'})
#                 category = ''
#                 names_list = []
#                 values_list = []
#                 for i in range(len(info_names)):
#                     names_list.append(info_names[i].text.strip())
#                     values_list.append(info_values[i].text.strip())
#                     # print(info_names[i].text.strip(),
#                     #      info_values[i].text.strip())
#                     if info_names[i].text.strip() == 'Категория':
#                         category = info_values[i].text.strip()
#                 title_url = ''.join(c for c in title if c.isalnum() or c == '_' or c == ' ')
#                 os.chdir(cwd_path)
#                 path_name = f'{cwd_path}\\2krossovka.ru\\{category}\\{title_url}'
#                 if not os.path.exists(path_name):
#                     os.makedirs(path_name)
#                 os.chdir(path_name)
#                 with open('info.txt', 'w', encoding='utf-8') as f:
#                     f.write(f'Товар: {title}\n')
#                     f.write(f'{price}\n')
#                     f.write(f'Характеристики:\n')
#                     for i in range(len(names_list)):
#                         f.write(f'{names_list[i]}: {values_list[i]}\n')
#                 images_url = soup_product.find_all('a', class_='thumbnail')
#                 for image in images_url:
#                     # print(image['href'].strip())
#                     gdown.download(image['href'].strip(), None, quiet=True)
#             k += 1
#             print()

import xml.etree.ElementTree as ET

# p = ET.Element('parent')
# c1 = ET.SubElement(p, 'child1')
# c2 = ET.SubElement(p, 'child2')
# ET.dump(p)
#
# comment = ET.Comment('user comment')
# p.append(comment)
# ET.dump(p)
#
# tree = ET.ElementTree(p)
# tree.write('sample.xml')

# tree = ET.parse('sample.xml')
# root = tree.getroot()
# element1 = root[0]
# print(element1.tag)
# element2 = root[1]
# print(element2.tag)
# element1.text = 'text1'
# element2.text = 'text2'
# element1.set('name', 'value')
# element2.set('name', 'value2')
# tree.write('sample2.xml')

# tree = ET.parse('sample2.xml')
# root = tree.getroot()
# element2 = root[1]
# root.remove(element2)
# tree.write('sample3.xml')

# tree = ET.parse('sample2.xml')
# root = tree.getroot()
# for child in root:
#     print(child.tag,
#           child.text,
#           child.attrib,
#           child.attrib['name'])

# tree = ET.parse('book.xml')
#
# # books = tree.findall("Books/Book")
# # for book in books:
# #     print('Title:', book[0].text)
# #     print('Author:', book[1].text)
# #     print()
#
# # book = tree.find("Books/Book[Title='The Eye of The World']")
# # print(book[1].text)
#
# # book = tree.find("Books/Book[Author='Robert Jordan']")
# # print(book[0].text)
#
# # book = tree.find("Books/Book[@id='5']")
# # print(book[0].text)
# # print(book[1].text)
#
# # book = tree.find("Books/Book[@price='7.95']")
# # print(book[0].text)
# # print(book[1].text)
#
# # authors = tree.findall(".//Author")
# # for author in authors:
# #     print(author.text)
#
# titles = tree.findall(".//Title")
# for title in titles:
#     print(title.text)

'''
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
</data>    
'''

# import xml.etree.ElementTree as ET
#
# tree = ET.parse('countries.xml')
# root = tree.getroot()
# countries = root.findall('country')
# for country in countries:
#     print('Name country:', country.get('name'))
#     print('Rank:', country[0].text)
#     print('Year', country[1].text)
#     print('GDPPC:', country[2].text)
#     neighbors = country.findall('neighbor')
#     for neighbor in neighbors:
#         print('Neighbor:', neighbor.get('name'),
#               'Direction:', neighbor.get('direction'))
#     print()


# import json

# with open('capitals.json', 'r', encoding='utf-8') as f:
#     capitals_json = f.read()
#
# capitals = json.loads(capitals_json)
#
# for country in capitals:
#     print(country, capitals[country])

# capitals = {
#     'Russia': 'Moscow',
#     'Belarus': 'Minsk',
#     'Kazakhstan': 'Astana'
# }
#
# capitals_json = json.dumps(capitals)
# with open('capitals2.json', 'w') as f:
#     f.write(capitals_json)

# import requests
#
# response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# data = response.json()
# print(data['Date'])
# print(data['PreviousDate'])
# print(data['PreviousURL'])
# print(data['Timestamp'])
# print()
# for k, valute in enumerate(data['Valute'].values(), start=1):
#     print(k, 'CharCode:', valute['CharCode'])
#     print('Value:', valute['Value'])
#     print('Previous:', valute['Previous'])
#     print('Name:', valute['Name'])
#     print('ID:', valute['ID'])
#     print('NumCode:', valute['NumCode'])
#     print('Nominal:', valute['Nominal'])
#     print()


# import requests
#
# response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# data = response.json()
#
# char_code = input('Введите валюту (3 символа): ').upper()
# if len(char_code) == 3:
#     for valute in data['Valute'].values():
#         if valute['CharCode'] == char_code:
#             print('Курс валюты')
#             print(valute['Name'])
#             print(valute['Value'])
#             break
#     else:
#         print('Введите корретные данные!')
# else:
#     print('Введите корректные данные!')


# import requests
#
# response = requests.get('https://randomuser.me/api/')
# data = response.json()
# # print(data['results'][0]['gender'])
# # for user in data['results'][0]:
# #     print(user, data['results'][0][user])
# print(data['results'][0]['name']['first'])
# print(data['results'][0]['name']['last'])
# print(data['results'][0]['email'])
# print(data['results'][0]['login']['username'])
# print(data['results'][0]['login']['password'])
# print(data['results'][0]['dob']['age'])
# print(data['results'][0]['phone'])
# print(data['results'][0]['picture']['large'])

# import requests
#
# response = requests.get('https://api.thecatapi.com/v1/breeds')
# data = response.json()
# print(len(data))
# print(data[0])
# print(data[1])
# print(data[0]['weight'])
# print(data[1]['name'])

# import requests
#
# response = requests.get('https://fakestoreapi.com/products')
# data = response.json()
# print(data)
# print(len(data))
# print(data[4])
# print(data[5]['title'])
# print(data[5]['price'])

# import requests
# from translate import Translator # pip install translate
#
# response = requests.get('http://numbersapi.com/12')
# # print(response.text)
# print(f"Факт об этом числе: {Translator(to_lang='ru').translate(response.text)}")
