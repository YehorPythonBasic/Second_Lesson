import random

# Создаем первый список с помощью рандома от 1 до 100 с длиной в 5
my_list = [random.randint(1, 100) for i in range(5)]

# С помощью срезов, создаем новый список на основе первого
new_list = my_list[1:] + [my_list[0]]

# Вывод
print('Первый список', my_list)
print('Новый список', new_list)
