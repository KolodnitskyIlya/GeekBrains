import random

class Animal:
    _mass = 1 # protected
    __age = 0 # private

    def __init__(self, name, mass):
        print('START INIT')
        print(id(self))
        self.name = name
        self.mass = mass
        print('END INIT')

    def say(self):
        print(f'{self.name} say: где звон монеты')

    def get_age(self):
        return self.__age

animal1 = Animal('Пес', 27)
print(id(animal1))
animal2 = Animal('Кот', 8)
print(id(animal2))

animal1.say()
animal2.say()

print(animal1.get_age())

print('#' * 20)

'''Инкапсуляция - позволяет скрыть детали реализации данных и методов внутри класса и предоставить контролируемый 
интерфейс для взаимодействия с ними. Это обеспечивает защиту данных от непосредственного доступа и изменения извне, 
а также улучшает структурированность и безопасность кода.

В Python инкапсуляция достигается с помощью следующих механизмов:

1) Именование приватных атрибутов и методов. Для обозначения атрибутов и методов, которые будут доступны только внутри 
класса, используются имена, начинающиеся с одного или двух подчёркиваний.
2) Использование свойств (properties). В Python можно использовать свойства для обеспечения контролируемого доступа к 
атрибутам класса.'''

NAMES = ('Шарик', 'Бобик', 'Пират')

class Animal2:
    __age = 0
    _population = []

    def __init__(self, a_type, mass):
        self.a_type = a_type
        self.mass = mass
        self._population.append(self)

    def say(self):
        print(f'{self.a_type} say: где звон монеты')

    def get_population(self):
        return tuple(self._population)

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(self.a_type, random.randint(1, 10))

animal1 = Animal2('Пес', 27)
animal2 = Animal2('Кот', 8)

print(Animal2._population)

'''
Наследование — это возможность создания нового класса на базе существующего.

Наследование предполагает наличие отношения «является» между классом-наследником и классом-родителем. При этом 
класс-потомок будет содержать те же атрибуты и методы, что и базовый класс, но при этом его можно расширять через 
добавление новых методов и атрибутов.

В организации наследования участвуют как минимум два класса: класс-родитель и класс-потомок. Возможно множественное 
наследование, в этом случае у класса-потомка может быть несколько родителей.
'''

class Dog(Animal2):
    def __init__(self, name):
        self.name = name
        super().__init__('Собака', random.randint(1, 3))
        #Animal.__init__(self, 'Собака', random.randint(1, 3))

dog1 = Dog('ШАРИК')
dog2 = Dog('ХАТИКО')

print(dog1.name, dog1.a_type)
dog1.say()
print(dog1.get_population())

'''
Полиморфизм — это концепция, которая позволяет обращаться с объектами разных классов так, как будто они являются 
объектами одного класса.

Реализовать полиморфизм можно через наследование, интерфейсы и перегрузку методов.

Этот подход имеет несколько преимуществ:

Позволяет использовать различные реализации методов в зависимости от типа объекта, что делает код более универсальным и 
удобным для использования.

Уменьшает дублирование кода — можно написать одну функцию для работы с несколькими типами объектов.

Позволяет использовать общие интерфейсы и абстракции для работы с объектами разных типов.

Обеспечивает гибкость и расширяемость — можно добавлять новые типы объектов без необходимости изменять существующий код.
'''

class Dog2(Animal2):
    def __init__(self, name):
        self.name = name
        super().__init__('Собака', random.randint(1, 3))

    def say(self):
        super().say()
        print('ГАВ ГАВ')

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(random.choice(NAMES))
class Cat(Animal2):
    def __init__(self, name):
        self.name = name
        super().__init__('Кошка', random.randint(1, 3))

    def say(self):
        print('МЯУ')

dog12 = Dog2('ШАРИК')
dog22 = Dog2('ХАТИКО')

cat1 = Cat('Барсик')
cat2 = Cat(',Борис')

cat1.say()
dog12.say()

animal3 = animal1.breeding(animal2)
print(animal3.a_type)

dog32 = dog12.breeding(dog22)
print(dog32.name)

dog42 = dog32.breeding(cat1)
print(dog42.a_type)


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = {}

    def add_animal(self, animal):
        if self.__animals.get(animal.a_type):
            self.__animals.get(animal.a_type).append(animal)
        else:
            self.__animals[animal.a_type] = [animal]

    def atype_population(self, atype):
        return self.__animals.get(atype)

zoo = Zoo('NYCZ')
zoo.add_animal(dog12)
zoo.add_animal(animal2)
zoo.add_animal(cat2)

print(zoo.atype_population('Собака'))
print(zoo._Zoo__animals)