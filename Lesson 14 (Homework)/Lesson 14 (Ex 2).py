# Общий класс Животные от него все классы будут дочерние
class Animals:
    def __init__(self, name, weight, movement_speed):
        self.name = name
        self.weight = weight
        self.movement_speed = movement_speed

    # Метод класса для вывода информации в консоль
    def __str__(self):
        return f'name: {self.name}' \
               f'\nweight(g): {self.weight}' \
               f'\nmovement speed(km/h): {self.movement_speed}'


# Дочерний класс от Животных - Птицы, добавлена длина крыльев
class Birds(Animals):
    def __init__(self, name, weight, movement_speed, wing_length):
        super().__init__(name, weight, movement_speed)
        self.wing_length = wing_length

    def __str__(self):
        base = super().__str__()
        return base + f'\nwing length(sm): {self.wing_length}\n'

    # Функция которая отвечает за издаваемые звуки дочерних классов этого класса, проверка на имя животного
    # для определения издаваемого звука
    def say(self):
        if self.name == 'crown':
            print('Caaarrr!')
        elif self.name == 'owl':
            print('Uwu!')
        else:
            print('Chirick!')


# Дочерний класс от Птиц - Ворона, добавлен цвет птицы
class Crown(Birds):
    def __init__(self, name, weight, movement_speed, wing_length, colour):
        super().__init__(name, weight, movement_speed, wing_length)
        self.colour = colour

    def __str__(self):
        base = super().__str__()
        return base + f'colour: {self.colour}\n'


# Дочерний класс от Птиц - Сова, добавлен размер птицы
class Owl(Birds):
    def __init__(self, name, weight, movement_speed, wing_length, size):
        super().__init__(name, weight, movement_speed, wing_length)
        self.size = size

    def __str__(self):
        base = super().__str__()
        return base + f'size(sm): {self.size}\n'


# Дочерний класс от Животных - Гады, добавлена опасность для человека
class Gads(Animals):
    def __init__(self, name, weight, movement_speed, lethal_to_humans):
        super().__init__(name, weight, movement_speed)
        self.lethal_to_humans = lethal_to_humans

    def __str__(self):
        base = super().__str__()
        return base + f'\nlethal to humans: {self.lethal_to_humans}\n'

    # Функция которая отвечает за издаваемые звуки дочерних классов этого класса, проверка на имя животного
    # для определения издаваемого звука
    def say(self):
        if self.name == 'python':
            print('Shhhhhh!')
        elif self.name == 'alligator':
            print('Hrrrrrr!')
        else:
            print('Phew!')


# Дочерний класс от Гадов - Питон, добавлен цвет
class Python(Gads):
    def __init__(self, name, weight, movement_speed, lethal_to_humans, colour):
        super().__init__(name, weight, movement_speed, lethal_to_humans)
        self.colour = colour

    def __str__(self):
        base = super().__str__()
        return base + f'colour: {self.colour}\n'


# Дочерний класс от Гадов - Алигатор, добавлен размер челюсти
class Alligator(Gads):
    def __init__(self, name, weight, movement_speed, lethal_to_humans, jaw_size):
        super().__init__(name, weight, movement_speed, lethal_to_humans)
        self.jaw_size = jaw_size

    def __str__(self):
        base = super().__str__()
        return base + f'jaw size(sm): {self.jaw_size}\n'


# Дочерний класс от Животных - Млекопитающие, добавлено наличие меха
class Mammalian(Animals):
    def __init__(self, name, weight, movement_speed, hair_presence):
        super().__init__(name, weight, movement_speed)
        self.hair_presence = hair_presence

    def __str__(self):
        base = super().__str__()
        return base + f'\nhair presence: {self.hair_presence}\n'

    # Функция которая отвечает за издаваемые звуки дочерних классов этого класса, проверка на имя животного
    # для определения издаваемого звука
    def say(self):
        if self.name == 'bear':
            print('Roarrrr!')
        elif self.name == 'monkey':
            print('Woaaaaa!')
        else:
            print('Tch Tch!')


# Дочерний класс от Млекопитающих - Медведь, добавлен цвет меха
class Bear(Mammalian):
    def __init__(self, name, weight, movement_speed, hair_presence, fur_colour):
        super().__init__(name, weight, movement_speed, hair_presence)
        self.fur_colour = fur_colour

    def __str__(self):
        base = super().__str__()
        return base + f'fur colour: {self.fur_colour}\n'


# Дочерний класс от Млекопитающих - Обезьяна, добавлена высота прыжка
class Monkey(Mammalian):
    def __init__(self, name, weight, movement_speed, hair_presence, jump_height):
        super().__init__(name, weight, movement_speed, hair_presence)
        self.jump_height = jump_height

    def __str__(self):
        base = super().__str__()
        return base + f'jump height(sm): {self.jump_height}\n'


# Проверка работы каждого из классов
Crown = Crown(name='crown', weight=400, movement_speed=30, colour='black', wing_length=8)
print(Crown)

Owl = Owl(name='owl', weight=1000, movement_speed=25, size=50, wing_length=15)
print(Owl)

Python = Python(name='python', weight=3000, movement_speed=15, colour='green', lethal_to_humans='yes')
print(Python)

Alligator = Alligator(name='alligator', weight=20000, movement_speed=30, lethal_to_humans='yes', jaw_size=1000)
print(Alligator)

Bear = Bear(name='bear', weight=55000, movement_speed=50, hair_presence='yes', fur_colour='brown')
print(Bear)

Monkey = Monkey(name='monkey', weight=5000, movement_speed=35, hair_presence='yes', jump_height=2000)
print(Monkey)

# Подставет название животного для проверки издаваемого звука
Bear.say()
