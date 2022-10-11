# Подключение модуля с функцией
from function_new_email import create_email

# Использование функции (create_email) из модуля (function_new_email)
p = create_email(li_names=['alex', 'bob', 'anna', 'rebeka'], li_domains=['com', 'ua', 'org', 'net'])

# Вывод
print(p)
