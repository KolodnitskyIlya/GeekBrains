# functions - фрагмент программного кода (подпрограмма), к которому можно обратиться из другого места программы
# Функции: input(), print(), type(), range() и др.
print(abs(-7))

numbers = [5, 15, 7, 1, -9, 0]
print(max(numbers))
print(min(numbers))

print(round(56.435636346, 3))

print(sum(numbers))

winners = ['Leo', 'Max', 'Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)

print()
# -----------------------------------------------
numbers_list = []
a, b, c = numbers_list.append(int(input())), numbers_list.append(int(input())), numbers_list.append(int(input()))

print(min(numbers_list))
print(max(numbers_list))
print(sum(numbers_list))

print()
# ------------------------------------------------------------------------------------------
# native functions

print('Моя первая функция')
print('-' * 100)
print('-' * 100)
print('-' * 100)
print('Красивый разделитель')
print('-' * 100)
print('-' * 100)

def print_sep():
    print('-' * 100)
print('Моя первая функция')
print_sep()
print_sep()
print_sep()
print('Красивый разделитель')
print_sep()
print_sep()

def print_sep(sep):
    print(sep * 100)
print_sep('*')
print_sep('+')

def print_sep(sep, len):
    print(sep * len)
print_sep('>', 50)
print_sep('<', 100)

def get_sep(sep, len):
    return sep * len
print(get_sep('{', 60))

print()
# ------------------------------------------------------------------------------------------
# function parameters

def hello_max():
    print('Hello', 'Max')
hello_max()

def hello(who):
    print('Hello', who)
hello('Leo')

def greeting(who, say):
    print(say, who)
greeting('Leo', 'Hi')
greeting(say='Hi', who='Leo')

def greeting(who, say='Hello'):
    print(say, who)
greeting('Neet')
greeting('Neet', 'Hi')

# Иногда нужно реализовать передачу любого количества аргументов
# def greeting('Hello', 'Leo', 'Max', 'Kate', ...)
# args - передача любого кол-ва по порядку (приходит кортеж)
# kwargs - передача любого кол-ва по имени (приходит словарь)

def greeting(say, *args):
    print(say, args)

greeting('Hello', 'Leo')
greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo', 'Max', 'Kate')

def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

get_person(name='Leo', age=20, has_car=True)

print()
# ------------------------------------------------------------------------------------------
# areas of view
# Область видимости - область программы, в пределах которой идентификатор(имя) некоторой переменной продолжает быть
# связанным с этой переменной и возвращать ее значение.
# За пределами области видимости тот же самый идентификатор может быть связан с другой переменной, либо быть свободным
# Область видимости объекта
# набор функций или модулей, внутри которых допустимо использование имени этого объекта

def my_f(my_var):
    my_var = 999
    print('Внутри функции:', my_var)

a = 1
my_f(a)
print('После выполнения функции', a)

def some_f():
    a = 999
    print('переменная внутри функции:', a)

a = 1
some_f()
print('переменная после выполнения функции', a)

# local and global variables
# Глобальными называют объекты, объявление которых дано вне функции. Они доступны(видимы) во всем файле, в котором они
# объявлены
# Локальными называют объекты, объявление которых дано внутри блока или функции. Эти объекты доступны только внутри того
# блока, в котором они объявлены

global_var = 1

def my_f():
    local_var = 100
    print(local_var)
    print(global_var)

my_f()
print(global_var)

# global
# при желании можно изменить глобальную переменную
# для этого в функции нужно указать что она глобальная
# global my_var
# этот механизм лучше не использовать (есть риск изменить значение переменной в одной функции, после чего получить
# неверное значение в другой функции)

global_var = 1
def my_f():
    global global_var
    local_var = 100
    print(local_var)
    print(global_var)
    global_var = 999

my_f()
print(global_var)

# почему стоит избегать изменение глобальных переменных?

global_var = 2

def my_f():
    result = global_var ** 5
    print(result)

def my_change_f():
    global global_var
    global_var = 'Какая то строка'

# my_change_f()
my_f()

# относительность области видимости
# вложенные друг в друга функции

m = 'Меня видно везде'

def a():
    ma = 'Меня видно в b() и в a()'

    def b():
        print(m)
        print(ma)
        mb = 'Меня видно в c() и в b() но не видно в a()'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'Меня видно только в c()'
        c()
    b()
a()

print()
# ------------------------------------------------------------------------------------------
# Передача функции параметром в другую функцию

def some_f():
    return 10

result = some_f()
print(result)

a = some_f
print(a)
print(type(a))

print(a())

# Функция - тоже объект
# Ее можно записать в переменную
# Ее можно передавать параметром в другие функции

def f():
    print('hello from other f')

def to(f_param):
    f_param() # параметром будет функция

to(f)

# Применение: алгоритм, последовательность действий, сами действия

def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

def is_even(number):
    return number % 2 == 0

def is_not_even(number):
    return number % 2 == 1

def big_4(number):
    return number > 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_filter(numbers, is_even))
print(my_filter(numbers, is_not_even))
print(my_filter(numbers, big_4))

# lambda-функции
# применяются для создания анонимных функций по месту их использования
# lambda входные параметры: результат

def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_filter(numbers, lambda number: number % 2 == 0))
print(my_filter(numbers, lambda number: number % 2 == 1))
print(my_filter(numbers, lambda number: number > 4))

print()
# ------------------------------------------------------------------------------------------
# функция sorted - сортировка последовательности
# sorted(iterable, *, key=None, reverse=False)
# аргументы: последовательность, ключ для сортировки, порядок

numbers = [1, 5, 3, 5, 9, 7, 11]
print(sorted(numbers)) # по возрастанию
print(sorted(numbers, reverse=True)) # по убыванию

names = ['Max', 'Alex', 'Kate']
print(sorted(names))

cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
print(sorted(cities)) # по алфавиту

def by_count(city):
    return city[1]

print(sorted(cities, key=by_count)) # по численности населения
print(sorted(cities, key=lambda city: city[1])) # по численности населения

# filter - фильтрация последовательности
# filter(function, iterable)
# аргументы: функция фильтрации, последовательность

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)
print(result)

result = list(result)
print(result)

names = ['Max', 'Alex', 'Kate']

print(list(filter(lambda name: len(name) > 3, names)))

# map - применяет функцию к каждому элементу последовательности
# map(func, iterable, ...)
# аргументы: функция, последовательность

numbers = [5, 3, 4, 7, 8]

print(list(map(lambda x: x**2, numbers)))
print(list(map(lambda x: str(x), numbers)))