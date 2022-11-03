import os


class PlayWithFiles:

    # 1. Инициализация класса с одним параметром - имя директории.
    def __init__(self, dir_name: str):
        self.dir_name = dir_name
        os.makedirs(dir_name, exist_ok=True)
        self.database: dict | None = None

    # 2. Написать метод экземпляра класса, который создает атрибут экземпляра класса в ввиде словаря
    # {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
    # Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
    def create_dict(self):
        new_dict = {
            'filenames': [],
            'dirnames': []
        }
        info_list = os.listdir(self.dir_name)
        for i in info_list:
            path = os.path.join(self.dir_name, i)
            if os.path.isfile(path):
                new_dict['filenames'].append(i)
            elif os.path.isdir(path):
                new_dict['dirnames'].append(i)
        self.database = new_dict
        return new_dict

    # 3. Написать метод экземпляра класса, которая получает булевое значение (True/False).
    # Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
    # Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
    def sort_name(self, name, sort: True):
        for h in self.database.values():
            h.sort()
            if not sort:
                h.reverse()

        return name

    # 4. Написать метод экземпляра класса, которая получает строку, которая может быть
    # или именем файла, или именем папки. (В имени файла должна быть точка).
    # В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
    # и вернуть обновленный словарь.
    def add_file_dir(self, name_str: str):
        if "." in name_str:
            self.database["filenames"].append(name_str)
        else:
            self.database["dirnames"].append(name_str)

        return self.database


test = PlayWithFiles(dir_name='Test')

check_2 = test.create_dict()
print(check_2)

check_3 = test.sort_name(check_2, False)
print(check_3)

check_4 = test.add_file_dir('D - four')
print(check_4)
