''' 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]. '''

my_list = [7, 5, 3, 3, 2]

while True:
    pers_number = input("Пользователь ввел число: ")
    if pers_number:
        if pers_number.isdigit():
            if int(pers_number) in my_list:
                my_list.sort(reverse=False)
                reverse_number_index = my_list.index(int(pers_number))
                my_list.sort(reverse=True)
                my_list.insert(len(my_list) - reverse_number_index, int(pers_number))
                print(my_list)

            else:
                my_list.append(int(pers_number))
                my_list.sort(reverse=True)
                print(my_list)
        else:
            print("Вы введи не число")
    else:
        break
