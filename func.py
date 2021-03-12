from telebot import types
from config import *
from classes import *
import time

menu_message = 'Список доступных комманд:\n' \
               '/steam_data - показать сохраненные данные Steam\n' \
               '/help - получить справку по всем настройкам\n' \
               '/get_data - получить все сохраненные данные по ставкам\n' \
               '/begin - запустить бота с текущими настройками\n' \
               '/re_autorisation - изменить данные по ставкам'

# Обрабатывает комманды из меню
def menu(message):
    if message.text == '/steam_data':
        send_steam_data(message)
    elif message.text == '/analytics' and admin_check(message.chat.id):
        pass
    elif message.text == '/get_data':
        send_table_data(message, message.chat.id)
    elif message.text == '/help':
        send_inf(message)
    elif message.text == '/re_autorisation':
        row = find_user_in_base(message.chat.id)
        data = [base[row][1].value, base[row][2].value]
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('0 5 28 95 100')
        markup_reply.add(item)
        message = bot.send_message(message.chat.id,
                                   "Введите 5 чисел от 0 до 100 через пробел, которые отражают процент "
                                   "ставок после одинарного, двойного и тд краша соответственно\n"
                                   "Рекомендации: 0 5 28 95 100",
                                   reply_markup=markup_reply)
        bot.register_next_step_handler(message, set_crashes, data)
    elif message.text == '/begin':
        if not str(message.chat.id) in users:
            msg = "Бот запущен, напечатайте <b>стоп</b>, чтобы остановить его\n" \
                  "Введите код Steam Guard как только мы вас попросим"
            bot.send_message(message.chat.id, msg)
            start_programm(message, message.chat.id)
        else:
            bot.send_message(message.chat.id, "Одновременно может работать только один бот")
            bot.register_next_step_handler(message, menu)
    else:
        pass

# Отсылает пользователю сохраненные в таблице данные Steam
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

# Отправляет пользователю его данные из таблицы
def send_table_data(message, id):
    row = find_user_in_base(id)
    arr = get_data_from_table(id)
    bets = ''
    for i in range(5):
        bets += str(round(arr['bets'][i] * 100)) + '% '
    msg = f"Статус оплаты {'<b>Не оплачено</b>' if arr['status'] == 'none' else '<b>Оплачено</b>'}\n\n" \
          f"Тип баланса <b>{arr['type']}</b>\n" \
          f"Ставки {'<b>' + bets + '</b>'}\n" \
          f"Несгораемая сумма <b>{arr['podushka']} $</b>\n" \
          f"Выбранный сайт <b>{arr['site']}</b>"
    bot.send_message(int(base[row][0].value), msg)
    bot.register_next_step_handler(message, menu)

# Получает все данные пользователя по его id
def get_data_from_table(id):
    row = find_user_in_base(str(id))
    arr = {}
    bets = []
    arr['id'] = str(id)
    arr['login'] = base[row][1].value
    arr['password'] = base[row][2].value
    arr['status'] = base[row][3].value
    arr['type'] = base[row][4].value
    for i in range(5):
        bets.append(round(float(base[row][i+5].value)/100, 2))
    arr['bets'] = bets
    arr['stairs'] = base[row][10].value
    arr['fix_bet'] = base[row][11].value
    arr['podushka'] = float(base[row][12].value)
    arr['site'] = base[row][13].value
    return arr

# Отправляет информацию по настройкам через команду "/help"
def send_inf(message):
    message = bot.send_message(message.chat.id, 'Пока тут пусто')
    bot.register_next_step_handler(message, menu)

# Запускает программу
def start_programm(message, id):
    arr = get_data_from_table(id)
    if arr['status'] != 'none':
        pass
    else:
        if arr['type'] == 'Динамический':
            type = 1
        elif arr['type'] == 'Статический':
            type = 2
        array = [arr['login'], arr['password'], arr['bets'], arr['fix_bet'], arr['podushka'], type, arr['id']]
        if arr['site'] == 'csgo.band':
            users[str(id)] = CsgoBand(array)
            users[str(id)]()
        if arr['site'] == 'cs.fail':
            users[str(id)] = CsFail(array)
            users[str(id)]()

# Принимает ответ от пользователя, хочет он изменить свои данные или нет
def register_again(message):
    if message.text.lower() == 'нет':
        message = bot.send_message(message.chat.id, menu_message, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, menu)
    elif message.text.lower() == 'да':
        message = bot.send_message(message.chat.id, 'Введите ваши данные Steam, логин и пароль, через пробел', reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, add_st_data_to_table)



