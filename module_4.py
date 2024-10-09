# Объектно-ориентированное программирование
# Классы и объекты

# a = 10
# b = 'hello'
# print(type(a))
# print(type(b))

# class название_класса:
#     атрибуты_класса
#     методы_класса

# class Person:
#     pass
#
# tom = Person()
# bob = Person()
#
# print(type(tom))
# print(type(bob))

# class Person:
#     def __init__(self):
#         print('Создание объекта Person')
#
# tom = Person()

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# tom = Person('Том', 25)
#
# print(tom.age)
# print(tom.name)
#
# tom.age = 30
# print(tom.age)

# class Person:
#
#     def __init__(self, name2, age2):
#         self.name = name2
#         self.age = age2
#
# tom = Person('Том', 25)
#
# print(tom.age)
# print(tom.name)
#
# tom.age = 30
# print(tom.age)

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# tom = Person('Том', 25)
#
# tom.company = 'Microsoft'
# print(tom.company)
#
# bob = Person('Bob', 27)
# print(bob.company)


# class Person:
#     def say_hello(self):
#         print('Hello')
#
# tom = Person()
# tom.say_hello()
#
# bob = Person()
# bob.say_hello()

# class Person:
#     def say(self, message):
#         print(message)
#
# tom = Person()
# tom.say('Hello World!')

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(f'Name: {self.name}  Age: {self.age}')
#
# tom = Person('Tom', 25)
# tom.display_info()
#
# bob = Person('Bob', 30)
# bob.display_info()

# from time import sleep
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         print('Создан человек с именем', self.name)
#
#     def __del__(self):
#         print('Удален человек с именем', self.name)
#
# tom = Person('Tom')
# sleep(10)

# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         print('Создан человек с именем', self.name)
#
#     def __del__(self):
#         print('Удален человек с именем', self.name)
#
# def create_person():
#     tom = Person('Tom')
#     print(type(tom))
#
# create_person()
# print('Конец программы')


# # # Определите класс Rectangle, который представляет прямоугольник. Через конструктор класс принимает ширину и длину и сохраняет их в атрибутах
# # # width и length соответственно. Также в этом классе определите метод area, который возвращает площадь прямоугольника, и метод perimeter,
# # # который возвращает периметра прямоугольника.
# # # После создания класса определите несколько объектов класса Rectangle и продемонстрируйте работу его методов.
#
# class Rectangle:
#
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def area(self):
#         return self.width * self.length
#
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#
# rect1 = Rectangle(40, 40)
# print('площадь:', rect1.area())
# print('периметр:', rect1.perimeter())
# print()
# rect2 = Rectangle(20, 30)
# print('площадь:', rect2.area())
# print('периметр:', rect2.perimeter())

# # # Создайте класс BankAccount, который представляет банковский счет. Определите в этом классе атрибуты account_number и balance,
# # # которые представляют номер счета и баланс. Через параметры конструктора передайте этим атрибутам начальные значения.
# # #
# # # Также в классе определите метод add, который принимает некоторую сумму и добавляет ее на баланс счета. И определите метод withdraw,
# # # который принимает некоторую сумму и снимает ее с баланса. При этом с баланса нельзя снять больше, чем имеется. Если на балансе
# # # недостаточно средств, то пользователю должно выводиться соответствующее сообщение.
#
#
# class BankAccount:
#
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#         print(f'Создан счет номер: {self.account_number}. Начальный баланс: {self.balance}')
#
#     def add(self, summ):
#         self.balance += summ
#         print(f'На счет зачислено: {summ}. Текущий баланс: {self.balance}')
#
#     def withdraw(self, summ):
#         if self.balance >= summ:
#             self.balance -= summ
#             print(f'Со счета снято: {summ}. Текущий баланс: {self.balance}')
#         else:
#             print('Недостаточно средств на счете')
#
# account1 = BankAccount('12345678', 10000)
# account1.add(5000)
# account1.withdraw(7000)
# account1.withdraw(9000)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_person(self):
#         print(f'Имя: {self.name} Возраст: {self.age}')
#
# tom = Person('Tom', 30)
# tom.print_person()
# tom.name = 'Bob'
# tom.age = -15
# tom.print_person()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_person(self):
#         print(f'Имя: {self.__name} Возраст: {self.__age}')
#
# tom = Person('Tom', 30)
# tom.print_person()
# tom.__name = 'Bob'
# tom.__age = -15
# tom.print_person()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def set_age(self, age):
#         if 0 < age < 200:
#             self.__age = age
#         else:
#             print('Недопустимый возраст')
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def print_person(self):
#         print(f'Имя: {self.__name} Возраст: {self.__age}')
#
# tom = Person('Том', 32)
# tom.print_person()
# tom.set_age(25)
# tom.print_person()
# tom.set_age(-20)
# tom.print_person()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 200:
#             self.__age = age
#         else:
#             print('Недопустимый возраст')
#
#     @property
#     def name(self):
#         return self.__name
#
#     def print_person(self):
#         print(f'Имя: {self.__name} Возраст {self.__age}')
#
# tom = Person('Tom', 30)
# tom.print_person()
# tom.age = 25
# print(tom.age)
# tom.age = -30
# tom.print_person()

# # class Triangle с методом type_triangle, который определяет тип треугольника
# # прямоугольный, остроугольный или тупоугольный
# # площадь треугольника через формулу Герона
#
# class Triangle:
#
#     def __init__(self, a, b, c):
#         lst = sorted([a, b, c])
#         self.a = lst[2]
#         self.b = lst[1]
#         self.c = lst[0]
#
#     def type_triangle(self):
#         if self.a ** 2 == self.b ** 2 + self.c ** 2:
#             return 'прямоугольный'
#         elif self.a ** 2 < self.b ** 2 + self.c ** 2:
#             return 'остроугольный'
#         else:
#             return 'тупоугольный'
#
#     def geron(self):
#         p = (self.a + self.b + self.c) / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
# t1 = Triangle(3, 4, 5)
# print(t1.type_triangle(), round(t1.geron(), 2))
# t2 = Triangle(4, 4, 2)
# print(t2.type_triangle(), round(t2.geron(), 2))
# t3 = Triangle(3, 3, 5)
# print(t3.type_triangle(), round(t3.geron(), 2))

# # # Создать класс MyMath, где атрибутами являются 2 числа,
# # а методами - 4 арифмет. операции + - * /
#
# class MyMath:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def multi(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
# t = MyMath(6, 3)
# print(t.add(), t.sub(), t.multi(), t.div())

# # '''
# # Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# # Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени
# # конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о
# # номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет
# # изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student, установить им разные имена,
# # возраст и номер группы.
# # '''
#
# class Student:
#
#     def __init__(self, name='Ivan', groupNumber='10A', age=18):
#         self.__name = name
#         self.__groupNumber = groupNumber
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 < age < 200:
#             self.__age = age
#         else:
#             print(age, 'недопустимый возраст!')
#
#     @property
#     def groupNumber(self):
#         return self.__groupNumber
#
#     @groupNumber.setter
#     def groupNumber(self, groupNumber):
#         self.__groupNumber = groupNumber
#
# # oleg = Student()
# # print(oleg.name, oleg.groupNumber, oleg.age)
# # oleg.name = 'Олег'
# # print(oleg.name)
#
# # alex = Student('Alex')
# # print(alex.name, alex.groupNumber, alex.age)
# # alex.groupNumber = '13N'
# # print(alex.groupNumber)
#
# # petr = Student('Petr', '12B')
# # print(petr.name, petr.groupNumber, petr.age)
# # petr.age = 21
# # print(petr.age)
#
# jay = Student('Jay', '11A', 20)
# print(jay.name, jay.groupNumber, jay.age)
# jay.age = -20
# print(jay.age)


# class Подкласс (Суперкласс):
#     ...

# class Person:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Name: {self.__name}')
#
# class Employee:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Name: {self.__name}')
#
#     def work(self):
#         print(f'{self.name}')

# class Person:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Name: {self.__name}')
#
#
# class Employee(Person):
#
#     def work(self):
#         print(f'{self.name} works!')
#
# tom = Employee('Tom')
# print(tom.name)
# tom.display_info()
# tom.work()

# class Person:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Name: {self.__name}')
#
#
# class Employee(Person):
#
#     def work(self):
#         print(f'{self.__name} works!')
#
# tom = Employee('Tom')
# print(tom.name)
# tom.display_info()
# tom.work()

# class Employee:
#     def work(self):
#         print('Employee works')
#
# class Student:
#     def study(self):
#         print('Student studies')
#
# class WorkingStudent(Employee, Student):
#     pass
#
# tom = WorkingStudent()
# tom.work()
# tom.study()

# class Employee:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def work(self):
#         print(f'{self.name} works')
#
# class Student:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def study(self):
#         print(f'{self.name} studies')
#
# class WorkingStudent(Employee, Student):
#     pass
#
# tom = WorkingStudent('Tom')
# tom.work()
# tom.study()

# class Employee:
#     def do(self):
#         print('Employee works')
#
# class Student:
#     def do(self):
#         print('Student studies')
#
# class WorkingStudent(Student, Employee):
#     pass
#
# tom = WorkingStudent()
# tom.do()
# print(WorkingStudent.mro())

