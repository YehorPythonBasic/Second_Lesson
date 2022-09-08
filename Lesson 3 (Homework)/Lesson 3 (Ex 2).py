# Ввод данных
first_class = input('Введите количество учеников для первого класса:')
second_class = input('Введите количество учеников для второго класса:')
third_class = input('Введите количество учеников для третьего класса:')

# Переобразование типов данных ввода
first_class = int(first_class)
second_class = int(second_class)
third_class = int(third_class)

# Подсчет общего количества учеников
obschee_chislo_uchenikov = first_class + second_class + third_class

# Выясняем сколько останеться учиников если их непарное количество
parnoe = obschee_chislo_uchenikov // 2
ne_parnoe = obschee_chislo_uchenikov % 2

# Подсчитываем количество необходимых парт
obschee_chislo_part = parnoe + ne_parnoe

# Вывод
print('\n' + 'Всего нужно закупить', obschee_chislo_part, 'штук парт')
