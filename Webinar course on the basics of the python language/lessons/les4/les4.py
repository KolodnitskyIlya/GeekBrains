result = []

for itm in range(10):
    if itm & 1:
        result.append(itm)

print(result)

#result2 = [itm for itm in range(10) if itm & 1]
#result2 = {itm: itm / 2 for itm in range(10) if itm & 1}

result2 = [(itm, n, m) for itm in range(5) for n in range(10, 20) for m in range(50, 100)]
print(result2)

t_tup = tuple((itm, n, m) for itm in range(5) for n in range(10, 20) for m in range(50, 100))
print(t_tup)


# yield - возврат промежуточного значения(функция сразу становится генератором)
def my_map(func, iter_object):
    for itm in iter_object:
        yield func(itm)

tmp = my_map(lambda x: x ** 2, range(3))
print(tmp)
print(list(tmp))

tmp = my_map(lambda x: x ** 2, range(3))
print(next(tmp))
print(next(tmp))
print(next(tmp))

tmp = my_map(lambda x: x ** 2, range(3))

for itm in tmp:
    print(itm)

# while True:
#     try:
#         itm = next(tmp)
#         print(itm)
#     except StopIteration:
#         break

def some(x):
    yield x - 2
    yield x - 3
    yield x - 4

tmp = some(10)

print(tmp)

for itm in tmp:
    print(itm)

def some_2(x, y):
    for n in range(y):
        print('PRE YIELD')
        yield (n + x) ** y
        print('POST YIELD')
    print('CYCLE DONE')

tmp = some_2(2, 5)
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
print(next(tmp))
