# open - открывает файл в указанном режиме
# f = open('my_txt', 'w')
# file - имя файла
# mode - режим
# encoding - кодировка

# Режимы открытия:
# r - чтение,
# w - запись, если файла нет, создается новый,
# x - запись, если файла нет, ошибка,
# a - дозапись,
# b - двоичный режим,
# + - открытие на чтение и запись

# f = open('first.txt', 'w')
# f = open('second.txt', 'r')
# f = open('first.txt', 'r')

# Запись текста в файл:
# write - запись строку в файл
# writelines - записать список строк в файл
# \n - символ конца строки

f = open('first.txt', 'w')

f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'Python\n'])

# Чтение из файла
# read - чтение всего файла
# for line in f: - чтение файла построчно
# readlines - чтение файла в список строк

f = open('first.txt', 'r')

#print(f.read())

# for line in f:
#     print(line.replace('\n', ""))

#print(f.readlines())

# Закрытие файла
# при работе с файлом его необходимо закрывать
# открытие файла тратят ресурсы системы
# f.close()
# но если до close произойдет исключительная ситуация, то файл не будет закрыт
# удобным вместо close() является использование with

f = open('first.txt', 'r')

for line in f:
    print(line.replace('\n', ""))

f.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ""))

print('end')

print()
# ------------------------------------------------------------------------------------------
# строки байт, кодировки
# str - обычные строки
# bytes - строки байт
# bytearray - изменяемая строка байт

s = 'Hello world'
print(type(s))

sb = b'Hello bytes'
print(type(sb))
print(sb)

# Действия со строками байт
# индекс sb[0]
# срез sb[1:3] и др.

s = 'Hello world'

sb = b'Hello bytes'

print(s[1])
print(sb[1])

print(s[1:3])
print(sb[1:3])

for item in sb:
    print(item)

# как строка хранится в памяти?
# любая информация хранится в памяти как набор 0 и 1
# строки не являются исключением
# каждому символу ставится в соответствие определенный код (число)
# коды могут быть разные и зависят от кодировки

# Основные кодировки:
# ascii - американские символы
# latin-1 - европейские символы
# utf-8 - универсальная кодировка для большинства языков
# чем универсальнее кодировка тем больше байт требуется для кодирования одного символа

sb = b'Ad'

print(sb[0]) # по ascii = 65
print(sb[1]) # по ascii = 100

# Перевод строки в байты (кодирование)
# 'Hello world'.encode('utf-8')
# при переводе строки str в байты bytes указываем кодировку
# кодировка должна поддерживать символы нужного нам алфавита

s = 'Hello world Мир'

sb = s.encode('utf-8')

print(sb)
print(type(sb))

# перевод байт в строку (декодирование)
# sb.decode('utf-8')
# указываем кодировку, которой мы кодировали строку

s = 'Hello world Мир'

sb = s.encode('utf-8')

print(sb)
print(type(sb))

s = sb.decode('utf-8')

print(s)
print(type(s))

print()
# ------------------------------------------------------------------------------------------
# Запись и чтение байтов
# open('filename', 'wb') - режим записи байтов
# open('filename', 'rb') - режим чтения байтов
# параметр encoding определяет кодировку
# open('filename', 'w', encoding='utf-8')

# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    pass

with open('bytes.txt', 'rb') as f:
    pass

# открываем файл в текстовом режиме с указанием кодировки
with open('bytes.txt', 'r', encoding='utf-8') as f:
    pass

# запись байтов в файл
# f.write(b'some bytes') - файл открыт в режиме wb
# f.write('some str') - файл открыт в режиме w
# в любом случае информация хранится в виде 0 и единиц

with open('bytes.txt', 'wb') as f:
    f.write(b'Hello bytes')

with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# f.read() - файл открыт в режиме rb - читаем байты
# f.read() - файл открыт в режиме r - читаем строки

with open('bytes.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир')

with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))

    s = result.decode('utf-8')
    print(s)

print()
# ------------------------------------------------------------------------------------------
# Сериализация
# это процесс преобразования объекта в поток байтов для сохранения или передачи в память, базу данных или файл
# обратный процесс - десериализация
# Применение: сохранение объекта в файл, сохранение объекта в базу данных, передача объекта по сети

# Способы записи объекта в файл:
# ручной "создание велосипеда"
# универсальный pickle

# ручной способ
# {'name': 'Max', 'phones': [123, 345]}
# как перевести такой объект (dict) в байты для сохранения в файл?
# например: 1. придумать способ приведения объекта к более простым
# 2. придумать свой формат хранения

person = {'name': 'Max', 'phones': [123, 345]}

# записываем объект в файл
with open('person.dat', 'wb') as f:
    name = person['name']
    f.write(f'{name}\n'.encode('utf-8'))

    phones = person['phones']
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('объект записан')

# читаем объект из файла
with open('person.dat', 'rb') as f:
    result = f.readlines()

person = {}
person['name'] = result[0].decode('utf-8').replace('\n', '')

phones = []
for bphone in result[1:]:
    phones.append(int(bphone.decode('utf-8').replace('\n', '')))

person['phones'] = phones

print(person)

# Ручной способ(недостатки):
# не универсальный
# при небольшом изменении объекта изменится весь алгоритм
# надо помнить как мы делали сохранение, чтобы потом прочитать
# трудоемкий

# Модуль pickle
# сохраняет сложные объекты в файл
# преобразует сложные объекты в байты
# встроен в пайтон

# Основные функции:
# dump - сохранение объекта в файл
# dumps - преобразование объекта в байты
# load - загрузка объекта из файла
# loads - загрузка объекта из набора байт

import pickle

person = {'name': 'Max', 'phones': [123, 345], 'age': 20}

# записываем объект в файл
with open('person.dat', 'wb') as f:
    pickle.dump(person, f)

print('Объект записан')

# читаем объект из файла
with open('person.dat', 'rb') as f:
    person = pickle.load(f)

print(person)

print()
# ------------------------------------------------------------------------------------------
# JSON (JavaScript Object Notation)
# текстовый формат обмена данными, основанный на JavaScript
# аналогичен набору словарей, списков, простых типов данных в python
# но является просто текстом (строкой)
# Применение: хранение и передача данных, чаще используется в web разработке, для передачи данных по протоколу http

# json в python
# т.к. основные структуры python схожи с форматом
# требуется только преобразование в строку и обратно
# этим занимается модуль json
# import json

# Основные функции:
# dump - сохранение объекта в формате json в файл
# dumps - преобразование объекта в json (в текст)
# load - загрузка объекта из файла
# loads - загрузка объекта из формата json (строки)

import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': 'Leo', 'age': 33}
]

print(type(friends))

# запись в json
json_friends = json.dumps(friends)

print(json_friends)
print(type(json_friends))

# обратно из json в объект
friends = json.loads(json_friends)

print(friends)
print(type(friends))

# открываем файл
with open('friends.jon', 'w') as f:
    json.dump(friends, f)

# обратно из файла в объект
with open('friends.jon', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))
print()
# ------------------------------------------------------------------------------------------
import json

favourite_tracks = [
    {'name': 'Вечная любовь', 'artist': 'Агата Кристи'},
    {'name': 'Angel', 'artist': 'Massive Attack'},
    {'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(favourite_tracks, f)

print('Выполнено')

