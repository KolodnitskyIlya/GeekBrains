#import statistics
#import statistics as stat
#from statistics import *
from statistics import mean as mn, median as md

a = [itm for itm in range(2, 1000, 3) if itm & 1]

def statistics():
    return 0

print(mn(a))
print(md(a))


import sys # нужно запускать из терминала

def my_sum(x, y):
    return x + y

def my_pow(x, y):
    return x ** y

proc = {
    'sum': my_sum,
    'pow': my_pow
}

print(sys.argv) # список всех аргументов запуска программы
if len(sys.argv) > 3:
    _, f, x, y = sys.argv
    print(proc[f](float(x), float(y)))

print(sys.platform) # имя ядра операционной системы


from itertools import cycle
import time
import random

tmp = ['one', 'two', 'three', 'four', 'five']

# for itm in cycle(range(10)):
#     print(itm)
#     time.sleep(1.5)
#     num = random.choice(tmp)
#     print(num)


import functools

a = [2, 3, 4, 5, 6, 7]

print(((((2 / 3) / 4) / 5) / 6) / 7)
print(functools.reduce(lambda x, y: x / y, a))


# рекурсия
def my_s(*args):
    return args[-1] + my_s(*args[:-1]) if args else 0

print(my_s(1, 2, 3, 4, 5, 6, 7))
print(my_s(1, 7)) # хвостовая рекурсия (вызывает саму себя первый и последний раз)