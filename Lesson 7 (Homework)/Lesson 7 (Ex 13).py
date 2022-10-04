# Ввод
str_one = input('Введите первую строку ')
str_two = input('Введите вторую строку ')

# Новые списки для цикла
new_str1 = []
new_str2 = []

# Цикл for для первой строки, поиск элементов которые в строке только 1 раз
for i in str_one:
    if str_one.count(i) == 1:
        new_str1.append(i)

# Цикл for для второй строки, поиск элементов которые в строке только 1 раз
for h in str_two:
    if str_two.count(h) == 1:
        new_str2.append(h)

# Переобразование новых двух строк в множества
new_str1 = set(new_str1)
new_str2 = set(new_str2)

# Создание нового множества с помощью операции пересечения первых двух множеств
new_list = new_str1 & new_str2

# Переобразование множества в список
new_list = list(new_list)

# Вывод
print(new_list)
