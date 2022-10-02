import random

# Создаем первый список с помощью рандома от 1 до 100 с длиной в 7
my_list_1 = [random.randint(1, 100) for i in range(7)]

# Создаем второй список с помощью рандома от 1 до 100 с длиной в 7
my_list_2 = [random.randint(1, 100) for h in range(7)]

# Создаем третий список с помощью сложения первого и второго списка
my_result = my_list_1[::2] + my_list_2[1::2]

# Вывод
print('my_list_1:', my_list_1)
print('my_list_2:', my_list_2)
print('my_result:', my_result)
