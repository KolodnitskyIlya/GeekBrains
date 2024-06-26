# ------------------------------------------------------------------------------------------
my_list_1 = [2, 5, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
my_list = []

cnt = 0
for i in range(len(my_list_1)):
    for j in range(len(my_list_2)):
        if my_list_1[i] == my_list_2[j]:
            cnt = 1
    if cnt == 0:
        my_list.append(my_list_1[i])
    cnt = 0
print(my_list)

# -----------------------------------------------
my_list_1 = [2, 5, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
for number in my_list_1[:]: # my_list_1[:] - создает временную копию списка, для того, чтобы избежать ошибки
    # "индекс вне диапазона" при удалении элементов из списка в процессе итерации.
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)
# ------------------------------------------------------------------------------------------
date = input()
d, m, y = date.split('.')
print(d, m, y)

month = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одинадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое'
}
print(days[d], month[m], y, 'года')
# ------------------------------------------------------------------------------------------
numbers = [2, 2, 5, 12, 8, 2, 12]
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print(result)