# class Person:
#
#     def __init__(self, name):
#         self.__name = name  # имя человека
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Name: {self.__name} ")
#
#
# class Employee(Person):
#
#     def __init__(self, name, company):
#         super().__init__(name)
#         self.company = company
#
#     def display_info(self):
#         super().display_info()
#         print(f'Company: {self.company}')
#
#     def work(self):
#         print(f"{self.name} works")
#
# tom = Employee('Tom', 'Intel')
# tom.display_info()

# a = 10
# b = 'hello'
# print(isinstance(a, int))
# print(isinstance(a, str))
# print(isinstance(b, int))
# print(isinstance(b, str))

# class Person:
#
#     def __init__(self, name):
#         self.__name = name  # имя человека
#
#     @property
#     def name(self):
#         return self.__name
#
#     def do_nothing(self):
#         print(f"{self.name} does nothing")
#
#
# #  класс работника
# class Employee(Person):
#
#     def work(self):
#         print(f"{self.name} works")
#
#
# #  класс студента
# class Student(Person):
#
#     def study(self):
#         print(f"{self.name} studies")
#
# def act(person):
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Employee):
#         person.work()
#     elif isinstance(person, Person):
#         person.do_nothing()
#
# tom = Employee('Tom')
# bob = Student('Bob')
# sam = Person('Sam')
#
# act(tom)
# act(bob)
# act(sam)

# # '''
# # Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# # Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# # Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска.
# # Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.
# # '''
#
# class Car:
#
#     def __init__(self, color, type, year, engine=False):
#         self.__color = color
#         self.__type = type
#         self.__year = year
#         self.__engine = engine
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         if isinstance(color, str):
#             self.__color = color
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def type(self):
#         return self.__type
#
#     @type.setter
#     def type(self, type):
#         if isinstance(type, str):
#             self.__type = type
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, year):
#         if isinstance(year, int):
#             if year > 0:
#                 self.__year = year
#             else:
#                 print('Принимаются только положительные значения!')
#         else:
#             print('Введите атрибут класса int!')
#
#     @property
#     def engine(self):
#         return self.__engine
#
#     @engine.setter
#     def engine(self, engine):
#         if isinstance(engine, bool):
#             self.__engine = engine
#         else:
#             print('Введите атрибут класса bool!')
#
#     def start_car(self):
#         self.__engine = True
#         print('Машина заведена!')
#
#     def stop_car(self):
#         self.__engine = False
#         print('Машина заглушена!')
#
#
# lada = Car('черный', 'седан', 2015)
# print(lada.color, lada.type, lada.year, lada.engine)
# lada.start_car()
# print(lada.engine)
# lada.color = 'белый'
# print(lada.color)
# lada.stop_car()

# # '''
# # Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота). Напишите метод calculate_area,
# # который вычисляет площадь прямоугольника. Создайте несколько экземпляров класса Rectangle и выведите их площади.
# # '''
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         if isinstance(width, int) or isinstance(width, float):
#             self.__width = width
#         else:
#             print('Введите атрибут класса int или float!')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if isinstance(height, int) or isinstance(height, float):
#             self.__height = height
#         else:
#             print('Введите атрибут класса int или float!')
#
#     def calculate_area(self):
#         return self.__width * self.__height
#
# rect1 = Rectangle(5, 5)
# print(rect1.calculate_area())
# rect1.height = 6
# print(rect1.calculate_area())
# rect1.width = 5.5
# print(rect1.calculate_area())

# # '''
# # Разработайте класс Person, у которого есть атрибуты name (имя) и age (возраст). Напишите метод greet,
# # который выводит приветствие с именем объекта Person. Создайте несколько экземпляров класса Person и вызовите метод greet для каждого из них.
# # '''
#
# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if isinstance(age, int):
#             self.__age = age
#         else:
#             print('Введите атрибут класса int!')
#
#     def greet(self):
#         print(f'Привет, {self.__name}!')
#
# p1 = Person('Иван', 25)
# p2 = Person('Олег', 20)
# p1.greet()
# p2.greet()

# # '''
# # Создайте класс Student, у которого есть атрибуты name (имя), age (возраст) и grades (оценки).
# # Напишите методы add_grade (добавление оценки) и calculate_average_grade (вычисление средней оценки).
# # Создайте несколько экземпляров класса Student, добавьте им оценки и выведите среднюю оценку каждого студента.
# # '''
#
# class Student:
#
#     def __init__(self, name, age, grades=None):
#         self.__name = name
#         self.__age = age
#         self.__grades = []
#         if grades is not None:
#             self.__grades.append(grades)
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if isinstance(age, str):
#             self.__age = age
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def grades(self):
#         return ' '.join([str(i) for i in self.__grades])
#
#     @grades.setter
#     def grades(self, grade):
#         if isinstance(grade, int):
#             self.__grades.append(grade)
#         else:
#             print('Введите атрибут класса int!')
#
#     def add_grades(self, *grades):
#         if isinstance(grades, tuple):
#             for grade in grades:
#                 self.__grades.append(grade)
#         else:
#             print('Введите кортеж оценок!')
#
#     def calc_aver_grade(self):
#         if len(self.__grades) == 0:
#             return 0
#         else:
#             return round(sum(self.__grades) / len(self.__grades), 2)
#
# s1 = Student('Петр', 20)
# print(s1.calc_aver_grade())
# s1.grades = 5
# print(s1.calc_aver_grade())
# s1.add_grades(2, 3, 4)
# print(s1.calc_aver_grade())

# # '''
# # Создайте класс Kvadr_urav, у которого есть 3 атрибута a, b и c (параметры квадратного уравнения).
# # И метод solve, который решает данное уравнение с учетом того, что у уравнения может быть 1 действительный корень,
# # 2 действительных корня или нет действительных корней.
# # '''
#
# class Kvadr_urav:
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         if isinstance(a, int) or isinstance(a, float):
#             self.__a = a
#         else:
#             print('Введите атрибут класса int или float!')
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         if isinstance(b, int) or isinstance(b, float):
#             self.__b = b
#         else:
#             print('Введите атрибут класса int или float!')
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, c):
#         if isinstance(c, int) or isinstance(c, float):
#             self.__c = c
#         print('Введите атрибут класса int или float!')
#
#     def solve(self):
#         d = self.__b ** 2 - 4 * self.__a * self.__c
#         if d > 0:
#             return f'x1 = {(-self.__b + d ** 0.5) / (2 * self.__a)} ' \
#                    f'x2 = {(-self.__b - d ** 0.5) / (2 * self.__a)}'
#         elif d == 0:
#             return f'x = {-self.__b / (2 * self.__a)}'
#         else:
#             return 'Действ. корней нет!'
#
# u1 = Kvadr_urav(1, 2, 3)
# print(u1.solve())
# u2 = Kvadr_urav(1, 2, 1)
# print(u2.solve())
# u3 = Kvadr_urav(2, 5, 3)
# print(u3.solve())

# '''
# # Создать класс "Кошка" с закрытыми атрибутами "имя", "возраст" и "вес".
# # Реализовать методы для установки значений этих атрибутов,
# # а также методы для получения значений этих атрибутов.
# # '''
#
# class Cat:
#
#     def __init__(self, name='', age=0, weight=0):
#         self.__name = name
#         self.__age = age
#         self.__weight = weight
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if isinstance(age, int):
#             self.__age = age
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         if isinstance(weight, int) or isinstance(weight, float):
#             self.__weight = weight
#         else:
#             print('Введите атрибут класса str!')
#
# cat1 = Cat()
# print(cat1.name, cat1.age, cat1.weight)
# cat1.name = 'Мурзик'
# cat1.age = 3
# cat1.weight = 4.5
# print(cat1.name, cat1.age, cat1.weight)

# # Создайте класс "Книга", который будет иметь следующие атрибуты и методы:
# # Атрибуты:
# # Название книги (строка)
# # Автор книги (строка)
# # Жанр книги (строка)
# # Количество страниц (целое число)
# # Читается ли книга (логическое значение, по умолчанию False)
# # Методы:
# # `start_reading()`: метод, который изменяет значение атрибута "читается ли книга" на True и выводит сообщение "Начал чтение книги: [название книги]".
# # `finish_reading()`: метод, который изменяет значение атрибута "читается ли книга" на False и выводит сообщение "Закончил чтение книги: [название книги]".
# # `show_info()`: метод, который выводит информацию о книге
#
# class Book:
#
#     def __init__(self, name='', author='', genre='', pages=0, reading=False):
#         self.__name = name
#         self.__author = author
#         self.__genre = genre
#         self.__pages = pages
#         self.__reading = reading
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def author(self):
#         return self.__author
#
#     @author.setter
#     def author(self, author):
#         if isinstance(author, str):
#             self.__author = author
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def genre(self):
#         return self.__genre
#
#     @genre.setter
#     def genre(self, genre):
#         if isinstance(genre, str):
#             self.__genre = genre
#         else:
#             print('Введите атрибут класса str!')
#
#     @property
#     def pages(self):
#         return self.__pages
#
#     @pages.setter
#     def genre(self, pages):
#         if isinstance(pages, int):
#             self.__pages = pages
#         else:
#             print('Введите атрибут класса int!')
#
#     @property
#     def reading(self):
#         return self.__reading
#
#     @reading.setter
#     def reading(self, reading):
#         if isinstance(reading, bool):
#             self.__reading = reading
#         else:
#             print('Введите атрибут класса bool!')
#
#     def start_reading(self):
#         self.__reading = True
#         print(f'Начал чтение книги: {self.__name}')
#
#     def finish_reading(self):
#         self.__reading = False
#         print(f'Закончил чтение книги: {self.__name}')
#
#     def show_info(self):
#         print(f'Название: {self.__name}')
#         print(f'Автор: {self.__author}')
#         print(f'Жанр: {self.__genre}')
#         print(f'Количество страниц: {self.__pages}')
#         print(f'Читается ли: {self.__reading}')


