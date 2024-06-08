# ------------------------------------------------------------------------------------------
number = int(input())
print(number + 2)

print()
# ------------------------------------------------------------------------------------------
person_number = int(input())
while not(0 < person_number < 10):
    print("Число должно быть больше 0 и меньше 10")
    person_number = int(input())
print(person_number ** 2)

print()
# ------------------------------------------------------------------------------------------
name = input('Имя: ')
surname = input('Фамилия: ')
age = int(input('Возраст: '))
weight = int(input('Вес: '))
if age <= 30 and 50 <= weight <= 120:
    print('Пациент в хорошем состоянии')
elif (age > 30 and age <= 40) and (weight < 50 or weight > 120):
    print('Пациенту требуется заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print('Пациенту требуется врачебный осмотр')


