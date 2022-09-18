# Ввод
a = float(input('Введите первое число: '))
operator = input('Введите оператор: ')
b = float(input('Введите второе число: '))
podschet = 'zatichka'
chisla_posle_tochki = 'zatichka'

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

# Убераем числа после точки, если их нет, так как тип float и он будет всегда дробным
if podschet != 'zatichka':
    chisla_posle_tochki = (podschet / 1) - (podschet // 1)
if chisla_posle_tochki != 'zatichka' and chisla_posle_tochki > 0:
    podschet = float(podschet)
if chisla_posle_tochki != 'zatichka' and chisla_posle_tochki == 0:
    podschet = int(podschet)

# Вывод решения и проверка на корректный ввод оператора и деления на 0
if podschet != 'zatichka':
    print(f'Решение:{podschet}')
else:
    print('Введены некорректные данные!')