# class Person:
# #     type = 'Person'
# #     description = 'Describes a person'
# #
# #
# # print(Person.type)
# # print(Person.description)
# #
# # Person.type = 'Class Person'
# # print(Person.type)
#
# class Person:
#     type = 'Person'
#     def __init__(self, name):
#         self.name = name
#
#
# tom = Person('Tom')
# bob = Person('Bob')
# print(tom.type)
# print(bob.type)
#
# Person.type = 'Class Person'
# print(tom.type)
# print(bob.type)


# # class Person:
# #     default_name = 'Undefined'
# #
# #     def __init__(self, name):
# #         if name:
# #             self.name = name
# #         else:
# #             self.name = Person.default_name
# #
# #
# # tom = Person('Tom')
# # bob = Person('')
# # print(tom.name)
# # print(bob.name)
#
# class Person:
#     name = "Undefined"
#
#     def print_name(self):
#         print(self.name)
#
#
# tom = Person()
# bob = Person()
# tom.print_name()
# bob.print_name()
#
# bob.name = "Bob"
# bob.print_name()
# tom.print_name()

# class Person:
#     __type = 'Person'
#
#     @staticmethod
#     def print_type():
#         print(Person.__type)
#
# Person.print_type()
#
# tom = Person()
# tom.print_type()

# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def display_info(self):
# #         print(f'Name: {self.name} Age: {self.age}')
# #
# #
# # tom = Person('Tom', 21)
# # print(tom)
# # print(tom.display_info())
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(f'Name: {self.name} Age: {self.age}')
#
#     def __str__(self):
#         return f'Name: {self.name} Age: {self.age}'
#
#
# tom = Person('Tom', 21)
# print(tom)
# print(tom.display_info())

# Сложение
#
# a + b
#
# __add__(a, b)
#
# Объединение
#
# seq1 + seq2
#
# __concat__(seq1, seq2)
#
# Проверка наличия
#
# obj in seq
#
# __contains__(seq, obj)
#
# Деление
#
# a / b
#
# __truediv__(a, b)
#
# Деление
#
# a // b
#
# __floordiv__(a, b)
#
# Поразрядное И
#
# a & b
#
# __and__(a, b)
#
# Поразрядное XOR
#
# a ^ b
#
# __xor__(a, b)
#
# Поразрядная инверсия
#
# ~ a
#
# __invert__(a)
#
# Поразрядное ИЛИ
#
# a | b
#
# __or__(a, b)
#
# Степень
#
# a ** b
#
# __pow__(a, b)
#
# Присвоение по индексу
#
# obj[k] = v
#
# __setitem__(obj, k, v)
#
# Удаление по индексу
#
# del obj[k]
#
# __delitem__(obj, k)
#
# Обращение по индексу
#
# obj[k]
#
# __getitem__(obj, k)
#
# Сдвиг влево
#
# a << b
#
# __lshift__(a, b)
#
# Остаток от деления
#
# a % b
#
# __mod__(a, b)
#
# Умножение
#
# a * b
#
# __mul__(a, b)
#
# Умножение матриц
#
# a @ b
#
# __matmul__(a, b)
#
# Арифметическое отрицание
#
# -a
#
# __neg__(a)
#
# Логическое отрицание
#
# not a
#
# __not__(a)
#
# Положительное значение
#
# +a
#
# __pos__(a)
#
# Сдвиг вправо
#
# a >> b
#
# __rshift__(a, b)
#
# Установка диапазона
#
# seq[i:j] = values
#
# __setitem__(seq, slice(i, j), values)
#
# Удаление диапазона
#
# del seq[i:j]
#
# __delitem__(seq, slice(i, j))
#
# Получение диапазона
#
# seq[i:j]
#
# __getitem__(seq, slice(i, j))
#
# Вычитание
#
# a - b
#
# __sub__(a, b)
#
# Проверка на Truе/False
#
# obj
#
# __bool__(obj)
#
# Меньше чем
#
# a < b
#
# __lt__(a, b)
#
# Меньше чем или равно
#
# a <= b
#
# __le__(a, b)
#
# Равенство
#
# a==b
#
# __eq__(a, b)
#
# Неравенство
#
# a != b
#
# __ne__(a, b)
#
# Больше чем или равно
#
# a >= b
#
# __ge__(a, b)
#
# Больше чем
#
# a > b
#
# __gt__(a, b)
#
# Сложение с присваиванием
#
# a += b
#
# __iadd__(a, b)
#
# Объединение с присваиванием
#
# a += b
#
# __iconcat__(a, b)
#
# Поразрядное умножение с присваиванием
#
# a &= b
#
# __iand__(a, b)
#
# Деление с присваиванием
#
# a //= b
#
# __ifloordiv__(a, b)
#
# Сдвиг влево с присваиванием
#
# a <<= b
#
# __ilshift__(a, b)
#
# Сдвиг вправо с присваиванием
#
# a >>= b
#
# __irshift__(a, b)
#
# Деление по модулю с присваиванием
#
# a %= b
#
# __imod__(a, b)
#
# Умножение с присваиванием
#
# a += b
#
# __imul__(a, b)
#
# Умножение матриц с присваиванием
#
# a @= b
#
# __imatmul__(a, b)
#
# Поразрядное сложение с присваиванием
#
# a |= b
#
# __ior__(a, b)
#
# Возведение в степень с присваиванием
#
# a **= b
#
# __ipow__(a, b)
#
# Вычитание с присваиванием
#
# a -= b
#
# __isub__(a, b)
#
# Деление с присваиванием
#
# a /= b
#
# __itruediv__(a, b)
#
# Операция XOR с присваиванием
#
# a ^= b
#
# __ixor__(a, b)

# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     # переопределение оператора сложения
#     def __add__(self, other):
#         return Counter(self.value + other.value)
#
#
# counter1 = Counter(5)
# counter2 = Counter(15)
# counter3 = counter1 + counter2
# print(counter3.value)  # 20

# # class Counter:
# #     def __init__(self, value):
# #         self.value = value
# #
# #     def __add__(self, other):
# #         return Counter(self.value + other)
# #
# #
# # counter1 = Counter(5)
# # counter3 = counter1 + 6
# # print(counter3.value)  # 11
#
# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return self.value + other
#
#
# counter1 = Counter(5)
# result = counter1 + 7
# print(result)  # 12

# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     def __bool__(self):
#         return self.value > 0
#
#
# def test(counter):
#     if counter:
#         print("Counter = True")
#     else:
#         print("Counter = False")
#
#
# counter1 = Counter(3)
# test(counter1)  # Counter = True
#
# counter2 = Counter(-3)
# test(counter2)  # Counter = False

# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     def __bool__(self):
#         return self.value > 0
#
#
# counter1 = Counter(3)
#
# while (counter1):
#     print("Counter1: ", counter1.value)
#     counter1.value -= 1

# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     def __gt__(self, other):
#         return self.value > other.value
#
#     def __lt__(self, other):
#         return self.value < other.value
#
#
# counter1 = Counter(1)
# counter2 = Counter(2)
#
# if counter1 > counter2:
#     print("counter1 больше чем counter2")
# elif counter1 < counter2:
#     print("counter1 меньше чем counter2")
# else:
#     print("counter1 и counter2 равны")

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def __getitem__(self, prop):
#         if prop == "name":
#             return self.__name
#         elif prop == "age":
#             return self.__age
#         return None
#
#
# tom = Person("Tom", 39)
#
# print("Name:", tom["name"])  # Name: Tom
# print("Age:", tom["age"])  # Age: 39
# print("Id:", tom["id"])  # Id: None


# # import abc
#
#
# # class Shape(abc.ABC):
# #     pass
#
# # class Shape(abc.ABC):
# #     @abc.abstractmethod
# #     def area(self): pass
#
# # class Shape(abc.ABC):
# #
# #     @abc.abstractmethod
# #     def area(self): pass
# #
# # # shape = Shape()
# # # print(shape)
# #
# # class Rectangle(Shape):
# #
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
# #
# #     def area(self): return self.width * self.height
# #
# # rect = Rectangle(30, 50)
# # print(f'Rectangle area: {rect.area()}')
#
# import abc
# from math import pi
#
#
# class Shape(abc.ABC):
#
#     @abc.abstractmethod
#     def area(self): pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self): return self.width * self.height
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self): return pi * self.radius * self.radius
#
#
# def print_area(shape):
#     print(f'Area: {round(shape.area(), 2)}')
#
# rect = Rectangle(30, 50)
# circle = Circle(30)
# print_area(rect)
# print_area(circle)

