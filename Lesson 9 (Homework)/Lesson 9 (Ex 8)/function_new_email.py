# Функция для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен

def create_email(li_names: list, li_domains: list):
    import random
    from string import ascii_lowercase

    # Переменные в которых будут рандомится значения
    name = random.choice(li_names)
    num = random.randint(100, 999)
    chose_domain = random.choice(li_domains)
    rand_range_str = random.randint(5, 7)
    rand_string = ''.join(random.choice(ascii_lowercase)
                          for i in range(rand_range_str))

    # Новый email который содержит в себе все переменные
    new_email = f'{name}.{num}@{rand_string}.{chose_domain}'

    # Вывод
    return new_email
