height = int(input('Введите высоту фигуры: '))

for h in range(height):
    for w in range(2 * height - 1):
        if w == height - 1 - h or \
                w == height - 1 + h or \
                h == height - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
