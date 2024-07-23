'''
map zip round sum filter min max abs sort reduce
'''

a = ['1', '2', '3', '4']
b = map(int, a)
print(b)
print(map('', a))
print(list(b))

print(map.__doc__)

from typing import Callable, Iterable, List
def my_map(func: Callable, some: Iterable) -> list:
    '''
    Реализация функции map
    :param func: call object
    :param some: iterable object
    :return: list result
    '''
    result = []
    for itm in some:
        result.append(func(itm))
    return result
print(my_map(int, a))

print(my_map.__doc__)

some = ['1', '2']

def some_append(itm) -> list:
    some = []
    some.append(itm)
    return some

a = [1, 2, 3, 4, 5]

b = some_append('HELLO')
print(some)
print(b)
# b = my_map(str, a) # позиционная передача
# c = my_map(some=a, func=str) # именновая передача


print(all.__doc__)

print(all((1, 1, 1, 0)))
print(all((1, 1, 1, 1)))
print(all([]))

print(any.__doc__)

print(any((1, 1, 1, 0)))
print(any((0, 0)))
print(any([]))

def some_f(*args, **kwargs):
    print(type(kwargs))
    print(type(args))
    print(args)
    print(kwargs)

def my_min(*args, key=lambda x: x):
    result = float('inf')
    for itm in args:
        if result > key(itm):
            result = key(itm)
    return result

some_f(1, 2, 3, 4, key1=1, key2=33, key3=44)

def some_key(x):
    return x + 22 ** 2

print(min(22, 333, 444, 666))
print(my_min(333, 444, 666, 22, key=some_key))
print(my_min(333, 444, 666, 22, key=lambda x: x + 22 ** 2))
print(type(my_map))
print(type(lambda x: x))

def some_temp(template: tuple):
    def producter(items):
        product = {}
        for name, item in zip(template, items):
            product[name] = item
        return product
    return producter

producter_1 = some_temp(('название', 'количество'))
a = producter_1(('comp', 22))
print(a)

print(zip.__doc__)

a = [1, 2, 3, 4]
b = [66, 55, 44, 33]
print(zip(a, b))
print(list(zip(a, b)))

c = [222, 3333, 444, 5555, 666, 7777777]
print(list(zip(a, b, c)))