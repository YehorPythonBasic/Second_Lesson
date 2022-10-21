# Функция цензор. На вход функция получает имя файла и список слов для замены,
# функция ничего не возвращает, но в результате ее работы необходимо создать файл,
# в котором слова из списка заменены шаблоном(звездочками например)

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