# import abc


# class Shape(abc.ABC):
#     pass

# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area(self): pass

# class Shape(abc.ABC):
#
#     @abc.abstractmethod
#     def area(self): pass
#
# # shape = Shape()
# # print(shape)
#
# class Rectangle(Shape):
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self): return self.width * self.height
#
# rect = Rectangle(30, 50)
# print(f'Rectangle area: {rect.area()}')

# # # Создайте класс Vector, который представляет вектор и определите в нем операторы сложения и вычитания.
# # # Для сложения векторов применяется формула a + b = {ax + bx; ay + by}, а для вычитания a - b = {ax - bx; ay - by}
#
# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __str__(self):
#         return f'X = {self.x} Y = {self.y}'
#
#
# v1 = Vector(3, 5)
# v2 = Vector(1, 1)
#
# v3 = v1 + v2
# print(v3)
#
# v4 = v1 - v2
# print(v4)

# import abc
# from math import pi
#
#
# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area(self): pass
#
# # shape = Shape()
# # print(shape)
#
# class Rectangle(Shape):
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self): return self.width * self.height
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self): return pi * self.radius ** 2
#
#
# def print_area(shape):
#     print(f'Area: {round(shape.area(), 2)}')
#
# # rect = Rectangle(30, 50)
# # print(f'Rectangle area = {rect.area()}')
#
# rect = Rectangle(30, 50)
# circle = Circle(30)
# print_area(rect)
# print_area(circle)

# import abc
#
#
# class Shape(abc.ABC):
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @abc.abstractmethod
#     def area(self): pass
#
#     def print_point(self):
#         print(f'X: {self.x} \tY: {self.y}')
#
# class Rectangle(Shape):
#
#     def __init__(self, x ,y, width, height):
#         super().__init__(x, y)
#         self.width = width
#         self.height = height
#
#     def area(self): return self.width * self.height
#
#
# rect = Rectangle(10, 20, 100, 100)
# rect.print_point()


# s = '5'
# num = int(s)
# print(num)

# s = 'hello'
# num = int(s)
# print(num)

# s = input('Введите число: ')
# num = int(s)
# print(num)

# try:
#     инструкции
# except [тип_исключения]:
#     инструкции

# try:
#     num = int(input('Введите число: '))
#     print(f'Введено число {num}')
# except:
#     print('Преобразование прошло неудачно')
# print('Завершение программы')

# try:
#     num = int(input('Введите число: '))
#     print(f'Введено число: {num}')
# except:
#     print('Преобразование прошло неудачно')
# finally:
#     print('Блок try завершил выполнение')
# print('Заврешение программы')

# try:
#     num = 3 / 0
#     print(num)
# finally:
#     print('Блок try завершил выполение')
# print('Завершение программы')


# try:
#     num = int(input('Введите число: '))
#     print(f'Введено число: {num}')
# except ValueError:
#     print('Преобразование прошло неудачно')
# print('Завершение программы')

# BaseException
# Exception
# ArithmeticError
# BufferError
# LookupError

# https://docs.python.org/3/library/exceptions.html

# IndexError
# KeyError
# OverflowError
# RecursionError
# TypeError
# ValueError
# ZeroDivisionError
# NotImplementedError
# ModuleNotFoundError
# OSError

# try:
#     num1 = int(input('Введите число1: '))
#     num2 = int(input('Введите число2: '))
#     print(f'Результат деления: {num1 / num2}')
# except ValueError:
#     print('Преобразование прошло неудачно')
# except ZeroDivisionError:
#     print('Попытка деления на ноль')
# except BaseException:
#     print('Общее исключение')
# print('Завершение программы')

# try:
#     num1 = int(input('Введите число1: '))
#     num2 = int(input('Введите число2: '))
#     print(f'Результат деления: {num1 / num2}')
# except ZeroDivisionError:
#     print('Попытка деления на ноль')
# print('Завершение программы')

# try:
#     num1 = int(input('Введите число1: '))
#     num2 = int(input('Введите число2: '))
#     print(f'Результат деления: {num1 / num2}')
# except (ZeroDivisionError, ValueError):
#     print('Попытка деления на ноль')
# print('Завершение программы')

# try:
#     num = int(input('Введите число: '))
#     print(f'Введенное число: {num}')
# except ValueError as ex:
#     print(f'Сведения об исключении: {ex}')
# print('Завершение программы')

# try:
#     age = int(input('Введите возраст: '))
#     if age > 150 or age < 1:
#         raise Exception('Некорректный возраст')
#     print(f'Ваш возраст: {age}')
# except ValueError:
#     print('Введены некорректные данные')
# except Exception as ex:
#     print(ex)
# print('Завершение программы')

# class PersonAgeException(Exception):
#
#     def __init__(self, age, minage, maxage):
#         self.age = age
#         self.minage = minage
#         self.maxage = maxage
#
#     def __str__(self):
#         return f'Недопустимое значение: {self.age}.\n' \
#                f'Возраст должен быть в диапазоне от {self.minage} до {self.maxage}'
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         minage, maxage = 1, 150
#         if minage < age < maxage:
#             self.__age = age
#         else:
#             raise PersonAgeException(age, minage, maxage)
#
#     def display_info(self):
#         print(f'Имя: {self.__name} Возраст: {self.__age}')
#
# try:
#     tom = Person('Tom', 25)
#     tom.display_info()
#
#     oleg = Person('Олег', 20)
#     oleg.display_info()
#
#     bob = Person('Bob', 200)
#     bob.display_info()
# except PersonAgeException as ex:
#     print(ex)

# '''
# Садовник и помидоры
# Классовая структура
# Необходимо создать следующую классовую структуру:
#
# Есть Помидор со следующими характеристиками:
# 1. Индекс
# 2. Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
# Помидор может:
# 1. Расти (переходить на следующую стадию созревания)
# 2. Предоставлять информацию о своей зрелости
# Есть Куст с помидорами, который:
# 1. Содержит список томатов, которые на нем растут
# И может:
# 1. Расти вместе с томатами
# 2. Предоставлять информацию о зрелости всех томатов
# 3. Предоставлять урожай
# И также есть Садовник, который имеет:
# 1. Имя
# 2. Растение, за которым он ухаживает
# И может:
# 1. Ухаживать за растением
# 2. Собирать с него урожай
#
# Задание
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет
# создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается параметром,
# является публичным и 2) _plant - принимает объект класса TomatoBush, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
# '''

# class Tomato:
#
#     states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}
#
#     def __init__(self, index):
#         self._index = index
#         self._state = self.states['Отсутствует']
#
#     def grow(self):
#         if self._state < 3:
#             self._state += 1
#
#     def is_ripe(self):
#         return self._state == 3
#
# class TomatoBush:
#
#     def __init__(self, num_tomatoes):
#         self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     def give_away_all(self):
#         self.tomatoes = []
#
# class Gardener:
#
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         self._plant.grow_all()
#
#     def harvest(self):
#         if self._plant.all_are_ripe():
#             print('Урожай собран!')
#             self._plant.give_away_all()
#         else:
#             print('Томаты еще не дозрели!')
#
#     @staticmethod
#     def knowledge_base():
#         print('Справка по садоводству')
#         print('1. Не забывайте регулярно поливать и подкармливать растения')
#         print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу расти')
#         print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней')
#
# Gardener.knowledge_base()
#
# bush = TomatoBush(5)
# gardener = Gardener('Василий', bush)
#
# gardener.work()
# gardener.work()
# gardener.work()
# gardener.harvest()


# # Класс DeckOfCards содержит список карт. Конструктор класса Card инициализирует
# # значения масти и номера из списков NumsList и MastList, которые объявлены как общие
# # атрибуты класса.
#
#
# import random
#
#
# class Card:
#
#     NumsList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#     MastList = ['Пики', 'Крести', 'Буби', 'Черви']
#
#     def __init__(self, i, j):
#         self.mast = Card.MastList[i - 1]
#         self.num = Card.NumsList[j - 1]
#
# class DeckOfCards:
#
#     def __init__(self):
#         self.deck = []
#         for i in range(1, 5):
#             for j in range(1, 15):
#                 self.deck.append(Card(i, j))
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#
#     def get(self, i):
#         if 0 <= i < len(self.deck):
#             answer = self.deck[i].num
#             answer += f' {self.deck[i].mast}'
#         else:
#             answer = 'Нет такой карты'
#         return answer
#
# deck = DeckOfCards()
# deck.shuffle()
# n = int(input('Выберите номер карты: '))
# print(deck.get(n - 1))

