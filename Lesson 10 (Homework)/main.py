# Подключение модуля с функцией
from function_cenzor import cenzor

# Использование функции (cenzor) из модуля (function_cenzor)
# На вход file_name_input - имя файла с текстом
# file_name_output - имя файла на выход
# word_list - список слов
p = cenzor(file_name_input='First_text.txt', file_name_output='out.txt', word_list=['Python', 'текст'])

# Отредактированный текст вы можете найти в файле с именем out.txt
