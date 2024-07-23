''' 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль. '''

def devide(*args: float) -> None:
    '''
    делит a на b и обратно
    :param args: любые действительные числа
    :return: None
    '''
    try:
        print(int(args[0]) / int(args[1]))
        print(int(args[1]) / int(args[0]))
    except ZeroDivisionError:
        print("Нельзя делить на ноль")

number1, number2 = input("Введите первое число\n"), input("Введите второе число\n")

if number1.isdigit() and number2.isdigit():
    devide(number1, number2)
else:
    print("Вы ввели не число")

devide2 = lambda a, b: a / b if b else None

# МИНИ ТЕСТЫ
assert devide2(4, 2) == 2, 'devision(4, 2) SOME TEXT'
assert devide2(0, 2) == 0, 'devision(0, 2)'
assert devide2(1, 0) is None, 'devision(1, 0)'