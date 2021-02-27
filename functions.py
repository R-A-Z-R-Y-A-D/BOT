from classes import *

menu_message = 'Список доступных комманд:\n' \
               '/steam_data - показать сохраненные данные Steam\n' \
               '/help - получить справку по всем настройкам'

# Подписывает первую строку таблицы (названия столбцов)
def excel_start_settings():
    base['a1'].value='id пользователя'
    base['b1'].value='Логин Steam'
    base['c1'].value='Пароль Steam'
    base['d1'].value ='Статус оплаты'
    base['e1'].value ='Тип баланса S-статический; D-динамический'
    base['f1'].value = 'Ставки после крашей (1-5)'
    # объединение ячеек для крашей (только подпись)
    base.merge_cells('f1:j1')
    base['k1'].value ='Участие в лесенках (0-нет, 1-КНК, 2-КНКНК)'
    base['l1'].value ='Фикс. ставка после лесенки'
    base['m1'].value ='Несгораемый баланс'
    base['n1'].value ='Выбранный сайт'

# Обрабатывает комманды из меню
def menu(message):
    if message.text == '/steam_data':
        send_steam_data(message)
    if message.text == '/analytics' and admin_check(message.chat.id):
        pass
    else:
        pass

# Проверяет пользователя, админ он или нет
def admin_check(id):
    for i in admins:
        if str(admins[i]) == str(id):
            return True
    return False

# Возвращает номер строки в результате поиска пользователя по id
def find_user_in_base (id):
    for row in range(1, base.max_row+1):
        if str(base[row][0].value) == str(id):
            return row
    return False

# Обработчик команды старт
@bot.message_handler(commands=['start'])
def getting_start(message):
    if find_user_in_base(message.chat.id) == 0:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('НАЧАТЬ')
        markup_reply.add(item_start)
        message = bot.send_message(message.chat.id, 'Нажмите на кнопку, чтобы запустить бота', reply_markup=markup_reply)
        bot.register_next_step_handler(message, make_new_user)
    else:
        message = bot.send_message(message.chat.id, menu_message, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, menu)

# Отсылает к функции сбора данных Steam
def make_new_user(message):
    if message.text.lower() == 'начать':
        welcome_text = "Здравствуйте, вы активировали бота, который поможет вам полностью автоматизировать" \
                       "ваши ставки на сайтах csgo.fail, csgo.band!\n" \
                       "Для начала давайте настроим бота (эти параметры можно будет изменить в любой момент)\n" \
                       "Введите ваши данные Steam, логин и пароль через пробел"
        message = bot.send_message(message.chat.id, welcome_text, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, add_st_data_to_table, index=1)
    else:
        pass

# Отсылает пользователю сохраненные в таблице данные Steam
@bot.message_handler(commands=['steam_data'])
def send_steam_data(message):
    us = find_user_in_base(message.chat.id)
    if not us:
        message = bot.send_message(message.chat.id, f"У вас нет доступа к этой комманде\n{menu_message}", reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, menu)
    else:
        bot.send_message(message.chat.id, f'<b>Логин Steam:</b> {str(base[us][1].value)}\n<b>Пароль Steam:</b> {str(base[us][2].value)}')
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_yes = types.KeyboardButton('Да')
        item_no = types.KeyboardButton('Нет')
        markup_reply.add(item_yes, item_no)
        time.sleep(1)
        message = bot.send_message(message.chat.id, "Хотите изменить их?", reply_markup=markup_reply)
        bot.register_next_step_handler(message, register_again)

# Принимает ответ от пользователя, хочет он изменить свои данные или нет
def register_again(message):
    if message.text.lower() == 'нет':
        message = bot.send_message(message.chat.id, menu_message, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, menu)
    elif message.text.lower() == 'да':
        message = bot.send_message(message.chat.id, 'Введите ваши данные Steam, логин и пароль, через пробел', reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, add_st_data_to_table)

# Заносит данные в таблицу, если они были введены верно
def add_st_data_to_table(message, index=0):
    data = [str(x) for x in message.text.split()]
    if len(data) != 2:
        if index == 0:
            message = bot.send_message(message.chat.id, f"Процесс был прерван, вы ввели данные неправильно, попробуйте еще раз")
            bot.register_next_step_handler(message, add_st_data_to_table, index=0)
        elif index == 1:
            message = bot.send_message(message.chat.id, f"Процесс был прерван, вы ввели данные неправильно, попробуйте еще раз")
            bot.register_next_step_handler(message, add_st_data_to_table, index=1)
    else:
        if index == 0:
            us = find_user_in_base(message.chat.id)
            base[us][1].value = data[0]
            base[us][2].value = data[1]
            message = bot.send_message(message.chat.id, f"Данные были успешно сохранены\n{menu_message}")
            bot.register_next_step_handler(message, menu)
        elif index == 1:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton('0 5 28 95 100')
            markup_reply.add(item)
            message = bot.send_message(message.chat.id, "Отлично, введите 5 чисел от 0 до 100 через пробел, которые отражают процент ставок после одинарного, двойного и тд краша соответственно\n"
                                                        "Рекомендации: 0 5 28 95 100", reply_markup=markup_reply)
            bot.register_next_step_handler(message, set_crashes, data)