def admin_check(id):
    for i in admins:
        if str(admins[i]) == str(id):
            return True
    return False

def find_user_in_base (id):
    for row in range(1, base.max_row+1):
        if str(base[row][0].value) == str(id):
            return row
    return False



# Отсылает к функции сбора данных Steam
def make_new_user(message):
    if message.text.lower() == 'начать':
        welcome_text = "Здравствуйте.\n" \
                       "Вы активировали бота, который поможет вам полностью автоматизировать" \
                       "ваши ставки на сайтах cs.fail, csgo.band!\n" \
                       "Бот имеет огромные возможности, связанные с автоматизацией ставой,\n" \
                       "которые будут только улучшаться с каждым обновлением\n" \
                       "Для начала давайте настроим бота (эти параметры можно будет изменить в любой момент)\n" \
                       "Введите ваши данные Steam, логин и пароль через пробел"
        message = bot.send_message(message.chat.id, welcome_text, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, add_st_data_to_table, index=1)

# Изменяет старые данные для зарегистрированного пользователя или
# Перенаправляет нового пользователя в функцию для получения ставок
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
            book.save("base.xlsx")
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
            item_fail = types.KeyboardButton('cs.fail')
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
    if message.text == 'cs.fail':
        site = 'cs.fail'
        msg = bot.send_message(message.chat.id,"Теперь введите подушку безопасности (сумма, которой вы не готовы рисковать)\nСоветуем поставить значение 0", reply_markup=markup_reply)
        bot.register_next_step_handler(msg, set_pillow, site, bets, st_data)
    elif message.text == 'csgo.band':
        site = 'csgo.band'
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
        item_type3 = types.KeyboardButton('КД')
        msg = 'Всего есть несколько возможный стратегий ставок:\n' \
              '1 Со статическим балансом\n' \
              'Это означает, что бот, перед тем как начнется серия крашей,\n' \
              'считывает баланс и затем ставит определенный процент, который вы можете указать при настройке\n' \
              '2 С динамическим балансом\n' \
              'Данный подход подразумевает, что после каждого краша бот считывает баланс и умножает его на процент,\n' \
              'который вы укажете в настройках\n' \
              '3 КД\n' \
              'Это значит, что бот ставит после каждого коэфициента строго определенный процент от баланса\n\n'
        markup_reply.add(item_type1, item_type2, item_type3)
        msg = bot.send_message(message.chat.id, msg, reply_markup=markup_reply)
        bot.register_next_step_handler(msg, set_type, pillow, site, bets, st_data)
    except Exception:
        message = bot.send_message(message.chat.id, "Вы ввели не число, попробуйте еще раз")
        bot.register_next_step_handler(message, set_pillow, site, bets, st_data)

# Получает от пользователя значение типа ставок
def set_type(message, pillow, site, bets, st_data):
    end_text = "Фух... Настройка завершена, теперь вы можете воспользоваться ботом\n" \
               "Остальные функции можно настроить отдельно"
    if message.text.lower() == 'статический':
        type = 'Статический'
        bot.send_message(message.chat.id, end_text, reply_markup=hide_reply_keyboard)
        add_to_table(type, pillow, site, bets, st_data, message.chat.id)
        m = bot.send_message(message.chat.id, menu_message)
        bot.register_next_step_handler(m, menu)
    elif message.text.lower() == 'динамический':
        type = 'Динамический'
        bot.send_message(message.chat.id, end_text, reply_markup=hide_reply_keyboard)
        add_to_table(type, pillow, site, bets, st_data, message.chat.id)
        m = bot.send_message(message.chat.id, menu_message)
        bot.register_next_step_handler(m, menu)
    else:
        message = bot.send_message(message.chat.id, "Выберите один из предложенных вариантов")
        bot.register_next_step_handler(message, set_type, pillow, site, bets, st_data)

# Добавляет все введенные пользователем данные в таблицу
def add_to_table(type, pillow, site, bets, st_data, id):
    row = find_user_in_base(id)
    if not row:
        row = base.max_row + 1
    base[row][0].value = str(id)
    base[row][1].value = st_data[0]
    base[row][2].value = st_data[1]
    base[row][3].value = 'none'
    base[row][4].value = type
    for i in range (5, 10):
        base[row][i].value = bets[i-5]
    base[row][10].value = 'none'
    base[row][11].value = '1.2'
    base[row][12].value = pillow
    base[row][13].value = site
    book.save("base.xlsx")
    time.sleep(1)