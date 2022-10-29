# Функция цензор. На вход функция получает имя файла и список слов для замены,
# функция ничего не возвращает, но в результате ее работы необходимо создать файл,
# в котором слова из списка заменены шаблоном(звездочками например)
# Файл stat.txt(формат данных JSON) со статисткой(обновляемый)
# Файл stat.csv(формат данных csv) со статисткой(обновляемый)
import json
import re
import csv



def cenzor(file_name_input: str, file_name_output: str, word_list: list):
    # Откритие файла (First_text) с исходным текстом в режиме чтения, и запись текста в переменную
    with open(file_name_input, 'r') as f:
        old_data = f.read()
    # Цикл for, который в списке введеных слов провереят текст и заменяет слово на другое функцией replace
    for x in word_list:
        old_data = old_data.replace(x, "***")
    # Запись в новый файл (out.txt) уже отредактированого текста
    with open(file_name_output, 'w') as g:
        g.write(old_data)

    # Откритие файла (First_text) с исходным текстом в режиме чтения, и запись текста в переменную
    with open(file_name_input, 'r') as f:
        old_data = f.read()
    # Цикл for, который в списке введеных слов провереят текст и заменяет слово на другое функцией replace
    for x in word_list:
        old_data = old_data.replace(x, "***")
    # Запись в новый файл (out.txt) уже отредактированого текста
    with open(file_name_output, 'w') as g:
        g.write(old_data)

    # JSON

    words = {}
    words['File name'] = file_name_input

    # Чтение и запись текста с файла где все слова с маленькой буквы
    with open(file_name_input, 'r') as file:
        text_string = file.read().lower()
        match_pattern = re.findall(r'\b[а-я,a-z]{1,20}\b', text_string)

    # Подсчет каждого слова в тексте
    for word in match_pattern:
        count = words.get(word, 0)
        words[word] = count + 1

    # Переменные для json
    json_string = json.dumps(words)

    # Создание json файла
    with open("stat.txt", "w", encoding='utf-8') as file:
        file.write(json_string)


    # CSV

    # Создание csv файла
    with open('stat.csv', 'w', newline='') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["Слово", "Количество", "Имя файла"])
        writer.writeheader()
        for word, amount in words.items():
            writer.writerow({'Слово': word, 'Количество': amount, 'Имя файла': file_name_input})
