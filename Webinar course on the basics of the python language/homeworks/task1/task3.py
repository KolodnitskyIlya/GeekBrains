''' 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369. '''

n = input("Введите число: ")

sum_int = 0
if n.isdigit():
    cnt = 3
    while cnt:
        sum_int += int(cnt * n)
        cnt -= 1
    print(sum_int)
else:
    print('Вы ввели не число')