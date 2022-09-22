# Ввод высоты
height = int(input('Введите высоту фигуры: '))

for h in range(height, 0, -1):
    for i in range(h + 1, height + 1):
        print(' ', end=' ')
        # Левая часть треугольника
    for w in range(h + 1):
        if w != 0:
            print('*', end=' ')
        # Правая часть треугольника
    for w in range(h):
        if w != 0:
            print('*', end=' ')
    print()
