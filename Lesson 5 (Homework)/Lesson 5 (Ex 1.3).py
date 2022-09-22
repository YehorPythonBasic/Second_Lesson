# Ввод высоты
height = int(input('Введите высоту фигуры: '))

# Верхний треугольник
for h in range(0, height):
    for i in range(h, height - 1):
        print(" ", end=' ')
    for w in range(0, h + 1):
        print("*", end=' ')
    print()
    # Нижний треугольник
for h in range(height - 1):
    for i in range(0, h + 1):
        print(" ", end=' ')
    for w in range(h, height - 1):
        print("*", end=' ')
    print()
