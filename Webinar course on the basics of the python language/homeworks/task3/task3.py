''' 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов. '''

def my_sum(args: tuple) -> int:
    sum = 0
    for itm in args:
        sum += int(itm)
    return sum

def my_min(args: tuple) -> int:
    min = float('inf')
    for itm in args:
        if itm < min:
            min = itm
    return min

def my_func(*args) -> int:
    return my_sum(args) - my_min(args)

print(my_func(-1, 2, -5))