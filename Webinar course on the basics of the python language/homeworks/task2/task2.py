''' 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения
списка элементов необходимо использовать функцию input(). '''

info = []

while True:
    s = input('Введите элемент списка: ')
    if s:
        info.append(s)
    else:
        break

for idx in range(0, len(info) - 1, 2):
    info[idx], info[idx + 1] = info[idx + 1], info[idx]

print(info)