# # Пусть необходимо разработать виртуальную модель процесса обучения. В программе
# # должны быть объекты-ученики, учитель, кладезь знаний.
# # Потребуется три класса – "учитель", "ученик", "данные". Учитель и ученик во многом
# # похожи, оба – люди. Значит, их классы могут принадлежать одному надклассу "человек".
# # Однако в контексте данной задачи у учителя и ученика вряд ли найдутся общие атрибуты.
# # Определим, что должны уметь объекты для решения задачи "увеличить знания":
# # • Ученик должен уметь брать информацию и превращать ее в свои знания.
# # • Учитель должен уметь учить группу учеников.
# # • Данные могут представлять собой список знаний. Элементы будут извлекаться по
# # индексу.
#
#
# class Data:
#
#     def __init__(self, info):
#         self.info = list(info)
#
#     def __getitem__(self, i):
#         return self.info[i]
#
# class Teacher:
#
#     def __init__(self):
#         self.work = 0
#
#     def teach(self, info, pupil):
#         for i in pupil:
#             i.take(info)
#             self.work += 1
#
# class Pupil:
#
#     def __init__(self):
#         self.knowledge = []
#
#     def take(self, info):
#         self.knowledge.append(info)
#
# lesson = Data(['класс', 'объект', 'наследование', 'инкапсуляция'])
# maria = Teacher()
# tom = Pupil()
# bob = Pupil()
# maria.teach(lesson[2], [tom, bob])
# maria.teach(lesson[1], [tom])
# print(tom.knowledge)
# print(bob.knowledge)
#




# from abc import ABC, abstractmethod
#
#
# class AbstractTovar(ABC):
#     @abstractmethod
#     def print_menu():
#         pass
#
#
# class Tovar(AbstractTovar):
#
#     def __init__(self, name, price, choose=False):
#         self.name = name
#         self.price = price
#         self.choose = choose
#
#     def print_menu():
#         print('\nВыберите действие:')
#         print('(1) Показать прайс-лист')
#         print('(2) Выбрать товар')
#         print('(3) Напечатать чек')
#         print('(0) Выход')
#
#
# goods = ['Гвозди', 'Шурупы', 'Болты',
#          'Рубанок', 'Шуруповерт', 'Молоток',
#          'Отвертка', 'Пила', 'Нож',
#          'Розетка', 'Удлинитель', 'Кварц',
#          'Паяльник', 'Плоскогубцы', 'Перфоратор']
# price = [100, 150, 200,
#          500, 600, 550,
#          1000, 1200, 800,
#          400, 350, 300,
#          100, 200, 2000]
#
# tovar_list = []
# for j in goods:
#     tovar_list.append(Tovar(j, price[goods.index(j)]))
#
# Tovar.print_menu()
#
# items_in_page = 5
# menu = 99
# while menu != 0:
#     try:
#         menu = int(input(': '))
#         if menu == 1:
#             print('-------Прайс-лист-------')
#             for i in range(len(tovar_list) // items_in_page + 1):
#                 print(f'------Лист {i + 1}------')
#                 for j in range(i * items_in_page, i * items_in_page + items_in_page):
#                     if j < len(tovar_list):
#                         print(f'Товар: {tovar_list[j].name}, цена: {tovar_list[j].price}')
#             Tovar.print_menu()
#         if menu == 2:
#             print('Выберете товар, указав его название\n')
#             try:
#                 ch = input(': ').lower()
#                 for o in tovar_list:
#                     if o.name.lower() == ch:
#                         o.choose = True
#             except:
#                 print('Введите название одного товара, как в прайсе\n')
#             Tovar.print_menu()
#         if menu == 3:
#             total = 0
#             for o in tovar_list:
#                 if o.choose:
#                     total += o.price
#             print('\n-------Чек-------\n')
#             for o in tovar_list:
#                 if o.choose:
#                     print(f'{o.name} --- {o.price}')
#             print('')
#             print(f'Итого: {total}')
#             print('\n-------Чек-------\n')
#             Tovar.print_menu()
#     except Exception as e:
#         print('error', e)


# from random import randint
# from time import sleep
#
#
# hangman = (
#     """
#      ------
#      |    |
#      |
#      |
#      |
#      |
#      |
#     ----------
#     """,
#     """
#      ------
#      |    |
#      |    O
#      |
#      |
#      |
#      |
#     ----------
#     """,
#     """
#      ------
#      |    |
#      |    O
#      |    |
#      |    |
#      |
#      |
#     ----------
#     """,
#     """
#      ------
#      |    |
#      |    O
#      |   /|
#      |    |
#      |
#      |
#     ----------
#     """,
#     """
#      ------
#      |    |
#      |    O
#      |   /|\\
#      |    |
#      |
#      |
#     ----------
#     """,
#     """
#      ------
#      |    |
#      |    O
#      |   /|\\
#      |    |
#      |   /
#      |
#     ----------
#     """,
#     """
#      ------
#      |    |
#      |    O
#      |   /|\\
#      |    |
#      |   / \\
#      |
#     ----------
#     """
# )
#
# class LengthError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
# class NotText(Exception):
#     def __init_(self, message):
#         super().__init__(message)
#
# error_message = "Exception occured"
#
# def trigger_exceptions(text):
#     if len(text) != 1:
#         raise LengthError(error_message)
#     if text not in 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
#         raise NotText(error_message)
#
# words = ['ЭЛЕКТРИФИКАЦИЯ', 'КАМЕНЬ', 'СПОРТ', 'КОСМОС', 'КОНДИТЕР', 'ПРОПЕЛЛЕР', 'БАЛЬЗАМ', 'ФЛОРА']
#
# chosen_word = words[randint(0, (len(words) - 1))]
#
# max_wrong_guesses = 6
#
# guessed_word = '-' * len(chosen_word)
# wrong_guesses = 0
# used_letters = []
#
# while wrong_guesses < max_wrong_guesses and guessed_word != chosen_word:
#     print(hangman[wrong_guesses])
#     print('Использованные буквы', used_letters)
#     print(guessed_word, '\n')
#
#     guess = input('Введите букву: ')
#
#     while guess.upper() in used_letters:
#         print('Вы уже вводили данную букву')
#         guess = input('Введите букву: ')
#
#     try:
#         trigger_exceptions(guess)
#         used_letters.append(guess.upper())
#         if guess.upper() in chosen_word:
#             print('Правильно, буква', guess, 'есть в слове')
#             update = ''
#             for i in range(0, len(chosen_word)):
#                 if guess.upper() == chosen_word[i]:
#                     update += guess.upper()
#                 else:
#                     update += guessed_word[i]
#             guessed_word = update
#
#         else:
#             wrong_guesses += 1
#             print('Неверно, буквы', guess, 'нет в слове')
#     except LengthError:
#         print('Ваш запрос длиннее 1 символа')
#         sleep(1)
#     except NotText:
#         print('Ваш запрос не является буквой или введён на другом языке')
#         sleep(1)
#
# if wrong_guesses == max_wrong_guesses:
#     print(hangman[6])
#     print('Вы проиграли!')
# else:
#     print('\n', 'Вы выиграли!')
#
# print('Слово-загадка:', chosen_word)

#
# import random
#
# def parse_questions(file_path):
#     questions = []
#     answers = []
#     correct_answers = []
#
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#
#     for i in range(0, len(lines), 6):
#         question = lines[i].strip()
#         option1 = lines[i + 1].strip()
#         option2 = lines[i + 2].strip()
#         option3 = lines[i + 3].strip()
#         option4 = lines[i + 4].strip()
#         correct_answer = int(lines[i + 5].strip())
#
#         questions.append(question)
#         answers.append([option1, option2, option3, option4])
#         correct_answers.append(correct_answer)
#
#     return questions, answers, correct_answers
#
# def play_quiz(questions, answers, correct_answers):
#     score = 0
#
#     for i in random.sample(range(len(questions)), len(questions)):
#         print(questions[i])
#         for j, option in enumerate(answers[i]):
#             print(f'{j + 1}. {option}')
#
#         user_answer = int(input('Введите номер правильного ответа: '))
#
#         if user_answer == correct_answers[i]:
#             score += 1
#
#     print(f'Вы набрали {score} баллов из {len(questions)}')
#
# if __name__ == '__main__':
#     questions, answers, correct_answers = parse_questions('questions.txt')
#     play_quiz(questions, answers, correct_answers)


# # '''
# # Простой класс, представляющий рациональную дробь (num – числитель, den –
# # знаменатель). Класс содержит конструктор и перегруженные методы умножения и деления
# # (дроби на дробь и дроби на целое число). Метод создания случайной дроби из заданного
# # диапазона целых чисел объявлен как статический.
# # '''
#
# from math import gcd
# from random import randint
#
#
# class MyFraction:
#
#     def __init__(self, num, den):
#         if num != 0 and den != 0:
#             k = gcd(num, den)
#             self.num = num // k
#             self.den = den // k
#         else:
#             raise ValueError('Числитель и знаменатель не могут быть равны нулю')
#
#     @staticmethod
#     def generate(num_min, num_max, den_min, den_max):
#         num = randint(num_min, num_max)
#         den = randint(den_min, den_max)
#         return MyFraction(num, den)
#
#     def __str__(self):
#         return f'{self.num}/{self.den}'
#
#     def __mul__(self, other):
#         if isinstance(other, MyFraction):
#             return MyFraction(self.num * other.num, self.den * other.den)
#         elif isinstance(other, int):
#             return MyFraction(self.num * other, self.den)
#         else:
#             raise TypeError('Можно умножать только на дробь или целое число')
#
#     def __truediv__(self, other):
#         if isinstance(other, MyFraction):
#             return MyFraction(self.num * other.den, self.den * other.num)
#         elif isinstance(other, int):
#             return MyFraction(self.num, self.den * other)
#         else:
#             raise TypeError('Можно делить только на дробь или целое число')
#
# a = [MyFraction.generate(1, 9, 2, 9) for i in range(3)]
# for f in a:
#     b = MyFraction.generate(1, 9, 2, 9)
#     cm = f * b
#     print(f'{f} * {b} = {cm}')
#     cd = f / b
#     print(f'{f} / {b} = {cd}')
#     n = randint(1, 9)
#     cm = f * n
#     print(f'{f} * {n} = {cm}')
#     cd = f / n
#     print(f'{f} / {n} = {cd}')


