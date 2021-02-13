from telebot import types
import telebot
import configure
from time import strftime
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

bot = telebot.TeleBot(configure.config['token'])
type = [0]
perc = ['', '', '', '', '']
podushka = [0]
id = {'login': '', 'password': ''}
hide_reply_keyboard = types.ReplyKeyboardRemove()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://cs.fail")

@bot.message_handler(commands=['start'])
def to_begin(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать')
    markup_reply.add(item_start)
    begin_text = 'Нажми на кнопку, если хочешь запустить бота'
    bot.send_message(message.chat.id, begin_text, reply_markup=markup_reply)


@bot.message_handler(commands=['list'])
def to_begin(message):
    list_text = f"Вот список текущих настроек бота:\n\n" \
                f"Одинарный - {str(perc[0] * 100)} %\n" \
                f"Двойной - {str(perc[1] * 100)} %\n" \
                f"Тройной - {str(perc[2] * 100)} %\n" \
                f"Четверной - {str(perc[3] * 100)} %\n" \
                f"Пятерной - {str(perc[4] * 100)} %\n" \
                f"Несгораемая сумма - {str(podushka[0])} $\n" \
                f"Тип ставок - {'Динамический' if type[0] == 1 else 'Статический'}\n" \
                f"Авторизован как {id['login']}"
    bot.send_message(message.chat.id, list_text)


@bot.message_handler(commands=['begin'])
def start_program(message):
    stpr_text = "Бот запущен, введи код Steam Guard как только он придет"
    bot.send_message(message.chat.id, stpr_text)
    pre_prim()
    bot.register_next_step_handler(message, primary)

def pre_prim():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_size_2 btn_success2']"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamAccountName']"))).send_keys(id['login'])
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamPassword']"))).send_keys(id['password'])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='imageLogin']"))).click()

def primary(message):
    try:
        code = message.text
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(code)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] :nth-child(1)"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[class='xbutton xbutton_icon xbutton_size_x34 xbutton_toggle']"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon volume_icon']"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon icon_settings']"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='control__label']"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xmodal__close']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).clear()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).send_keys(
            "1.2")
        bot.send_message(message.chat.id, "Авторизация пройдена успешно 🤟")

        def crash(n):
            string = "[class='xhistory__content ng-star-inserted'] :nth-child(" + str(n) + ")"
            button = float(driver.find_element(By.CSS_SELECTOR, string).text[:-1])
            return button

        def click(n):
            for i in range(n):
                time.sleep(0.4)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='form__checkbox xswitch xswitch_primary xswitch_small xswitch_md_mini']"))).click()

        def balance():
            save = driver.find_elements(By.CSS_SELECTOR, "[class='inventory__count symbol_usd']")
            vyb = float(save[0].text)
            bal = float(save[1].text)
            return bal + vyb

        def start():
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[class='btn btn_block btn_size_create btn_purple ng-star-inserted']"))).click()

        def zakup(bal, pc):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[class='btn btn_block btn_size_2 btn_default4']"))).click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).clear()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(
                str(round((bal - podushka[0]) * pc, 2)))
            time.sleep(1)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='skins skins_for_window'] :nth-child(1)"))).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_block xbutton_buy']"))).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='shop__close']"))).click()

        def watch():
            time.sleep(1)
            try:
                driver.find_element(By.CSS_SELECTOR, "[class='skins skins_for_inventory'] > div")
                return True
            except NoSuchElementException:
                return False

        def check(n, bal):
            if perc[n] != 0:
                click(1)
                if type[0] == 1:
                    bal = balance()
                zakup(bal, perc[n])
                click(2)
                start()
                save = watch()
                if save == True:
                    bot.send_message(message.chat.id, "Бот не сделал ставку")
                else:
                    bot.send_message(message.chat.id, strftime("%Y-%m-%d %H:%M:%S"))

        check_perc = 0
        bal = balance()
        for i in perc:
            if i > 0:
                check_perc = i
                break
        if bal*check_perc < 0.25:
            raise IOError("Пополните баланс")

        click(2)

        a = crash(1)
        while a < 1.2:
            a = crash(1)
        while True:
            time.sleep(0.5)
            last = crash(1)
            if last < 1.2:
                if type[0] == 1:
                    check(0, 0)
                else:
                    bal = balance()
                    check(0, bal)
                a = crash(2)
                while a >= 1.2:
                    a = crash(2)
                lastcheck = crash(1)

                if lastcheck < 1.2:
                    if type[0] == 1:
                        check(1, 0)
                    else:
                        bal = balance()
                        check(1, bal)
                    a = crash(3)
                    while a >= 1.2:
                        a = crash(3)
                    last1check = crash(1)

                    if last1check < 1.2:
                        if type[0] == 1:
                            check(2, 0)
                        else:
                            bal = balance()
                            check(2, bal)
                        a = crash(4)
                        while a >= 1.2:
                            a = crash(4)
                        last2check = crash(1)

                        if last2check < 1.2:
                            if type[0] == 1:
                                check(3, 0)
                            else:
                                bal = balance()
                                check(3, bal)
                            a = crash(5)
                            while a >= 1.2:
                                a = crash(5)
                            last3check = crash(1)

                            if last3check < 1.2:
                                if type[0] == 1:
                                    check(4, 0)
                                else:
                                    bal = balance()
                                    check(4, bal)
                                a = crash(6)
                                while a >= 1.2:
                                    a = crash(6)
                                last4check = crash(1)

                                if last4check < 1.2:
                                    bot.send_message(message.chat.id, "Шестерной краш")
                                    break

                                else:
                                    if perc[4] != 0:
                                        click(1)

                            else:
                                if perc[3] != 0:
                                    click(1)

                        else:
                            if perc[2] != 0:
                                click(1)

                    else:
                        if perc[1] != 0:
                            click(1)

                else:
                    if perc[0] != 0:
                        click(1)
    except OSError:
        bot.send_message(message.chat.id, "На твоем балансе недостаточно средств")
    finally:
        bot.send_message(message.chat.id, "Возникла ошибка, бот завершил работу")
        driver.quit()

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'начать':
        start_text = "Привет 😜\n" \
                     "Перед тем как запустить бота необходимо сделать некоторые настройки,\n" \
                     "чтобы бот работал корректно. Это не займет больше двух минут.\n\n" \
                     "Введи пять чисел от 0 до 100 через пробел, отражающие процент ставок:\n" \
                     "(наши рекомендации: 0 5 30 95 100)"
        bot.send_message(message.chat.id, start_text, reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, get_perc)


