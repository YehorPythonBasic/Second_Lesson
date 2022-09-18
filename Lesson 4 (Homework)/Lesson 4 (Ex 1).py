# Ввод
a = float(input('Введите первое число: '))
operator = input('Введите оператор: ')
b = float(input('Введите второе число: '))
podschet = 'zatichka'

# Решение в зависимости от введенного оператора
if operator == '+':
    podschet = a + b
elif operator == '-':
    podschet = a - b
elif operator == '*':
    podschet = a * b
elif operator == '/' and b != 0:
    podschet = a / b
elif operator == '**':
    podschet = a ** b

# Вывод решения и проверка на корректный ввод
if podschet != 'zatichka':
    print(f'Решение:{podschet}')
else:
    print('Введены некорректные данные!')
