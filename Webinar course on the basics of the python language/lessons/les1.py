# PEP 8

# snake_case = 1
# CamelCase = 2
# camelCase = 3

# kebab-case = 2

some_str = "Hello my friends" # str()
some_str2 = 'Hello my friends'

some_int = 1 # int()
some_float = 2.33434343 # float()
some_bool = True # bool()

ask_name = "введите имя\n"
ask_age = "введите возраст\n"
#
# name = input(ask_name)
#
# print("Привет", name, end='!!!!!', sep='----')

# age = input(ask_age)
#
# if age.isdigit():
#     age = int(age)
#     if age >= 18:
#         print('Доступ открыт')
#     elif age > 16:
#         print('Доступ к боевикам')
#     else:
#         print('Смотри мультики')
# else:
#     print("Введено не число")

print(isinstance(2.0, int))
print(isinstance(2.0, float))

print(4 % 2)
print(bool(4 % 2))
print(bool(1), not bool(-2), bool(-56))

# & - and в бинарной логике
# лучшая проверка на четность
print(5 & 1, bin(5), bin(1)) #0b101 0b001 - так как посл 1(True) == посл 1(True), то будет 1
print(4 & 1, bin(4), bin(1))
print(hex(55), hex(5))
print(oct(55), oct(5))

x = 5
if x & 1:
   print ("Наш x - нечетный")
else:
   print ("Наш x - четный")
# Здесь всё просто, мы наше двоичное представление 5 (101) сравниваем с двоичным представлением 1 (001), через
# побитовое И. В итоге получаем 001, что будет больше нуля, значит последний символ в двоичном представлении - 1
# (вся суть такой проверки, выяснить, последний символ у нас 1 (нечетное) или 0 (четное).

print(int('010101', 2), int('010101', 8))

a = 123456789543

temp = a # сохраняем переменную a
while temp: # любое число отличное от нуля - True
   tmp = temp % 10
   temp //= 10
   if tmp == 5:
      continue
   # a = a // 10
   print(tmp, temp)
else:
   print('ELSE')

# моржовый оператор

a = 1234567895430

temp = a
while (tmp := temp % 10) or temp:
   temp //= 10
   print(tmp, temp)
else:
   print('ELSE')