def get_perc(message):
    str = [x for x in message.text + ' ']
    global perc
    j = 0
    for i in range(5):
        while str[j] != " ":
            perc[i] += str[j]
            j += 1
        j += 1
        perc[i] = round(float(perc[i]) / 100, 2)
    perc_text = "Отлично! 👍\n" \
                "Теперь введи несгораемую сумму на случай,\n" \
                "если тебе не хочется рисковать всем балансом"
    bot.send_message(message.chat.id, perc_text)
    bot.register_next_step_handler(message, get_podushka)

def get_podushka(message):
    global podushka
    podushka[0] = float(message.text)
    podushka_text = "Теперь выбери тип ставок:\n\n" \
                    "1.Динамический\n" \
                    "2.Статический"
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_dynamic = types.KeyboardButton('1')
    item_static = types.KeyboardButton('2')
    markup_reply.add(item_dynamic, item_static)
    bot.send_message(message.chat.id, podushka_text, reply_markup=markup_reply)
    bot.register_next_step_handler(message, get_type)

def get_type(message):
    global type
    type[0] = float(message.text)
    text_st = "Введи свои данные Steam, логин и пароль, через пробел"
    bot.send_message(message.chat.id, text_st, reply_markup=hide_reply_keyboard)
    bot.register_next_step_handler(message, get_user)

def get_user(message):
    data = [x for x in message.text + ' ']
    i=0
    global id
    id['login'] = ''
    id['password'] = ''
    while data[i] != ' ':
        id['login'] += data[i]
        i+=1
    i+=1
    while data[i] != ' ':
        id['password'] += data[i]
        i+=1
    type_text = "Настройка завершена, теперь тебе доступны следующие команды:\n\n" \
                "/list - просмотреть текущие настройки\n" \
                "/start - пройти авторизацию заново\n" \
                "/begin - запустить бота"
    bot.send_message(message.chat.id, type_text)


bot.polling(none_stop=True, interval=0)