# # # Класс Student содержит имя студента full_name, номер группы group_number и список
# # # полученных оценок progress. В программе вводится список студентов. Далее список
# # # сортируется по имени, потом выводятся студенты, имеющие неудовлетворительные
# # # оценки.
#
# class Student:
#
#     def __init__(self, full_name='', group_number=0, progress=[]):
#         self.full_name = full_name
#         self.group_number = group_number
#         self.progress = progress
#
#     def __str__(self):
#         txt = f'Студент: {self.full_name} Группа: {self.group_number}'
#         txt += ' Оценки:'
#         for i in self.progress:
#             txt += f' {i}'
#         return txt
#
# def SortParam(st):
#     return st.full_name
#
# st_size = 3
# students = []
#
# for i in range(st_size):
#     full_name = input('Введите имя студента: ').strip()
#     group_number = input('Введите номер группы: ').strip()
#     n = 3
#     print(f'Введите {n} оценок в столбик: ')
#     progress = []
#     for i in range(n):
#         progress.append(int(input('Оценка: ')))
#     st = Student(full_name, group_number, progress)
#     students.append(st)
#
# print('Список студентов:')
# for st in students:
#     print(st)
# print()
#
# students.sort(key=SortParam)
#
# print('Сортировка по имени:')
# for st in students:
#     print(st)
# print()
#
# print('Студенты, имеющие неудовлетворительные оценки:')
# k = 0
# for st in students:
#     for i in st.progress:
#         if i < 3:
#             print(st)
#             k += 1
#             break
# if k == 0:
#     print('Нет студентов с неудовлетворительными оценками')


# # '''
# # В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
# # уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
# # солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
# # "герой". У героев есть метод увеличения собственного уровня.
# # В основной ветке программы создается по одному герою для каждой команды. В
# # цикле генерируются объекты-солдаты. Их принадлежность команде определяется
# # случайно.
# # Солдаты разных команд добавляются в разные списки. Измеряется длина списков
# # солдат противоборствующих команд и выводится на экран. У героя, принадлежащего
# # команде с более длинным списком, увеличивается уровень.
# # Отправляем одного из солдат следовать за первым героем и выводим их
# # идентификационные номера.
# # '''
#
# from random import randint
#
#
# class Person:
#
#     count = 0
#     def __init__(self, c):
#         self.id = Person.count
#         Person.count += 1
#         self.command = c
#
# class Hero(Person):
#
#     def __init__(self, c):
#         Person.__init__(self, c)
#         self.level = 1
#
#     def up_level(self):
#         self.level += 1
#
# class Soldier(Person):
#
#     def __init__(self, c):
#         Person.__init__(self, c)
#         self.my_hero = None
#
#     def follow(self, hero):
#         self.my_hero = hero.id
#
# h1 = Hero(1)
# h2 = Hero(2)
# army1 = []
# army2 = []
# for i in range(21):
#     if randint(1, 2) == 1:
#         s = Soldier(1)
#         army1.append(s)
#     else:
#         s = Soldier(2)
#         army2.append(s)
# print(f'Армия 1: {len(army1)}, Армия 2: {len(army2)}')
# if len(army1) > len(army2):
#     h1.up_level()
# elif len(army1) < len(army2):
#     h2.up_level()
# print(f'Герой 1 уровень: {h1.level}, Герой 2 уровень: {h2.level}')
# army1[0].follow(h1)
# print(f'ID солдата 1: {army1[0].id} ID героя 1: {h1.id}')


# # # В классе Battle реализована композиция: он включает два объекта типа Soldier.
#
# from random import randint
#
# class Soldier:
#
#     def __init__(self, name='NoName', health=100):
#         self.name = name
#         self.health = health
#
#     def set_name(self, name):
#         self.name = name
#
#     def make_kick(self, enemy):
#         enemy.health -= 20
#         if enemy.health < 0:
#             enemy.health = 0
#         self.health += 10
#         print(f'{self.name} бьет {enemy.name}')
#         print(f'{self.name} = {self.health}')
#         print(f'{enemy.name} = {enemy.health}')
#
# class Battle:
#
#     def __init__(self, u1, u2):
#         self.u1 = u1
#         self.u2 = u2
#         self.result = 'Сражения не было'
#
#     def battle(self):
#         while self.u1.health > 0 and self.u2.health > 0:
#             if randint(1, 2) == 1:
#                 self.u1.make_kick(self.u2)
#             else:
#                 self.u2.make_kick(self.u1)
#         if self.u1.health > self.u2.health:
#             self.result = f'Победил {self.u1.name}'
#         elif self.u1.health < self.u2.health:
#             self.result = f'Победил {self.u2.name}'
#
#     def who_win(self):
#         return self.result
#
# u1 = Soldier('Василий', 140)
# u2 = Soldier()
# u2.set_name('Петр')
# b = Battle(u1, u2)
# b.battle()
# print(b.who_win())

# '''
# Класс ForeignPassport является производным от класса Passport. Метод PrintInfo
# существует в обоих классах. PassportList представляет собой список, содержащий объекты
# обоих классов. Вызов метода PrintInfo для каждого элемента списка демонстрирует его
# полиморфное поведение
# '''
# import requests
#
# class Passport:
#
#     def __init__(self, first_name, last_name, country, date_of_birth, passport_number):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.date_of_birth = date_of_birth
#         self.passport_number = passport_number
#
#     def PrintInfo(self):
#         print(f'Полное имя: {self.first_name} {self.last_name}')
#         print(f'Страна: {self.country}')
#         print(f'Дата рождения: {self.date_of_birth}')
#         print(f'Номер паспорта: {self.passport_number}')
#
# class ForeignPassport(Passport):
#
#     def __init__(self, first_name, last_name, country, date_of_birth, passport_number, visa):
#         Passport.__init__(self, first_name, last_name, country, date_of_birth, passport_number)
#         self.visa = visa
#
#     def PintInfo(self):
#         Passport.PrintInfo(self)
#         if hasattr(self, 'visa'):
#             print(f'Виза: {self.visa}')
#
#
# PassportList = []
# for i in range(5):
#     response = requests.get('https://randomuser.me/api/')
#     data = response.json()
#     PassportList.append(Passport(data['results'][0]['name']['first'],
#     data['results'][0]['name']['last'],
#     data['results'][0]['location']['country'],
#     data['results'][0]['dob']['date'],
#     data['results'][0]['id']['value']))
#
# for emp in PassportList:
#     emp.PrintInfo()


# # # Классы Printer, Scaner и Xerox являются производными от класса Equipment. Метод
# # # str() перегружен только в классе Printer, для остальных используется метод из базового
# # # класса. Метод action() перегружен для всех производных классов. Вызов этих методов для
# # # каждого элемента списка демонстрирует их полиморфное поведение.
#
# class Equipment:
#
#     def __init__(self, name, make, year):
#         self.name = name
#         self.make = make
#         self.year = year
#
#     def action(self):
#         return 'не определено'
#
#     def __str__(self):
#         return f'Производитель: {self.name} Модель: {self.make} Годд выпуска: {self.year}'
#
# class Printer(Equipment):
#
#     def __init__(self, name, make, year, series):
#         super().__init__(name, make, year)
#         self.series = series
#
#     def action(self):
#         return 'печатает'
#
#     def __str__(self):
#         return f'Производитель: {self.name} Модель: {self.make} Годд выпуска: {self.year} Серия: {self.series}'
#
# class Scaner(Equipment):
#
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'сканирует'
#
# class Xerox(Equipment):
#
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'копирует'
#
#
# sklad = []
# scaner = Scaner('Mustek', 'BearPow 1200CU', 2019)
# sklad.append(scaner)
# xerox = Xerox('Xerox', 'Phaser 3120', 2020)
# sklad.append(xerox)
# printer = Printer('HP', 'Laser Jet', 2021, '1200')
# sklad.append(printer)
# print('На складе имеются: ')
# for i in sklad:
#     print(i, i.action())
# for i in sklad:
#     if isinstance(i, Printer):
#         sklad.remove(i)
# print('На складе осталось:')
# for i in sklad:
#     print(i, i.action())

