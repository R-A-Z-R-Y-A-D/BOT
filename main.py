import csv
import telebot
from classes import *

login = ''
password = ''

msg = "Вот список доступных комманд:\n" \
      "/steam_data - получить установленные данные Steam"

def menu(message):
    if message.text == '/steam_data':
        send_steam_data(message)
    else:
        pass

@bot.message_handler(commands=['start'])
def getting_start(message):
    if find_user_in_base(message.chat.id) == 0:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('Начать')
        markup_reply.add(item_start)
        bot.send_message(message.chat.id, "Нажми на кнопку, чтобы запустить бота", reply_markup=markup_reply)
    else:
        message = bot.send_message(message.chat.id, msg, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, menu)

@bot.message_handler(commands=['steam_data'])
def send_steam_data(message):
    us = find_user_in_base(message.chat.id)
    if us == 0 or base[us][1].value == None and base[us][2].value == None:
        bot.send_message(message.chat.id, "Запрашиваемые данные не обнаружены")
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_yes = types.KeyboardButton('Хочу')
        item_no = types.KeyboardButton('Нет')
        markup_reply.add(item_yes, item_no)
        time.sleep(1)
        message = bot.send_message(message.chat.id, "Хотите указать их?", reply_markup=markup_reply)
        bot.register_next_step_handler(message, register_again)
    else:
        bot.send_message(message.chat.id, "<b>Логин Steam:</b> " + str(base[us][1].value)+"\n<b>Пароль Steam:</b> " + str(base[us][2].value))
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_yes = types.KeyboardButton('Да')
        item_no = types.KeyboardButton('Нет')
        markup_reply.add(item_yes, item_no)
        time.sleep(1)
        message = bot.send_message(message.chat.id, "Хотите изменить их?", reply_markup=markup_reply)
        bot.register_next_step_handler(message, register_again)

@bot.message_handler(content_types=['text'])
def start_bot(message):
    if message.text.lower() == "начать":
        bot.send_message(message.chat.id,"Здравствуйте, вы активировали бота, который поможет вам полностью автоматизировать"
                                         " ваши ставки на сайтах csgo.fail, csgo.band!\n"
                                         "Для начала давайте настроим бота (эти параметры можно будет изменить в любой момент).")
        base[base.max_row + 1][0].value = message.chat.id
        set_settings(message)
    elif message.text.lower() == "стоп":
        try:
            users[message.chat.id].stop_prog()
        except StopProgramm:
            try:
                del users[message.chat.id]
                bot.send_message(message.chat.id, "Бот остановлен\nПерезапустите его командой /begin")
            except KeyError:
                pass
    else:
        pass

#возвращает номер строки в результате поиска пользователя по id
def find_user_in_base (rubish):
    for row in range(1, base.max_row+1):
        if str(base[row][0].value) == str(rubish):
            return row
        elif row == base.max_row:
            return 0

#подписывает первую строку таблицы (названия столбцов)
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

#Записывает данные ставок в таблицу
def set_settings(message):
    row = find_user_in_base(message.chat.id)
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_yes = types.KeyboardButton('Динамический')
    item_no = types.KeyboardButton('Статический')
    markup_reply.add(item_yes, item_no)
    bot.send_message(message.chat.id, "Введите тип баланса (сейчас поясню):\n"
                                      "Ставки будут производиться в процентах баланса (когда от нынешнего баланса вы ставите какую-либо часть), "
                                      "либо они будут зафиксированы (в независимости от размера баланса вы будете ставить одну и ту же сумму, "
                                      "конечно же непривосходящую баланс)\n"
                                      "Динамический баланс позволит вам быстро поднятся, но с ним вы рискуете проиграть почти все\n"
                                      "Статический баланс позволит вам уверенно подниматься, но этот процесс займет больше времени", reply_markup=markup_reply)
    bot.register_next_step_handler(message, set_balance)

#Заносит в таблицу данные о типе ставок
def set_balance(message):
    row = find_user_in_base(message.chat.id)
    if message.text.lower() == 'динамический':
        base[row][4].value = 'D'
        bot.send_message(message.chat.id, "Т", reply_markup=hide_reply_keyboard)

    elif message.text.lower() == 'статический':
        base[row][4].value = 'S'
        bot.send_message(message.chat.id, "Т", reply_markup=hide_reply_keyboard)

    book.save("base.xlsx")

#Изменяет старые данные пользователя
def change_old_user(message):
    us = find_user_in_base(message.chat.id)
    logs = [str(x) for x in message.text.split(' ')]
    base[us][1].value = logs[0]
    base[us][2].value = logs[1]
    book.save("base.xlsx")
    message = bot.send_message(message.chat.id, 'Данные сохранены\n' + msg, reply_markup=hide_reply_keyboard)
    bot.register_next_step_handler(message, menu)

#Регистрирует нового пользователя
def register_user(message):
    base[base.max_row+1][0].value=str(message.chat.id)
    logs = [str(x) for x in message.text.split(' ')]
    base[base.max_row][1].value = logs[0]
    base[base.max_row][2].value = logs[1]
    book.save("base.xlsx")
    message = bot.send_message(message.chat.id, 'Данные сохранены\n' + msg, reply_markup=hide_reply_keyboard)
    bot.register_next_step_handler(message, menu)

#Получает ответ от пользователя, хочет ли он изменить свои данные
def register_again(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, "Введите данные Steam, логин и пароль, через пробел", reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, change_old_user)
    elif message.text.lower() == 'хочу':
        bot.send_message(message.chat.id, "Введите данные Steam, логин и пароль, через пробел",reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, register_user)
    else:
        message = bot.send_message(message.chat.id, msg, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, menu)

#Перенаправляет к функции изменения дефолтных настроек или запускает бота
def change_defolt(message):
    if message.text.lower() == "да":
        pass
    elif message.text.lower() == "нет":
        with open("table.csv", newline='') as table:
            reader = csv.DictReader(table, delimiter=';')
            for row in reader:
                if row['user_id'] == str(message.chat.id):
                    login = row['steam_login']
                    password = row['steam_password']
        bot.send_message(message.chat.id, "Бот запущен\nНапечатайте <b>стоп</b>, чтобы остановить его", reply_markup=hide_reply_keyboard)
        try:
            users[message.chat.id] = CSGO_BAND(login=login, password=password, chat_id=message.chat.id)
            users[message.chat.id].pre_autorisation()
            bot.register_next_step_handler(message, code_add)
        except Exception:
            try:
                del users[message.chat.id]
                bot.send_message(message.chat.id, "Бот остановлен\nПерезапустите его командой /start")
            except KeyError:
                pass
    else:
        pass

#Добавляет код в объект класса
def code_add(message):
    try:
        if message.text.lower() == "стоп":
            users[message.chat.id].stop_prog()
        else:
            users[message.chat.id].data['code'] = message.text
            users[message.chat.id].autorisation()
            users[message.chat.id].autorisation_check()
    except Exception:
        try:
            del users[message.chat.id]
            bot.send_message(message.chat.id, "Бот остановлен\nПерезапустите его командой /start")
        except KeyError:
            pass


bot.polling(none_stop=True, interval=0.5)
