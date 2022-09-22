# Ввод высоты
height = int(input('Введите высоту фигуры: '))
# Верхний треугольник
for h in range(height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(2 * h + 1):
        if w == 0 or w != 0:
            print('*', end=' ')
    print()
    # Нижний треугольник
for h in range(height - 1):
    for w in range(2 * height):
        if w - height + 2 == height - 1 - h or w + height - 1 == height + h or w == height - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
