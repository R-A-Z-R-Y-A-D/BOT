import csv
from classes import *

msg = "Вот список доступных комманд:\n" \
      "/steam_data - получить установленные данные Steam"

def admin_check(id):
    for i in admins:
        if str(admins[i]) == str(id):
            return True
    return False

def menu(message):
    if message.text == '/steam_data':
        send_steam_data(message)
    if message.text == '/analytics' and admin_check(message.chat.id):
        pass
    else:
        pass

@bot.message_handler(commands=['start'])
def getting_start(message):
    if find_user_in_base(message.chat.id) == 0:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('НАЧАТЬ')
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
        msg = 'hgjgf'
        bot.send_message(message.chat.id,msg)
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
        bot.send_message(message.chat.id,
                         "А теперь последовательно введите ставки (начиная со ставки после одинарного краша и заканчивая ставкой после пятерного).\n"
                         "Обратите внимание, что в динамическом балансе ставки измеряются в процентах. "
                         "Значение '100' будет означать, что бот поставит весь допустимый для ставок баланс.\n"
                         "Вводить ставки следует в отдельнх сообщениях. "
                         "При вводе нецелого числа, дробную часть отделять точкой.", reply_markup=hide_reply_keyboard)


    elif message.text.lower() == 'статический':
        base[row][4].value = 'S'
        bot.send_message(message.chat.id,
                         "А теперь последовательно введите ставки (начиная со ставки после одинарного краша и заканчивая ставкой после пятерного).\n"
                         "Обратите внимание, что в статическом балансе ставки измеряются в долларах. "
                         "Если ставка будет превышать доступный для пользования ботом баланс, бот остановит свою работу. \n"
                         "Вводить ставки следует в отдельнх сообщениях. "
                         "При вводе нецелого числа, дробную часть отделять точкой.", reply_markup=hide_reply_keyboard)

    book.save("base.xlsx")
    message.text = ''
    bot.register_next_step_handler(message, wait_float)


def wait_float(message):  # функция будет работать до тех пор, пока пользователь не введет float
    a = message.text
    try:
        print(a)
        float(a)
        print(a)
        set_bets(message, a)
    except ValueError:
        print("Текст = 0")
        bot.send_message(message.chat.id, "Неверный формат ввода")
        bot.register_next_step_handler(message, wait_float)



def set_bets(message, bet):
    print("here")
    row = find_user_in_base(message.chat.id)
    i = 4
    while base[row][9].value == None:
        base[row][i].value = bet
        book.save("base.xlsx")
        i+=1
        wait_float(message)

    if base[row][10].value == None:
        message.text = ''
        bot.send_message(message.chat.id,
                         "Введенное значение - " + str(bet) + ". Введите значение следующей ставки.")
        bot.register_next_step_handler(message, set_bets)
    else:
        bot.send_message(message.chat.id, "Ваши ставки от первой до последней:")
        for rubish in base.iter_cols(min_col=6, max_col=10, min_row=row, max_row=row):
            for cell in rubish:
                bot.send_message(message.chat.id, cell.value)
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
