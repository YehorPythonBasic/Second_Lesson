# Список с словарями
users = [{"name": "John",
          "age": 15},

         {"name": "Jackie",
          "age": 45},

         {"name": "Milo",
          "age": 15},

         {"name": "Aleksandr",
          "age": 55},

         {"name": "Stephan",
          "age": 50}]

# Поиск самого юного
age_min = users[0]["age"]

for i in users:
    if i["age"] < age_min:
        age_min = i["age"]

# Если несколько людей с минимальным возрастом
names_age_min = []

for dictionary in users:
    if dictionary["age"] == age_min:
        names_age_min.append(dictionary["name"])

# Создание списка со всеми значениями ключей name
list_of_names = []

for user in users:
    if user["name"]:
        list_of_names.append(user["name"])

# Поиск самой длинной строки в списке
max_name = max(list_of_names, key=len)

# Цикл for для поиска самых длинных имен с одинаковой длиной
list_of_max_names = []
for name in list_of_names:
    if len(max_name) == len(name):
        list_of_max_names.append(name)

# Создание списка со всеми значениями ключей age
values = []

for user in users:
    if user["age"]:
        values.append(user["age"])

# Подсчет среднего значения
middle_age = sum(values) / len(values)

# Вывод
print('Минимальный возраст: ', age_min,
      '\nИмена самых молодых людей: ', names_age_min,
      '\nСамые длинные имена: ', list_of_max_names,
      '\nСреднее количество лет всех людей: ', middle_age)
