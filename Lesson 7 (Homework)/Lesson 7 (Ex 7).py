# Ввод
my_str = input('Введите строку:')

# Переменные с буквами
i_letter = "o"
h_letter = "g"

# Создание новой строки на основе поиска элементов из веденной строки
new_str = my_str[my_str.find(i_letter) + 1: my_str.rfind(h_letter)]

# Вывод
print(new_str)
