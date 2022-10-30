class ITMan:

    def __init__(self, firstname, lastname, age, e_mail, skills, people_lang, coding_lang):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.e_mail = e_mail
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    # Функция print_itman_info которая возвращает всю информацию про персонажа
    def print_itman_info(self):
        info = {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age,
            'e_mail': self.e_mail,
            'skills': self.skills,
            'people_lang': self.people_lang,
            'coding_lang': self.coding_lang
        }
        for key in info:
            print(f'{key}:{info[key]}')

    # Функция is_name которая проверяет, правильное ли имя персонажа
    def is_name(self, firstname):
        if (self.firstname == firstname):
            print("Yes, it is my name")
        else:
            print("No, it is not my name")


first_man = ITMan('Kenny', 'MacCormic', 8, 'kenny@gmail.com', ['говорить', 'ходить', 'умирать'], ['Укр', 'Англ'],
                  ['Python', 'Java'])

second_man = ITMan('Eric', 'Cartman', 8, 'cartman@gmail.com', ['говорить', 'ходить', 'толстеть'],
                   ['Укр', 'Англ', 'Китай'],
                   ['Java'])

first_man.print_itman_info()
second_man.print_itman_info()
first_man.is_name('Stan')
second_man.is_name('Eric')
