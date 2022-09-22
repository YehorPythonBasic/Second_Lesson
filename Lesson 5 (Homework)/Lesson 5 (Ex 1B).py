# Ввод высоты
height = int(input('Введите высоту фигуры: '))

for h in range(height):
    for i in range(h, height - 1):
        print(' ', end=' ')
    for w in range(2 * h + 1):
        if w == 0 or \
                w != 0:
            print('*', end=' ')
    print()
