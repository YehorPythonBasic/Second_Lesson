# Ввод
my_str = input('Введите строку:')
new_str = []

# Узнаем длину строки для цикла
dlina = len(my_str)

# Цикл for для перебора попарных элементов строки
for i in range(0, dlina, 2):
    # Добавление элементов в новую строку
    if i < dlina - 1:
        new_str.append(my_str[i] + my_str[i + 1])
        # Если не четное, то добавляем '_'
    else:
        new_str.append(my_str[i] + '_')
# Вывод
print(new_str)