# Получает от пользователя данные о процентах ставок после крашей
def set_crashes(message, st_data):
    try:
        bets = [int(x) for x in message.text.split()]
        if len(bets) != 5:
            message = bot.send_message(message.chat.id, "Вы ввели данные неверно, попробуйте еще раз")
            bot.register_next_step_handler(message, set_crashes, st_data)
        else:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_fail = types.KeyboardButton('csgo.fail')
            item_band = types.KeyboardButton('csgo.band')
            markup_reply.add(item_fail, item_band)
            message = bot.send_message(message.chat.id, "Осталось пару шагов\nВыберите сайт, на котором хотите ставить", reply_markup=markup_reply)
            bot.register_next_step_handler(message, set_site, bets, st_data)
    except Exception:
        message = bot.send_message(message.chat.id, "Вы ввели данные неверно, попробуйте еще раз", reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, set_crashes, st_data)

# Получает данные о выборе сайта пользователем
def set_site(message, bets, st_data):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_pillow = types.KeyboardButton('0')
    markup_reply.add(item_pillow)
    if message.text == 'csgo.fail':
        site = 'fail'
        msg = bot.send_message(message.chat.id,"Теперь введите подушку безопасности (сумма, которой вы не готовы рисковать)\nСоветуем поставить значение 0", reply_markup=markup_reply)
        bot.register_next_step_handler(msg, set_pillow, site, bets, st_data)
    elif message.text == 'csgo.band':
        site = 'band'
        msg = bot.send_message(message.chat.id, "Теперь введите подушку безопасности (сумма, которой вы не готовы рисковать)\nСоветуем поставить значение 0", reply_markup=markup_reply)
        bot.register_next_step_handler(msg, set_pillow, site, bets, st_data)
    else:
        m = bot.send_message(message.chat.id, "Выберите сайт из предложенных")
        bot.register_next_step_handler(m, set_site, bets, st_data)

# Получает от пользователя значение подушки безопасности
def set_pillow(message, site, bets, st_data):
    try:
        pillow = float(message.text)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_type1 = types.KeyboardButton('Статический')
        item_type2 = types.KeyboardButton('Динамический')
        markup_reply.add(item_type1, item_type2)
        msg = bot.send_message(message.chat.id, "Остался последний шаг, укажите тип ставок", reply_markup=markup_reply)
        bot.register_next_step_handler(msg, set_type, pillow, site, bets, st_data)
    except Exception:
        message = bot.send_message(message.chat.id, "Вы ввели не число, попробуйте еще раз")
        bot.register_next_step_handler(message, set_pillow, site, bets, st_data)

# Получает от пользователя значение типа ставок
def set_type(message, pillow, site, bets, st_data):
    end_text = "Фух... Настройка завершена, теперь вы можете воспользоваться ботом\n" \
               "Остальные функции можно настроить отдельно"
    if message.text.lower() == 'статический':
        type = 'st'
        bot.send_message(message.chat.id, end_text, reply_markup=hide_reply_keyboard)
        add_to_table(type, pillow, site, bets, st_data, message.chat.id)
        m = bot.send_message(message.chat.id, menu_message)
        bot.register_next_step_handler(m, menu)
    elif message.text.lower() == 'динамический':
        type = 'dn'
        bot.send_message(message.chat.id, end_text, reply_markup=hide_reply_keyboard)
        add_to_table(type, pillow, site, bets, st_data, message.chat.id)
        m = bot.send_message(message.chat.id, menu_message)
        bot.register_next_step_handler(m, menu)
    else:
        message = bot.send_message(message.chat.id, "Выберите один из предложенных вариантов")
        bot.register_next_step_handler(message, set_type, pillow, site, bets, st_data)

# Добавляет все введенные пользователем данные в таблицу
def add_to_table(type, pillow, site, bets, st_data, id):
    row = base.max_row + 1
    base[row][0].value = str(id)
    base[row][1].value = st_data[0]
    base[row][2].value = st_data[1]
    base[row][3].value = 'none'
    base[row][4].value = type
    for i in range (5, 10):
        base[row][i].value = bets[i-5]
    base[row][12].value = pillow
    base[row][13].value = site
    book.save("base.xlsx")
    time.sleep(1)

bot.polling(none_stop=True, interval=0.5)
