import random

# Рандомим список с значениями от 1 до 300 в количестве 10
my_list = [random.randint(1, 300) for i in range(10)]
print('Список:', my_list)
print('\nЧисла из списка больше 100:')

# Цикл for который ищет значения в списке больше 100
for i in my_list:
    if i > 100:
        # Вывод значений больше 100
        print(i, end='  ')
