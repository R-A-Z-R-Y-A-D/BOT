import telebot
import os
import time
from selenium import webdriver
from time import strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

TOKEN='1605123545:AAFnWDyHOh9_CJXNjEpX5UlX04MTHdBPFJE'
bot = telebot.TeleBot(TOKEN)
perc=[0,0.05,0.3,0.95,1]
podushka=[0]
type=[1]
id={'login':"spiviksj", 'password':"FghJJhgF16052659"}
welcome_text="Привет 🥰." \
             "С этим ботом ты сможешь автоматизировать свои ставки на csgo-крашах.\n" \
             "Вот несколько доступных команд:\n\n" \
             "/begin - запустить бота с текущими настройками\n" \
             "/list - просмотреть список текущих настроек\n" \
             "/set_crash - изменить настройки ставок\n" \
             "/set_type - изменить тип ставок\n" \
             "/set_user - указать данные Steam\n" \
             "/set_save - изменить несгораемую сумму" \

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('1', '2', '3')

def primary():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("http://cs.fail")

        def crash(n):
            string = "[class='xhistory__content ng-star-inserted'] :nth-child(" + str(n) + ")"
            button = float(driver.find_element(By.CSS_SELECTOR, string).text[:-1])
            return button

        def autorization():
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_size_2 btn_success2']"))).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamAccountName']"))).send_keys(id['login'])
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamPassword']"))).send_keys(id['password'])
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='imageLogin']"))).click()
            @bot.message_handler(content_types=['text'])
            def count_guard(message):
                code=message.text
                WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(code)
            time.sleep(60)
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
            print("Авторизация пройдена")
        def click(n):
            for i in range(n):
                time.sleep(0.4)
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='inventory__toggle'] > label"))).click()

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

        autorization()

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

        if type[0] == 1:
            a = crash(1)
            while a < 1.2:
                a = crash(1)
            while True:
                time.sleep(0.5)
                last = crash(1)
                if last < 1.2:
                    check(0, 0)
                    a = crash(2)
                    while a >= 1.2:
                        a = crash(2)
                    lastcheck = crash(1)

                    if lastcheck < 1.2:
                        check(1, 0)
                        a = crash(3)
                        while a >= 1.2:
                            a = crash(3)
                        last1check = crash(1)

                        if last1check < 1.2:
                            check(2, 0)
                            a = crash(4)
                            while a >= 1.2:
                                a = crash(4)
                            last2check = crash(1)

                            if last2check < 1.2:
                                check(3, 0)
                                a = crash(5)
                                while a >= 1.2:
                                    a = crash(5)
                                last3check = crash(1)

                                if last3check < 1.2:
                                    check(4, 0)
                                    a = crash(6)
                                    while a >= 1.2:
                                        a = crash(6)
                                    last4check = crash(1)

                                    if last4check < 1.2:
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

        if type[0] == 2:
            a = crash(1)
            while a < 1.2:
                a = crash(1)
            while True:
                time.sleep(0.5)
                last = crash(1)
                if last < 1.2:
                    bal = balance()
                    check(0, bal)
                    a = crash(2)
                    while a >= 1.2:
                        a = crash(2)
                    lastcheck = crash(1)

                    if lastcheck < 1.2:
                        check(1, bal)
                        a = crash(3)
                        while a >= 1.2:
                            a = crash(3)
                        last1check = crash(1)

                        if last1check < 1.2:
                            check(2, bal)
                            a = crash(4)
                            while a >= 1.2:
                                a = crash(4)
                            last2check = crash(1)

                            if last2check < 1.2:
                                check(3, bal)
                                a = crash(5)
                                while a >= 1.2:
                                    a = crash(5)
                                last3check = crash(1)

                                if last3check < 1.2:
                                    check(4, bal)
                                    a = crash(6)
                                    while a >= 1.2:
                                        a = crash(6)
                                    last4check = crash(1)

                                    if last4check < 1.2:
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
    finally:
        @bot.message_handler(commands=['status'])
        def send_welcome(message):
            bot.send_message(message.chat.id, "Бот завершил работу")
        driver.quit()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['list'])
def send_list(message):
    list_text=f"Ставки:\n" \
              f"Одинарный - {str(round(perc[0]*100))}%\n" \
              f"Двойной - {str(round(perc[1]*100))}%\n" \
              f"Тройной - {str(round(perc[2]*100))}%\n" \
              f"Четверной - {str(round(perc[3]*100))}%\n" \
              f"Пятерной - {str(round(perc[4]*100))}%\n\n" \
              f"Подушка безопасности:\n" \
              f"{podushka[0]}$\n\n" \
              f"Тип ставок:\n" \
              f"{'Динамический' if type[0]==1 else 'Статический'}\n\n" \
              f"Авторизован как {id['login']}"
    bot.send_message(message.chat.id, list_text)

@bot.message_handler(commands=['set_crash'])
def make_new_list(message):
    bot.send_message(message.chat.id, "Введи 5 чисел от 0 до 100 через пробел:")
    @bot.message_handler(content_types=['text'])
    def count_text(message):
        str=message.text+" "
        str1 = [x for x in str]
        try:
            j = 0
            new = ["", "", "", "", ""]
            for i in range(5):
                while str1[j] != " ":
                    new[i] += str1[j]
                    str1.pop(j)
                j += 1
                perc[i] = round(float(new[i]) / 100, 2)
        except ValueError:
            bot.send_message(message.chat.id, "Некорректный формат ввода")

@bot.message_handler(commands=['set_type'])
def make_new_type(message):
    bot.send_message(message.chat.id, "Введи тип ставок:\n1. Динамический\n2. Статический")
    @bot.message_handler(content_types=['text'])
    def count_type(message):
        type_type=message.text
        try:
            type[0]=int(type_type)
        except ValueError:
            bot.send_message(message.chat.id, "Некорректный формат ввода")

@bot.message_handler(commands=['set_save'])
def make_new_save(message):
    bot.send_message(message.chat.id, "Введи несгораемую сумму:")
    @bot.message_handler(content_types=['text'])
    def count_save(message):
        save=message.text
        try:
            podushka[0]=int(save)
        except ValueError:
            bot.send_message(message.chat.id, "Некорректный формат ввода")

@bot.message_handler(commands=['set_user'])
def make_new_user(message):
    bot.send_message(message.chat.id, "Введи логин и пароль от аккаунта Steam через пробел:")
    @bot.message_handler(content_types=['text'])
    def user(message):
        usr=message.text+" "
        usr = [x for x in usr]
        try:
            i=0
            id['login']=""
            id['password']=""
            while usr[i]!=" ":
                id['login']+=usr[i]
                i+=1
            i+=1
            while usr[i] != " ":
                id['password'] += usr[i]
                i+=1
        except ValueError:
            bot.send_message(message.chat.id, "Некорректный формат ввода")

@bot.message_handler(commands=['begin'])
def begin(message):
    bot.send_message(message.chat.id, "Бот запущен\nВведите код Steam Guard:")
    primary()

# reply_markup=keyboard1
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling(none_stop=True, interval=0)