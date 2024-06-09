import random

user_number = random.randint(1, 100)
print(f'Пользователь загадал число: {user_number}')

result = {
    'Загаданное число меньше': '<',
    'Загаданное число больше': '>',
    'Победа': '='
}

comp_number = None
min_value = 1
max_value = 100
while comp_number != user_number:
    comp_count = random.randint(1, 5)
    comp_list = []

    for i in range(comp_count):
        comp_number = random.randint(min_value, max_value)
        comp_list.append(comp_number)
        print(comp_number)

    polz_answer = input()
    if polz_answer == result['Победа']:
        print('Победа')
        break
    elif polz_answer == result['Загаданное число меньше']:
        max_value = comp_list[-1] - 1
    else:
        min_value = comp_list[-1] + 1