# # Программа для подсчета количества слов, строк и символов в текстовом файле.
#
# file = open('input.txt', 'r', encoding='utf-8')
# words = file.read().split()
# num_words = len(words)
# num_lines = sum(1 for line in open('input.txt'))
# num_chars = sum(len(word) for word in words)
# print(f'words: {num_words}')
# print(f'lines: {num_lines}')
# print(f'chars: {num_chars}')

# # # Программа для сортировки строк в текстовом файле по алфавиту.
#
# file = open('input.txt', 'r', encoding='utf-8')
# lines = file.readlines()
# lines.sort()
# sorted_file = open('sorted_input.txt', 'w', encoding='utf-8')
# for line in lines:
#     sorted_file.write(line)
# file.close()
# sorted_file.close()

# # Программа для поиска определенного слова или фразы в текстовом файле
#
# file = open('input.txt', 'r', encoding='utf-8')
# search_word = input('Введите искомую строку: ')
# for line in file:
#     if search_word in line:
#         print(line.replace('\n', ''))
# file.close()

# # Программа для удаления всех чисел из текстового файла.
#
# import re
#
# file = open('input.txt', 'r', encoding='utf-8')
# text = file.read()
# clean_text = re.sub(r'\d+', '', text)
# clean_file = open('clean_input.txt', 'w', encoding='utf-8')
# clean_file.write(clean_text)
# file.close()
# clean_file.close()

# # Программа для замены определенного слова или фразы в текстовом файле на другую.
#
# file = open('input.txt', 'r', encoding='utf-8')
# text = file.read()
# re_text = text.replace('23', 'yes')
# re_file = open('re_input.txt', 'w', encoding='utf-8')
# re_file.write(re_text)
# file.close()
# re_file.close()

# # Программа для объединения нескольких текстовых файлов в один.
#
# file1 = open('file1.txt', 'r', encoding='utf-8')
# file2 = open('file2.txt', 'r', encoding='utf-8')
# comb_text = file1.read() + file2.read()
# comb_file = open('comb_file.txt', 'w', encoding='utf-8')
# comb_file.write(comb_text)
# file1.close()
# file2.close()
# comb_file.close()

# # Программа для выделения определенной информации из текстового файла (например, email адресов).
#
# import re
#
# file = open('input.txt', 'r', encoding='utf-8')
# text = file.read()
# emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
# for email in emails:
#     print(email)
# file.close()

# # Программа для подсчета частоты встречаемости слов в текстовом файле.
#
# from collections import Counter
#
# file = open('input.txt', 'r', encoding='utf-8')
# words = file.read().split()
# word_freq = Counter(words)
# for word in word_freq:
#     print(f'{word}: {word_freq[word]}')
# file.close()

# # Программа для создания нового текстового файла с уникальными словами из существующего.
#
# file = open('input.txt', 'r', encoding='utf-8')
# words = set(file.read().split())
# un_words = ' '.join(words)
# un_file = open('un_file.txt', 'w', encoding='utf-8')
# un_file.write(un_words)
# file.close()
# un_file.close()

# # Программа для шифрования текстового файла с помощью шифра Цезаря.
#
# file = open('input.txt', 'r', encoding='utf-8')
# shift = 3
# en_text = ''
# for char in file.read():
#     if char.isalpha():
#         en_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#     else:
#         en_text += char
# en_file = open('en_file.txt', 'w', encoding='utf-8')
# en_file.write(en_text)
# file.close()
# en_file.close()

# # программа для ведения базы данных Студенты
#
# menu = '''\nМеню:
# 1 - Показать список студентов
# 2 - Добавить студента
# 3 - Редактировать студента
# 4 - Удалить студента
# 0 - Выход из программы
# '''
# FILE_NAME = 'students.txt'
#
# def file_read():
#     with open(FILE_NAME, 'r', encoding='utf-8') as file:
#         print('\nСписок студентов:')
#         print(file.read())
#
# def file_readlines():
#     with open(FILE_NAME, 'r', encoding='utf-8') as file:
#         return file.readlines()
#
# def file_add(new_line):
#     with open(FILE_NAME, 'a', encoding='utf-8') as file:
#         file.write(f'\n{new_line}')
#
# key = 1
# while key != '0':
#     print(menu)
#     key = input('Введите команду: ').strip()
#     if key == '1':
#         file_read()
#     elif key == '2':
#         new_id = str(len(file_readlines()) + 1)
#         new_student = input('Введите данные о новом студенте: ').strip()
#         file_add(f'{new_id} {new_student}')
#     elif key == '3':
#         students_list = file_readlines()
#         id_student = input('Введите id студента: ').strip()
#         with open('temp_file.txt', 'w', encoding='utf-8') as temp_file:
#             for i in range(len(students_list)):
#                 if students_list[i].split()[0] == id_student:
#                     student = input('Введите новые данные: ').strip()
#                     if i != len(students_list) - 1:
#                         students_list[i] = f'{id_student} {student}\n'
#                     else:
#                         students_list[i] = f'{id_student} {student}'
#                 temp_file.write(f'{students_list[i]}')
#     elif key == '4':
#         students_list = file_readlines()
#         id_student = input('Введите id студента: ').strip()
#         k = 1
#         with open('temp_file.txt', 'w', encoding='utf-8') as temp_file:
#             for i in range(len(students_list)):
#                 if students_list[i].split()[0] != id_student:
#                     temp_file.write(f'{k} {students_list[i].split()[1]}\n')
#                     k += 1
#     else:
#         if key != '0':
#             print('Неправильная команда!')
#     if key != '0':
#         key = input('\nНажмите Enter для вывода меню либо 0 для выхода из программы: ').strip()
# print('Завершение программы!')

#
# import datetime
#
# class Doctor:
#     def __init__(self, name, max_appointments):
#         self.name = name
#         self.max_appointments = max_appointments
#         self.appointments = []
#
#     def add_appointment(self, appointment):
#         if len(self.appointments) < self.max_appointments:
#             self.appointments.append(appointment)
#             return True
#         else:
#             return False
#
# class Appointment:
#     def __init__(self, patient_name, doctor_name, date_time):
#         self.patient_name = patient_name
#         self.doctor_name = doctor_name
#         self.date_time = date_time
#
# class Schedule:
#     def __init__(self):
#         self.doctors = []
#
#     def add_doctor(self, doctor):
#         self.doctors.append(doctor)
#
#     def find_doctor(self, doctor_name):
#         for doctor in self.doctors:
#             if doctor.name == doctor_name:
#                 return doctor
#         return None
#
#     def is_available(self, doctor_name, date_time):
#         doctor = self.find_doctor(doctor_name)
#         if doctor is not None:
#             for appointment in doctor.appointments:
#                 if appointment.date_time == date_time:
#                     return False
#         return True
#
#     def make_appointment(self, patient_name, doctor_name, date_time):
#         doctor = self.find_doctor(doctor_name)
#         if doctor is not None and self.is_available(doctor_name, date_time):
#             appointment = Appointment(patient_name, doctor_name, date_time)
#             if doctor.add_appointment(appointment):
#                 return True
#         return False
#
#     def print_schedule(self):
#         for doctor in self.doctors:
#             print("Doctor:", doctor.name)
#             for appointment in doctor.appointments:
#                 print("Patient:", appointment.patient_name, "Date and Time:", appointment.date_time)
#
# # Пример использования программы
# schedule = Schedule()
#
# # Создание врачей
# doctor1 = Doctor("Doctor 1", 16)
# doctor2 = Doctor("Doctor 2", 16)
#
# # Добавление врачей в расписание
# schedule.add_doctor(doctor1)
# schedule.add_doctor(doctor2)
#
# # Запись пациентов на прием
# patient_name = input("Введите имя пациента: ")
# doctor_name = input("Введите имя врача: ")
# date_str = input("Введите дату и время приема в формате ГГГГ-ММ-ДД ЧЧ:ММ: ")
# date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
# schedule.make_appointment(patient_name, doctor_name, date_time)
#
# # Вывод расписания на экран
# schedule.print_schedule()

#
# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
#
# board = list(range(1,10))
#
# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)
#
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")
#
# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)
#
# input("Нажмите Enter для выхода!")


