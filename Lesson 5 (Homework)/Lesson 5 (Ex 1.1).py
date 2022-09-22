# Ввод высоты
height = int(input('Введите высоту фигуры: '))

# Верхний треугольник
for i in range(1, height + 1):
    for k in range(1, i + 1):
        print("*", end=' ')
    print()
    # Нижний треугольник
for i in range(height, 1, -1):
    for k in range(i, 1, -1):
        print("*", end=' ')
    print()
