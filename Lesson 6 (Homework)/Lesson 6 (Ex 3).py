import random

# Рандомим список с значениями от 1 до 300 с длиной от 0 до 5
my_list = [random.randint(1, 300) for i in range(random.randint(0, 5))]
print('Список:', my_list)
if len(my_list) < 2:
    my_list.append(0)
    print('Длина списка меньше 2, поэтому в список в конец был добавлен 0:', my_list)
else:
    my_list = my_list[-1] + my_list[-2]
    print('Длина списка больше или равна 2, поэтому сумма последних двух элементов:', my_list)
