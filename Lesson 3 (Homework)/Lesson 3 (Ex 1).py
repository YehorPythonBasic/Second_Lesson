# Ввод данных
shkolniki = input('Введите количество школьников:')
yabloki = input('Введите количество яблок в корзине:')

# Переобразование типов данных ввода
shkolniki = float(shkolniki)
yabloki = float(yabloki)

# Подсчет значений
kazdomu_shkolniiku = yabloki // shkolniki
v_korzine = yabloki % shkolniki

# Переобразование типов на случай если пользователь введет дробное количество яблок (например 0.5 - половина яблока)
kazdomu_shkolniiku = int(kazdomu_shkolniiku)
v_korzine = float(v_korzine)

# Вывод данных
print('\n' + 'Если делить поровну, то каждому школьнику достанеться по такому количеству яблок:', kazdomu_shkolniiku)
print('В корзине осталось:', v_korzine)
