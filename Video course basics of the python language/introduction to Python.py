print('Hello world')
print('Hello world')
# ------------------------------------------------------------------------------------------

name = 'Кеша'
age = 2
period = 5

print(name)
print(age + period)

print()
# верное наименование переменных(age, person_name, is_good, person)

# типы данных
age = 30
print(type(age))
person_name = 'Max'
print(type(person_name))
period = 3.2
print(type(period))
is_good = True
print(type(is_good))
person = None
print(type(person))

print()
# приведение типов
a = '4567'
print(type(int(a)))

b = 345
print(type(str(a)))

year = '1988'
period = 20
print(int(year) + period)
print(year + str(period)) # конкатенация строк

print()
# ------------------------------------------------------------------------------------------
# ввод и вывод данных
print('Hello')
print('Hello % Rrfr # ede')
print(100)
print(None)

print(5, 45)

age = 5
name = "Кеша"
print(name, age, sep=',')
print(name, age, sep='\n')

print("Kеша", end=" ")
print(5)

result = input('How old are you? ')
print('Тебе', result)

number = float(input())
print(number + 10)

print()
# ------------------------------------------------------------------------------------------
# арифметические операции
ale = 71
age = int(input())
print(ale + age)
print(ale - age)
print(ale * age)
print(ale / age)
print(ale // age)
print(ale ** age)
print(ale % age)

# логические операции (==, !=, <, >, <=, >=)
f = ale == age
print(f)

# сложные логические выражения (and, or, not)
f_1 = ale < 100 and ale == 71
print(f_1)

print()
# ------------------------------------------------------------------------------------------
# условные операторы

age = int(input())
if age < 18:
    print('БАН')
elif 18 <= age < 21:
    print('ОК')
else:
    print('КРАСАВА')
    if age % 5 == 0:
        print('СОМНИТЕЛЬНО НО ОК')

print()
# ------------------------------------------------------------------------------------------
# циклы

number = 43
value = int(input('Угадайте число: '))

while value != number:
    if value < number:
        print("Берите больше")
    else:
        print('Берите меньше')

    value = int(input('Угадайте число: '))
print('Вы угадали!')

n = 0
while n <= 100:
    print(n)
    n += 1

n = int(input())
k = 0
while k <= n:
    print(k)
    k += 1

n = int(input())
k = 0
while k <= n:
    if k % 2 == 0:
        print(k)
    k += 1

print()
# ------------------------------------------------------------------------------------------
# break - continue. while - else

n = int(input())
k = 0
while k <= n:
    if k % 2 == 0:
        print(k)
        break
    k += 1

number = 0
n = int(input())

while number <= n:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1

n = 0
while n <= 100:
    print(n)
    n += 1
else:
    print('А все')

n = 0
while n <= 100:
    print(n)
    n += 1
    if n == 33:
        break
else:
    print('А все')