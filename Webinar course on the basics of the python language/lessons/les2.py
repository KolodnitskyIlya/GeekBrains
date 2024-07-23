print(type(65))

var_str = "Это строка" # str - неизменяемый тип коллекция итерируемый

print(var_str[0], var_str[3]) # Э ''
print('hello \t world'[6]) # \t

print(len(var_str), var_str[10-1], var_str[len(var_str)-1], var_str[-1], var_str[-10])

print(var_str[1:5])
print(var_str[-7:5])
print(var_str[:5])
print(var_str[:-1])
print(var_str[5:])

print(var_str[::2])
print(var_str[2:9:3])
print(var_str[-7:1:-1])
print(var_str[::-1])

print(var_str[True])
print(var_str[False])
print(var_str[2 > 3])

print(id(var_str))
var_str = 'Hello'
print(id(var_str))
print(id(var_str.lower()))

print(var_str.lower())
print(var_str.upper())
print(var_str.title())

print(var_str.isdigit())
print(var_str.islower())
print(var_str.isupper())

a = 'HELLO'
b = "HELLO"
print(a is b)
print(id(a))
print(id(b))

c = 'ПРИВЕТ №№№№№'
d = 'ПРИВЕТ №№№№№'
print(c is d)
print(c == d)

print('------------------------------------')
var_int = 22 # int - неизменяемый тип

a = 22
b = 22
print(a is b)

a = 257
b = 257
print(a is b)

print('------------------------------------')
var_list = [1, 2, 3, 4, 5, [1, 2, 3], True, False, "HELLO"] # list - изменяемый тип коллекция итерируемая
print(list('hello'))

print(var_list[0])
print(var_list[:4])
print(var_list[5][1])

var_list.append('new')
print(var_list)
print(id(var_list))

var_list.append('new2')
print(id(var_list))

var_list.append(var_list)
print(var_list)
print(var_list[-1])
print(var_list[-1] is var_list)

var_list[-1].insert(0, 'new insert')
print(var_list[-1])
print(var_list)

var_hz1 = var_list.pop()
print(var_hz1)

var_hz2 = var_list.pop(3)
print(var_hz2)

print(var_list)

print('------------------------------------')
var_tuple = (1, 2, 3, 4, 5, [1, 2, 3], True, False, "HELLO") # кортеж tuple - изменяемый коллекция
var_tuple1 = (1, 2, 3, 4, 5, [1, 2, 3], True, False, "HELLO")

print(var_tuple is var_tuple1)
print(var_tuple == var_tuple1)

b = ()
print(b)
print(bool(b))

b = (2, )
print(b)

print(None is None)
print(bool(None))

print('------------------------------------')
var_float = 2.33 # float неизменяемое число

a = float('inf')
print(type(a))
print(a > 1, a == a, a == a + 34343)
print(a)

a = float('nan')
print(a == a, a < a, a > a)
print(a is a)

print('------------------------------------')
var_set = {1, 2, 3, 4, 5, 6, 1, 2, 3, (1, 2, 3)} # set множество изменяемый не индексируемый итерируемый
print(var_set)

var_set = {0, 1, 2, 3, 4, True, False, None}
print(var_set)

var_set = {True, False, 0, 1, 2, 3, 4, None}
print(var_set)

var_set_a = {1, 2, 3, 4}
var_set_b = {2, 4, 6, 8}

print(var_set_a | var_set_b) # объединение
print(var_set_a & var_set_b) # пересечение

print(var_set_a.intersection(var_set_b)) # множество значений из а которые пересекаются в б
print(var_set_a.difference(var_set_b)) # а без б
print(var_set_b.difference(var_set_a)) # б без а

info = var_set_a.pop()
print(info)

var_set_a.remove(2)
print(var_set_a)

var_set_a.add(444)
print(var_set_a)

print('------------------------------------')
var_dict = {'key': 'HELLO', 1: 22, (1, 2): 33} # dict словарь изменяем итерируемый

print(var_dict['key'], var_dict[1], var_dict[(1, 2)])

var_dict = {'key': 'HELLO', 1: 22, (1, 2): 33, True: "TRUE"}
print(var_dict[1])
print(var_dict) # ключ 1 был первый объявлен, а значение последнее добавилось (ключи уникальны и хэшируемы,
# ключ должен быть не изменяем)

print('------------------------------------')
# итерируемость

# i = 0
# while i < len(var_str):
#     char = var_str[i]
#     print(char)
#     i += 1

# for char in var_str:
#     print(char)

for idx, char in enumerate(var_str, 10):
    print(idx, char)

for num in range(0, 10, 3):
    print(num)

for itm, value in var_dict.items():
    print(itm, value)
print(var_dict.items())

b, c = (1, 2)
print(b, c)

a = [(1, 2), (2, 3), (5, 7)]
print(a)
print(dict(a))
b = dict(a)
print(tuple(b))
print(tuple(b.items()))

print(b.keys())

b['hello'] = 22222
print(b)

print(b.get('help', 'NOT HELP'))
print(b.get('hello', 'gg'))

pref = {True: 'доступ разрешен', False: 'Доступ запрещен'}
age = 22

print(pref[age > 18])

user_template = {
    'age' : 'Введите возраст: ',
    'name': 'Введите имя: ',
    'surname': 'Введите фамилию: '
}

user = {}
for key, ask in user_template.items():
    user[key] = input(ask)
print(user)

print('------------------------------------')
# тернарные выражения
a = []
b = [1, 2, 3]

c = a or b # первое встречное True
print(c)

c = a and b # первое встречное False
print(c)

c = a if len(b) > 3 else "HELLO"
print(c)

c = a or b if len(b) <= 3 else "HELLO"
print(c)