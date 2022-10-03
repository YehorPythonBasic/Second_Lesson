# Ddjl
my_str = input('Введите строку:')

# Новый список
new_str = []

# Цикл for для проверки всех элементов строки
for i in my_str:
    if my_str.count(i) == 1:
        new_str.append(i)

# Вывод
print(new_str)
