''' 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
месяц (зима, весна, лето, осень). Напишите решения через list и через dict. '''

month_number = input('Введите месяц в виде целого числа: ')

months = ['зима', 'весна', 'лето', 'осень']
dict_weather = {
    (12, 1, 2) : months[0],
    (3, 4, 5): months[1],
    (6, 7, 8): months[2],
    (9, 10, 11): months[3]
}

if month_number.isdigit():
    for key, value in dict_weather.items():
        if int(month_number) in key:
            print(value)
else:
    print('Вы ввели не число')

# month_number = 12
# print(month_number // 3 % 4)