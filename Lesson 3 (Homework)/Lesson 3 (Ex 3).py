# Ввод
chislo = input('Введите число:')

# Переобразование типа ввода
chislo = int(chislo)

# Вычисление цифр
cifra_1 = chislo // 100
cifra_2 = chislo / 10 % 10
cifra_3 = chislo % 10

# Переобразование второй цифры из float в int
cifra_2 = int(cifra_2)

# Вывод с использованием форматирования f-string для вывода без пробелов между цифрами
print (f'{cifra_3}' + f'{cifra_2}' + f'{cifra_1}')
