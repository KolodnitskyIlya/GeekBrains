# определение модуля
# python позволяет поместить классы, функции, данные а также скрипты в отдельный файл и использовать их в др. программах
# модулем в python называется любой файл с программой
# применение: управление пространством имен, повторное использование кода, деление большого проекта на мелкие части
# разновидности модулей: встроенные(math, random, ...), сторонние(django,PyQt5, ...), свои(любой .py файл)
# варианты подключений: import math(целиком), import math as mt(псевдоним), from math import*(все содержание, не реком),
# импорт конкретных функций, классов, ...: from math import sin, cos

import math
import random as rd

print(math.pi)
print(math.sin(45))

print(rd.randint(1, 10))

from math import *
from random import randint, randrange

print(pi)
print(sin(30))

print(randint(1, 10))

print()
# ------------------------------------------------------------------------------------------
# math - математические функции, работа с числами
import math

r = 100
print(2 * math.pi * r)
print(math.pi * r**2)
print(math.pi * math.pow(r, 2))

x1, y1 = 10, 10
x2, y2 = 50, 100

x = x2 - x1
y = y2 - y1

print(math.sqrt(x**2 + y**2))

print(math.factorial(9))

# random - генерация случайных чисел, букв, элементов последовательности
from random import randint, choice, sample, shuffle

print(randint(0,100))

players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players)) # выбирает один элемент
print(sample(players, 3)) # выбирает заданное число элементов

cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards) # перемешивает
print(cards)

print()
# ------------------------------------------------------------------------------------------
# создание собственных модулей
# import first_module(если в той же папке)
# import folder.second_module(название папки.название самого модуля (если не в одной и той же папке))
import first_module

print(first_module.foo)
first_module.bar()

from modules.first_module import foo, bar

print(foo)
bar()

# модули со скриптами
# при любом варианте импорта скрипты будут выполняться
# если не указано никаких условий (if __name__ == '__main__')
# это обязательно нужно учитывать при импорте

import modc
from modc import foo
# всегда будет выполняться скрипт print() независимо от всех условий, даже если импортируем некоторые элементы

# if __name__ == '__main__'
# ограничивает выполнение скриптов
# при импорте код не будет выполняться
# но он будет выполняться при запуске самого модуля

# __name__ == __main__ в самом модуле, но тут __name__ == modc, следовательно скрипты не выполнятся

print()
# ------------------------------------------------------------------------------------------
# пакеты
# пакет - каталог включающий в себя другие пакеты и модули
# пакет содержит файл __init__.py
# назначение пакетов: формирование пространств имен, работа с модулями с указанием уровня вложенности
# пакет1.пакет2.модуль
# уровни отделяются точкой
#   ВАРИАНТЫ ИМПОРТОВ:
# import.модуль - внутри пакета из одного модуля в другой
# import пакет.модуль - стандартно
# import, from, as ...
# вложенность пакетов может быть любой(пакет в пакете ...)

from hospital.h import get_main
from hospital.patients.index import get_index

get_main()
get_index()

print()
# ------------------------------------------------------------------------------------------
# модуль os
# функции для работы с операционной системой
# не зависит от конкретной ОС
# функции: name, chdir, getcwd(), mkdir(), os.path, ...

import os

print(os.name) # имя операционной системы

print(os.getcwd()) # текущая рабочая директория

new_path = os.path.join(os.getcwd(), 'new_f') # создаем новый путь
#os.mkdir(new_path) # создаем папку по новому пути

# модуль sys
# взаимодействие с интерпретатором python
# функции: executable, exit(), platform, path, argv

import sys

print(sys.executable) # путь до интерпретатора

print(sys.platform) # информация о платформе

#sys.exit() # выход из python

print('Этот код мы уже не выполним')

# sys.path
# очень важная переменная
# она хранит пути по которым python ищет модули
# она имеет изменяемый тип данных list
# таким образом мы можем изменять эту переменную

# мы можем импортировать
import math
# но не можем импортировать наш модуль например на диске C:
#import mymodule

# как питон находит модули?
import sys

print(sys.path)
print(type(sys.path))

for p in sys.path:
    print(p)

# как нужно импортировать на разных дисках и тд.

#sys.path.append('D:')
#import mymodule

# -----------------------------------------

import sys, os

name = sys.platform

#for i in range(1, 6):
    #new_path = os.path.join(os.getcwd(), f'{name}_{i}')
    #os.mkdir(new_path)

print()
# ------------------------------------------------------------------------------------------
# запуск скрипта с параметрами
# sys.argv
# список аргументов командной строки при запуске скрипта python
# sys.argv[0] - путь до скрипта
# остальные параметры передаются при вызове скрипта через пробел
# python my_script.py par1 par2 par3 ...

# перейти в папку scripts with parameters

