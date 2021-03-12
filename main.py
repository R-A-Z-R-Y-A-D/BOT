from classes import *
from func import *
from config import *

# a = 0
# @bot.message_handler(commands=['start'])
# def getting_start(message):
#     global a
#     array = ['Velocycle0', 'aSdFtGy160505', [0.1, 0.28, 0.39, 0.95, 1], '1.2', 0, 1, admins['bub']]
#     a = CsFail(array)
#     a.autirisation()
#     a.autorisation_check()
#     print('ok')
#
# @bot.message_handler(content_types=['text'])
# def get_any_text(message):
#     a.data['code'] = message.text

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

@bot.message_handler(content_types=['text'])
def get_any_text(message):
    if message.text.lower() == 'стоп' and users[str(message.chat.id)] != None:
        users[str(message.chat.id)].stop_prog()
    elif len(message.text) == 5:
        count = 0
        rus = set('аоуыэяеёюибвгдйжзклмнпрстфхцчшщ')
        for i in range(5):
            if message.text[i] in rus:
                count = 1
                break
        if count == 0:
            users[str(message.chat.id)].data['code'] = message.text


bot.polling(none_stop=True, interval=0.5)