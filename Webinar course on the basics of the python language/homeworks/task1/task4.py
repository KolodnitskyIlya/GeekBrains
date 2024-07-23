''' Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции. '''

number = input('Введите целое положительное число: ')

if number.isdigit():
    max_number = -1
    norm_number = int(number)
    while norm_number:
        if norm_number % 10 > max_number:
            if norm_number == 9:
                max_number = norm_number
                break
            max_number = norm_number % 10
        norm_number //= 10
    print(max_number)
else:
    print('Вы ввели не число')