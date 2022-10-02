# Ввод
my_string = input('Введите строку: ')

# Переобразование строки в список и разбитее на элементы
li = my_string.split()

# Счетчик
counter = 0

# Цикл for, для поиска чисел
for i in li:
    # Проверяем, состоит ли список из цифр
    if i.isdigit():
        counter += int(i)

# Вывод
if counter >= 1:
    print('Сумма всех чисел в строке:', counter)
else:
    print('В строке нет чисел')
