# Словари
my_dict_1 = {'nickname': 'LandLord',
             'class': 'Warrior',
             'level': 30
             }

my_dict_2 = {'nickname': 'Tifer',
             'class': 'Thief',
             }

# Переобразование словарей (ключей) в множества
my_dict_1_set = set(my_dict_1)
my_dict_2_set = set(my_dict_2)

# Создание списка из ключей, которые есть в обоих словарях
in_two_dict = list(my_dict_1_set & my_dict_2_set)

# Создание списка из ключей, которые есть в первом словаре, но нет во втором
only_in_dict_1 = list(my_dict_1_set - my_dict_2_set)

# Поиск, ключ:значение которое есть в первом словаре но нет во втором
pair_only_my_dict_1 = None

for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        pair_only_my_dict_1 = dict([item])

# Создаем пустой словарь в который будем добавлять элементы из словарей
dict_1_uni_dict_2 = dict()

# Цикл for, который проверяет наявность ключ:значение в словарях
for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        dict_1_uni_dict_2[item[0]] = item[1]
    else:
        dict_1_uni_dict_2[item[0]] = [item[1], my_dict_2[item[0]]]

# Вывод
print('Cписок из ключей, которые есть в обоих словарях:', in_two_dict,
      '\nCписок из ключей, которые есть в первом но нет во втором словаре:', only_in_dict_1,
      '\n{Ключ:значение} которые есть в первом, но нет во втором словаре:', pair_only_my_dict_1,
      '\nОбъединенные два словаря:', dict_1_uni_dict_2)
