# Метод My_database, который принимает info из классов, и записывает эту информацию в текстовый файл.
# Таким образом, мы создаем своеобразную базу данных с транспортом, который у нас есть.
# Вызываем этот метод, когда хотим добавить транспорт определенного класса в нашу базу данных.
def My_database(info):
    with open('Databse.txt', 'a') as file:
        file.write(info)


class Transport:
    def __init__(self, state_number, wheels, motor_accuracy, max_speed):
        self.state_number = state_number
        self.wheels = wheels
        self.motor_accuracy = motor_accuracy
        self.max_speed = max_speed

    # Метод класса для вывода информации в консоль
    def __str__(self):
        return f'\nstate_number: {self.state_number}' \
               f'\nwheels: {self.wheels}' \
               f'\nmotor_accuracy: {self.motor_accuracy}' \
               f'\nmax_speed: {self.max_speed}'


class Bicycle(Transport):
    def __init__(self, state_number, wheels, motor_accuracy, max_speed, size):
        super().__init__(state_number, wheels, motor_accuracy, max_speed)
        self.size = size

    # Перезапись метода класса для вывода информации в консоль с дополнительной информацией от наследника
    def __str__(self):
        base = super().__str__()
        return base + f'\nsize: {self.size}\n'

    # Метод для класса, который вызывает метод вне класса, для добавления информации в базу данных
    def Add_to_database(self):
        info = f'Bicycle{self.__str__()}\n'
        My_database(info)


class Motorcycle(Bicycle):
    def __init__(self, state_number, wheels, motor_accuracy, max_speed, size, type):
        super().__init__(state_number, wheels, motor_accuracy, max_speed, size)
        self.type = type

    # Перезапись метода класса для вывода информации в консоль с дополнительной информацией от наследника
    def __str__(self):
        base = super().__str__()
        return base + f'type: {self.type}\n'

    # Метод для класса, который вызывает метод вне класса, для добавления информации в базу данных
    def Add_to_database(self):
        info = f'Motorcycle{self.__str__()}\n'
        My_database(info)


class Car(Transport):
    def __init__(self, state_number, wheels, motor_accuracy, max_speed, doors, brand):
        super().__init__(state_number, wheels, motor_accuracy, max_speed)
        self.doors = doors
        self.brand = brand

    # Перезапись метода класса для вывода информации в консоль с дополнительной информацией от наследника
    def __str__(self):
        base = super().__str__()
        return base + f'\ndoors: {self.doors}' \
                      f'\nbrand: {self.brand}\n'

    # Метод для класса, который вызывает метод вне класса, для добавления информации в базу данных
    def Add_to_database(self):
        info = f'Car{self.__str__()}\n'
        My_database(info)


class Bus(Transport):
    def __init__(self, state_number, wheels, motor_accuracy, max_speed, purpose):
        super().__init__(state_number, wheels, motor_accuracy, max_speed)
        self.purpose = purpose

    # Перезапись метода класса для вывода информации в консоль с дополнительной информацией от наследника
    def __str__(self):
        base = super().__str__()
        return base + f'\npurpose: {self.purpose}\n'

    # Метод для класса, который вызывает метод вне класса, для добавления информации в базу данных
    def Add_to_database(self):
        info = f'Bus{self.__str__()}\n'
        My_database(info)


class Truck(Bus):
    def __init__(self, state_number, wheels, motor_accuracy, max_speed, purpose, max_weight_lifting):
        super().__init__(state_number, wheels, motor_accuracy, max_speed, purpose)
        self.max_weight_lifting = max_weight_lifting

    # Перезапись метода класса для вывода информации в консоль с дополнительной информацией от наследника
    def __str__(self):
        base = super().__str__()
        return base + f'max weight lifting(kg): {self.max_weight_lifting}\n'

    # Метод для класса, который вызывает метод вне класса, для добавления информации в базу данных
    def Add_to_database(self):
        info = f'Truck{self.__str__()}\n'
        My_database(info)


first = Truck(state_number='AA666', wheels=4, motor_accuracy=150, max_speed=80, purpose='Buildings',
              max_weight_lifting=800)
print(first)

first.Add_to_database()
