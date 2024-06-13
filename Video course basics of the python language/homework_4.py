def info(name, age, city):
    return f'{name},{age} год(а), проживает в городе {city}'
print(info('Василий', 21, 'Москва'))
# ------------------------------------------------------------------------------------------

def max_number(a, b, c):
    return max(a, b, c)
print(max_number(5, 6, -5))
# ------------------------------------------------------------------------------------------

def attack(person_1, enemy_1):
    person_damage, enemy_damage = armor_damage(person_1, enemy_1)
    person_1['health'] = person_1['health'] - enemy_damage
    enemy_1['health'] = enemy_1['health'] - person_damage

def armor_damage(person_1, enemy_1):
     person_damage = person_1['damage'] / enemy_1['armor']
     enemy_damage = enemy_1['damage'] / person_1['armor']
     return person_damage, enemy_damage


player = {'name': input("Введите имя игрока: "), 'health': 100, 'damage': 80, 'armor': 2}
enemy = {'name': input("Введите имя врага: "), 'health': 80, 'damage': 30, 'armor': 1.5}

print(player)
print(enemy)

attack(player, enemy)

print(player)
print(enemy)

