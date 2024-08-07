''' 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
} '''

product_template = {
    'название': ('имя товара', str),
    'цена': ('стоимость товара', int),
    'количество': ('количество товара', int),
    'ед': ('Единицы измерения (шт, кг, и тд)', str),
}

next_enter = True

auto_inc = 1
products_list = []

while next_enter:
    # словарь в который мы будем заполнять атрибуты товара
    product = {}
    # заполняем товар по шаблону
    for key, value in product_template.items():
        # цикл While True я использую для того, чтобы переспросить вопрос, если будет неверный ввод по типу
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value) # int(user_value)
            except ValueError as e:
                print(f"{e}\nНе верное значение данных")
                continue
            product[key] = user_value
            break
    products_list.append((auto_inc, product))
    auto_inc += 1

    # тут мы проверим надо еще товар вводить или нет
    while True:
        next_add = input('Добавить еще продукт? Да/Нет\n')
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, повторите')
print(products_list)

products_analytics = {}

for key in product_template:
    result = []
    for itm in products_list:
        result.append(itm[1][key])
    products_analytics[key] = result

    # products_analytics[key] = [itm[1][key]] for itm in products_list
print(products_analytics)