# import pickle
#
#
# class Task:
#     def __init__(self, name, description, priority, due_date):
#         self.name = name
#         self.description = description
#         self.priority = priority
#         self.due_date = due_date
#
# class TaskManager:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def view_tasks(self):
#         for i, task in enumerate(self.tasks, 1):
#             print(f"Задача {i}:")
#             print(f"Название: {task.name}")
#             print(f"Описание: {task.description}")
#             print(f"Приоритет: {task.priority}")
#             print(f"Дата выполнения: {task.due_date}")
#             print()
#
#     def edit_task(self, task_index, name, description, priority, due_date):
#         if 1 <= task_index <= len(self.tasks):
#             task = self.tasks[task_index - 1]
#             task.name = name
#             task.description = description
#             task.priority = priority
#             task.due_date = due_date
#             print(f"Задача {task_index} была обновлена.")
#         else:
#             print("Этой задачи не существует.")
#
#     def delete_task(self, task_index):
#         if 1 <= task_index <= len(self.tasks):
#             deleted_task = self.tasks.pop(task_index - 1)
#             print(f"Задача {task_index} была удалена.")
#         else:
#             print("Этой задачи не существует.")
#
#     def save_tasks(self, filename):
#         with open(filename, 'wb') as file:
#             pickle.dump(self.tasks, file)
#             print(f'Задачи сохранены {filename}')
#
#     def load_tasks(self, filename):
#         try:
#             with open(filename, 'rb') as file:
#                 self.tasks = pickle.load(file)
#             print(f'Задачи загружены {filename}')
#         except FileNotFoundError:
#             print(f'Файл {filename} не найден.')
#
# def main():
#     task_manager = TaskManager()
#
#     while True:
#         print("Task Manager Menu:")
#         print("1. Добавить задачу")
#         print("2. Посмотреть задачи")
#         print("3. Редактировать задачи")
#         print("4. Удалить задачу")
#         print("5. Сохранить задачу")
#         print("6. Загрузить задачу")
#         print("7. Выход")
#
#         choice = input("Введите свой выбор: ")
#
#         if choice == "1":
#             name = input("Название: ")
#             description = input("Описание: ")
#             priority = input("Приоритет задачи: ")
#             due_date = input("Срок выполнения: ")
#             task = Task(name, description, priority, due_date)
#             task_manager.add_task(task)
#             print("Задача была успешно добавлена.")
#         elif choice == "2":
#             task_manager.view_tasks()
#         elif choice == "3":
#             task_index = int(input("Введите номер задачи которую хотите редактировать: "))
#             name = input("Новое имя задачи: ")
#             description = input("Новое описание задачи: ")
#             priority = input("Новый приоритет задачи: ")
#             due_date = input("Новый срок выполнения: ")
#             task_manager.edit_task(task_index, name, description, priority, due_date)
#         elif choice == "4":
#             task_index = int(input("Введите номер задачи, которую хотите удалить: "))
#             task_manager.delete_task(task_index)
#         elif choice == "5":
#             filename = input("Введите имя файла чтобы сохранить задачу: ")
#             task_manager.save_tasks(filename)
#         elif choice == "6":
#             filename = input("Введите имя файла чтобы загрузить задачу: ")
#             task_manager.load_tasks(filename)
#         elif choice == "7":
#             print("Выход из Task Manager. До свидания!")
#             break
#         else:
#             print("error 404.")
#
# if __name__ == "__main__":
#     main()



# class Appointment:
#     def __init__(self, customer_name, appointment_time):
#         self.customer_name = customer_name
#         self.appointment_time = appointment_time
#
# class AppointmentEdit:
#     def __init__(self):
#         self.appointments = []
#
#     def edit_appointment(self):
#         customer_name = input("Введите имя клиента: ")
#         appointment_time = input("Введите время записи: ")
#
#         for appointment in self.appointments:
#             if appointment.appointment_time == appointment_time:
#                 print("Это время уже занято!")
#                 return
#
#         new_appointment = Appointment(customer_name, appointment_time)
#         self.appointments.append(new_appointment)
#         print("Запись на техническое обслуживание создана!")
#
#     def cancel_appointment(self):
#         appointment_time = input("Введите время записи для отмены: ")
#
#         for appointment in self.appointments:
#             if appointment.appointment_time == appointment_time:
#                 self.appointments.remove(appointment)
#                 print("Запись отменена!")
#                 return
#
#         print("Запись на это время не найдена!")
#
#     def display_appointments(self):
#         if len(self.appointments) == 0:
#             print("Нет записей на техническое обслуживание.")
#         else:
#             print("Записи на техническое обслуживание:")
#             for appointment in self.appointments:
#                 print(f"{appointment.customer_name}: {appointment.appointment_time}")
#
#
# scheduler = AppointmentEdit()
#
# while True:
#     print("\nМеню:")
#     print("1. Создать новую запись")
#     print("2. Отменить существующую запись")
#     print("3. Показать все записи")
#     print("4. Выйти из программы")
#
#     choice = input("Выберите пункт меню: ")
#
#     if choice == "1":
#         scheduler.edit_appointment()
#     elif choice == "2":
#         scheduler.cancel_appointment()
#     elif choice == "3":
#         scheduler.display_appointments()
#     elif choice == "4":
#         break
#     else:
#         print("Неверный выбор. Пожалуйста, попробуйте снова.")


# import random
#
# board_size = 10
# player_board = [["~" for _ in range(board_size)] for _ in range(board_size)]
# computer_board = [["~" for _ in range(board_size)] for _ in range(board_size)]
#
#
# def place_ships(board):
#     ship_sizes = [2]
#     for size in ship_sizes:
#         while True:
#             x = random.randint(0, board_size - 1)
#             y = random.randint(0, board_size - 1)
#             direction = random.choice(["horizontal", "vertical"])
#             if direction == "horizontal" and x + size <= board_size:
#                 if all(board[y][x + i] == "~" for i in range(size)):
#                     for i in range(size):
#                         board[y][x + i] = "S"
#                     break
#             elif direction == "vertical" and y + size <= board_size:
#                 if all(board[y + i][x] == "~" for i in range(size)):
#                     for i in range(size):
#                         board[y + i][x] = "S"
#                     break
#
#
# def print_board(board):
#     print(" ", end=" ")
#     for i in range(board_size):
#         print(i, end=" ")
#     print()
#     for i in range(board_size):
#         print(i, end=" ")
#         for j in range(board_size):
#             print(board[i][j], end=" ")
#         print()
#
#
# def get_player_shot():
#     while True:
#         try:
#             x = int(input("Введите координату x для выстрела: "))
#             y = int(input("Введите координату y для выстрела: "))
#             if x < 0 or x >= board_size or y < 0 or y >= board_size:
#                 print("Некорректные координаты. Попробуйте снова.")
#             else:
#                 return x, y
#         except ValueError:
#             print("Некорректный ввод. Попробуйте снова.")
#
#
# def shoot(board, x, y):
#     if board[y][x] == "S":
#         board[y][x] = "X"
#         return True
#     else:
#         board[y][x] = "O"
#         return False
#
#
# place_ships(player_board)
# place_ships(computer_board)
#
# # цикл
# while True:
#     print("Ваше поле:")
#     print_board(player_board)
#     print("Поле компьютера:")
#     print_board(computer_board)
#
#     print("Ваш ход:")
#     x, y = get_player_shot()
#     player_hit = shoot(computer_board, x, y)
#     if player_hit:
#         print("Попадание!")
#     else:
#         print("Промах!")
#
#     x = random.randint(0, board_size - 1)
#     y = random.randint(0, board_size - 1)
#     computer_hit = shoot(player_board, x, y)
#     if computer_hit:
#         print("Компьютер попал по Вашему кораблю!")
#     else:
#         print("Компьютер промахнулся!")
#
#     if all(all(cell != "S" for cell in row) for row in computer_board):
#         print("Вы победили!")
#         break
#
#     elif all(all(cell != "S" for cell in row) for row in player_board):
#         print("Компьютер победил. Попробуйте еще раз.")
#         break

#
# import json
# import random
#
# def load_questions(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         questions = json.load(file)
#     return questions
#
# def ask_question(question, correct_answer):
#     user_answer = input(f"Вопрос: {question}\nВаш ответ: ").strip().lower()
#     return user_answer == correct_answer
#
# def run_quiz(questions):
#     random.shuffle(questions)
#     score = 0
#     for question_data in questions:
#         question = question_data['question']
#         correct_answer = question_data['correct_answer']
#         if ask_question(question, correct_answer):
#             print("Верно!")
#             score += 1
#         else:
#             print(f"Неверно. Правильный ответ: {correct_answer}")
#         print()
#
#     print(f"Вы набрали {score}/{len(questions)} баллов.")
#
# if __name__ == "__main__":
#     filename = 'quizz'
#     questions = load_questions(filename)
#     run_quiz(questions)


# # pip install qrcode
#
# import qrcode
# import os
# import string
# import random
# import datetime
#
# output_folder = "QR"
# if not os.path.exists(output_folder):
# # Функция для генерации QR-кода
#     os.makedirs(output_folder)
#
# def generate_qr_code(text, filename):
#     qr = qrcode.QRCode(
#         version = 1,
#         error_correction = qrcode.constants.ERROR_CORRECT_H,
#         box_size = 10,
#         border = 4,
#     )
#     qr.add_data(text)
#     qr.make(fit = True)
#     image = qr.make_image(fill_color = "black", back_color = "white")
#     file_path = os.path.join(output_folder, filename) # Измененный путь к файлу
#     image.save(file_path)
#
# # Функция для генерации случайной строки
#
# def generate_random_string(length):
#     current_time = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
#     return current_time + '.' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
#
#
# # Ввод текста для QR-кода
# text = input("Ссылка/текст: ")
#
# # Генерация случайного имени файла
# filename = "qr_code_" + generate_random_string(10) + ".png"
#
# try:
#     if len(text) >= 1:
#         print('Имя файла: ', filename)
#         # Генерация QR-кода
#         generate_qr_code(text, filename)
#     else:
#         print("ОШИБКА: Длина текста меньше 1 символа")
# except:
#     print("ОШИБКА: ВВЕДЕНО НЕДОПУСТИМОЕ ЗНАЧЕНИЕ")