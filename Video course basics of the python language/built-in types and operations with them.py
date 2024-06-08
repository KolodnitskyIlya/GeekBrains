# string
friend = 'Maxim'
friend_1 = "Max"
print(type(friend), type(friend_1))

say = 'say "Hello"'
print(say)

first_letter = friend[0]
print(first_letter, type(first_letter))
print(friend[3])
print(friend[-1], friend[-2])

# cut
friend = 'Maxim'
print(friend[1:3]) # с 1-го по 3-й элемент
print(friend[:3]) # с начала по 3-й элемент
print(friend[2:]) # от 2-го элемента и до конца

# methods
friends = 'Максим;Леонид1'
number = '3453453453'
print(friends)
print(len(friends))
print(friends.find('Лео'), friends.find('34Лео'))
print(friends.split(';'))
print(friends.isdigit(), number.isdigit())
print(friends.upper())
print(friends.lower())

# formatting strings
name = 'Leo'
age = 30
# 1. Конкатенация
print('Привет, ' + name + ' тебе ' + str(age) + ' лет')
# 2. %
print('Привет, %s тебе %d лет'%(name, age))
# 3. format
print(f'Привет, {name} тебе {age} лет')


stroka_23 = "Первые 5 мест на соревнованиях: 1. иванов 2. петров 3 сидоров 4. орлов 5. соколов"
start = stroka_23.find('1')
end = stroka_23.find('4')

top3 = stroka_23[start:end]
print(f'Поздравляем {top3.upper()}с успехом!')

print()
# ------------------------------------------------------------------------------------------
# lists
# списки - упорядоченные изменяемые коллекции объектов произвольных типов
empty_list = []
some_list = ['hello', 123, True]
friends_list = ['Leo', 'Max', 'Kate']
print(friends_list)
print(friends_list[0], friends_list[-1])

print(friends_list[1:2])
print(friends_list[:2])
print(friends_list[1:])


print(len(friends_list))

friends_list.append('Ron')
print(friends_list)
print(len(friends_list))

print(friends_list.pop())
print(friends_list)

friends_list.clear()
print(friends_list)

friends_list = ['Leo', 'Max', 'Kate']

friends_list.remove('Kate')
print(friends_list)

del friends_list[0]
print(friends_list)

# оператор in

hero = 'Superman'

if hero.find('man') != -1:
    print('Есть')

if 'man' in hero:
    print('Есть')

goals = ['здоровье', 'спорт', 'учеба']

if 'здоровье' in goals:
    print(100)

# tuple(кортеж) - список который нельзя менять (нужен для защиты от изменений)
roles = ('user', 'manager', 'admin')


print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))

names = []

while count != 0:
    name = names.append(input(f'Кто занял {count} место?: '))
    count -= 1

print(f'В соревнованиях участвовали: {sorted(names)}')

names.reverse()

print(f'Победители: {names[:3]}. Поздравляем!')

print()
# ------------------------------------------------------------------------------------------
# sequence(последовательность) - контейнер, элементы которого представляют собой некую последовательность,
# могут быть как изменяемыми(список), так и неизменяемыми(кортеж, строка)
# реализует определенные методы(индексация, взятие длины, цикл for in)
# утиная типизация - если объект содержит реализацию методов последовательности - он будет считаться последовательностью

friend_name = 'Max'
friends = ['Leo', 'Max', 'Kate']
roles = ('user', 'manager', 'admin')

# while
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

# for - перебор последовательности(индекс не нужен)
for friend in friends:
    print(friend)

for letter in friend_name:
    print(letter)

for role in roles:
    print(role)

print()
# ------------------------------------------------------------------------------------------
# range - последовательность целых чисел
numbers = range(10)
print(numbers)
print(type(numbers))
print(list(numbers))

winners = ['Leo', 'Max', 'Kate']

for i in range(len(winners)):
    print(i + 1, winners[i])
# range(start_or_stop, stop, step)

numbers = [1, 3, 5]

print(list(range(1, 1000, 2)))

for number in range(1, 1000, 2):
    print(number)

for i in range(1, len(winners) + 1):
    print(i, winners[i-1])

print()
# ------------------------------------------------------------------------------------------
# dictionaries - неупорядоченные коллекции произвольных объектов с доступом по ключу.
my_dict = {'a': 1, 'b': 1}
dog = {'name': 'Rocky', age: 3}

friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))

print(friend['age'])

friend['has_car'] = True
print(friend)

friend['has_car'] = False
print(friend)

del friend['age']
print(friend)

if 'age' in friend:
    print('Есть возраст')
if 'has_car' in friend:
    print('Есть машина')

# перебор
friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам
for key in friend.keys():
    print(key)
    print(friend[key])

for key in friend:
    print(key)
    print(friend[key])

# по значениям
for value in friend.values():
    print(value)

# пары ключ значение
for item in friend.items():
    print(item)

for key, value in friend.items():
    print(key)
    print(value)

print()
# ------------------------------------------------------------------------------------------
# sets - неупорядоченные коллекции, содержащие не повторяющиеся элементы(не может быть одинаковых элементов)
cities_1 = {'Las Vegas', 'Paris', 'Moscow'}

cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
print(type(cities))
print(cities)

cities = set(cities)
print(cities)
print(type(cities))

cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)

cities.add('Burma')
print(cities)
cities.add('Moscow')
print(cities)

cities.remove('Moscow')
print(cities)

print(len(cities))

print('Paris' in cities)

for city in cities:
    print(city)

# операции со множествами(объединение |, пересечение &, разность -)

max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

print(max_things | kate_things) # и Макс взял и Кейт взяла
print(max_things & kate_things) # какие вещи повторяются
print(max_things - kate_things) # взял Макс, но не взяла Кейт
print(kate_things - max_things) # взяла Кейт, но не взял Макс