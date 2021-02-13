import os
import csv
import telebot
from telebot import types
import time
import requests
from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

token = '1622405338:AAHkL_FBzftlUe2DYtA-cQQ9JRKSt_qpmCc'
admin_id = 830130638
bot = telebot.TeleBot(token, parse_mode="HTML")
hide_reply_keyboard = types.ReplyKeyboardRemove()

login = ''
password = ''
users = {}

class StopProgramm(Exception):
    pass

class CSGO_BAND:

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("window-size=1920x1080")

    data = {
        'login': '',
        'password': '',
        'perc': [0, 0, 0, 0, 0],
        'podushka': 0,
        'type': 1,
        'id': '',
        'code': ''
    }

    def __init__(self, login='', password='', perc=[0, 0.1, 0.6, 0.95, 1], podushka=0, type=1, chat_id=''):
        self.data['login'] = login
        self.data['password'] = password
        self.data['perc'] = perc
        self.data['podushka'] = podushka
        self.data['type'] = type
        self.data['id'] = chat_id
        self.driver = webdriver.Chrome(options=CSGO_BAND.chrome_options)

    def stop_prog(self):
        self.driver.quit()
        raise StopProgramm

    def get_crash(self, n):
        try:
            time.sleep(0.5)
            button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"[class='graph-labels'] :nth-child({n}) > span")))
            return float(button.text[:-1])
        except Exception:
            self.stop_prog()

    def get_code(self):
        save = self.data['code']
        self.data['code'] = ''
        return save

    def pre_autorisation(self):
        try:
            self.driver.get("https://csgo.band/")
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn--green steam-login']"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamAccountName']"))).send_keys(self.data['login'])
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamPassword']"))).send_keys(self.data['password'])
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='imageLogin']"))).click()
            try:
                WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='error_display']")))
                bot.send_message(self.data['id'],
                                 "Вы указали неверные данные Steam, либо при попытке входа появляется CAPTCHA\nПроверьте правильность логина и пароля командой /steam_data")
                self.stop_prog()
            except TimeoutException:
                pass
            bot.send_message(self.data['id'], "Введите код Steam Guard")
        except Exception:
            self.stop_prog()

    def autorisation(self, autocrash='1.2'):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(self.get_code())
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] > div"))).click()
            def enter(self):
                bot.send_message(self.data['id'], "Код неверный, перезапустите бота командой /start")
                # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(self.get_code())
                # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode'] > div"))).click()
                self.stop_prog()
            while True:
                try:
                    WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode']")))
                    enter(self)
                except TimeoutException:
                    break
            # изменение настроек
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn-toggler chat-trigger active']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-sound"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".field-input"))).send_keys(Keys.BACK_SPACE)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".field-input"))).send_keys(autocrash)
        except Exception:
            self.stop_prog()

    def autorisation_check(self):
        save=0
        for i in self.data['perc']:
            if i > 0:
                save=i
                break
        self.click(1)
        bal = self.get_balance()
        self.click(1)
        if save*bal < 0.25:
            bot.send_message(self.data['id'], "На вашем балансе недостаточно средств")
            self.stop_prog()
        else:
            bot.send_message(self.data['id'], "Отлично, на вашем балансе достаточно средств, бот начал работу")
            self.main()

    def click(self, n):
        try:
            for i in range(n):
                time.sleep(0.4)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='checkbox-control__content']"))).click()
        except Exception:
            self.stop_prog()

    def get_balance(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='cur-u-drops-selected']")))
            sel = self.driver.find_element(By.CSS_SELECTOR, "[class='cur-u-drops-selected__selected']").text[2:]
            total = self.driver.find_element(By.CSS_SELECTOR, "[class='cur-u-drops-selected__total']").text[2:]
            return float(sel)+float(total)
        except Exception:
            self.stop_prog()

    def make_bet(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn-base btn btn--blue make-bet']"))).click()
        except Exception:
            self.stop_prog()

    def change(self, part, bal):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn--blue']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='exchange-filter-maxPrice-field']"))).send_keys(Keys.BACK_SPACE*10)
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='exchange-filter-maxPrice-field']"))).send_keys(str(round(part*bal - self.data['podushka'], 2)))
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='withdraw-list__inner'] > button"))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='withdraw-footer'] :nth-child(2)"))).click()
        except Exception:
            self.stop_prog()

    def do_afull_process_dynamic(self, num_of_perc):
        self.click(1)
        self.change(self.data['perc'][num_of_perc], self.get_balance())
        self.click(1)
        time.sleep(3)
        self.make_bet()

    def do_afull_process_static(self, num_of_perc, bal):
        self.click(1)
        self.change(self.data['perc'][num_of_perc], bal)
        self.click(1)
        time.sleep(3)
        self.make_bet()

    def wait_crash(self, n):
        crash_n = self.get_crash(n)
        while crash_n >= 1.2:
            crash_n = self.get_crash(n)
        return self.get_crash(1)

    def main(self):

        if self.data['type'] == 1:
            crash_1 = self.get_crash(1)
            while crash_1 < 1.2:
                crash_1 = self.get_crash(1)
            while True:
                crash_1 = self.get_crash(1)
                if crash_1 < 1.2:
                    if self.data['perc'][0] != 0: self.do_afull_process_dynamic(0)
                    crash_1 = self.wait_crash(2)

                    if crash_1 < 1.2:
                        if self.data['perc'][1] != 0: self.do_afull_process_dynamic(1)
                        crash_1 = self.wait_crash(3)

                        if crash_1 < 1.2:
                            if self.data['perc'][2] != 0: self.do_afull_process_dynamic(2)
                            crash_1 = self.wait_crash(4)

                            if crash_1 < 1.2:
                                if self.data['perc'][3] != 0: self.do_afull_process_dynamic(3)
                                crash_1 = self.wait_crash(5)

                                if crash_1 < 1.2:
                                    if self.data['perc'][4] != 0: self.do_afull_process_dynamic(4)
                                    crash_1 = self.wait_crash(6)

                                    if crash_1 < 1.2:
                                        print("Шестерной краш")
                                        break

        if self.data['type'] == 2:
            crash_1 = self.get_crash(1)
            while crash_1 < 1.2:
                crash_1 = self.get_crash(1)
            while True:
                crash_1 = self.get_crash(1)
                if crash_1 < 1.2:
                    self.click(1)
                    bal = self.get_balance()
                    self.click(1)
                    if self.data['perc'][0] != 0: self.do_afull_process_static(0, bal)
                    crash_1 = self.wait_crash(2)

                    if crash_1 < 1.2:
                        if self.data['perc'][1] != 0: self.do_afull_process_static(1, bal)
                        crash_1 = self.wait_crash(3)

                        if crash_1 < 1.2:
                            if self.data['perc'][2] != 0: self.do_afull_process_static(2, bal)
                            crash_1 = self.wait_crash(4)

                            if crash_1 < 1.2:
                                if self.data['perc'][3] != 0: self.do_afull_process_static(3, bal)
                                crash_1 = self.wait_crash(5)

                                if crash_1 < 1.2:
                                    if self.data['perc'][4] != 0: self.do_afull_process_static(4, bal)
                                    crash_1 = self.wait_crash(6)

                                    if crash_1 < 1.2:
                                        print("Шестерной краш")
                                        break

        if self.data['type'] == 3:
            while True:
                crash_1 = self.get_crash(1)
                crash_2 = self.get_crash(2)
                crash_3 = self.get_crash(3)
                crash_4 = self.get_crash(4)
                while crash_1 == self.get_crash(1) or crash_2 == self.get_crash(2) or crash_3 == self.get_crash(3) or crash_4 == self.get_crash(4):
                    time.sleep(0.1)
                self.do_afull_process_dynamic(0)

class CS_FAIL:

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("window-size=1920x1080")

    data = {
        'login': '',
        'password': '',
        'perc': [0, 0, 0, 0, 0],
        'podushka': 0,
        'type': 1,
        'id': '',
        'code': ''
    }

    def __init__(self, login='', password='', perc=[0, 0.05, 0.3, 0.95, 1], podushka=0, type=1, chat_id=''):
        self.data['login'] = login
        self.data['password'] = password
        self.data['perc'] = perc
        self.data['podushka'] = podushka
        self.data['type'] = type
        self.data['id'] = chat_id
        self.driver = webdriver.Chrome(options=CS_FAIL.chrome_options)

    def stop_prog(self):
        self.driver.quit()
        raise StopProgramm

    def get_crash(self, n):
        try:
            time.sleep(0.5)
            button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"[class='xhistory__content ng-star-inserted'] :nth-child({n})")))
            return float(button.text[:-1])
        except Exception:
            self.stop_prog()

    def get_code(self):
        save = self.data['code']
        self.data['code'] = ''
        return save

    def pre_autorisation(self):
        try:
            self.driver.get("https://csgo.band/")
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_size_2 btn_success2']"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamAccountName']"))).send_keys(self.data['login'])
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamPassword']"))).send_keys(self.data['password'])
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='imageLogin']"))).click()
            try:
                WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='error_display']")))
                bot.send_message(self.data['id'],
                                 "Вы указали неверные данные Steam, либо при попытке входа появляется CAPTCHA\nПроверьте правильность логина и пароля командой /steam_data")
                self.stop_prog()
            except TimeoutException:
                pass
            bot.send_message(self.data['id'], "Введите код Steam Guard")
        except Exception:
            self.stop_prog()

    def autorisation(self, autocrash='1.2'):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(self.get_code())
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] > div"))).click()
            def enter(self):
                bot.send_message(self.data['id'], "Код неверный, перезапустите бота командой /start")
                self.stop_prog()
            while True:
                try:
                    WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode']")))
                    enter(self)
                except TimeoutException:
                    break
            # изменение настроек
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_icon xbutton_size_x34 xbutton_toggle']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon volume_icon']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).clear()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).send_keys(autocrash)
        except Exception:
            self.stop_prog()

    def autorisation_check(self):
        save=0
        for i in self.data['perc']:
            if i > 0:
                save=i
                break
        self.click(1)
        bal = self.get_balance()
        self.click(1)
        if save*bal < 0.25:
            bot.send_message(self.data['id'], "На вашем балансе недостаточно средств")
            self.stop_prog()
        else:
            bot.send_message(self.data['id'], "Отлично, на вашем балансе достаточно средств, бот начал работу")
            self.main()

    def click(self, n):
        try:
            for i in range(n):
                time.sleep(0.4)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xswitch__content']"))).click()
        except Exception:
            self.stop_prog()

    def get_balance(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='inventory__head']")))
            sel = self.driver.find_element(By.CSS_SELECTOR, "[class='inventory__selected'] :nth-child(2)").text
            total = self.driver.find_element(By.CSS_SELECTOR, "[class='inventory__balance'] :nth-child(2)").text
            return float(sel)+float(total)
        except Exception:
            self.stop_prog()

    def make_bet(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_block btn_size_create btn_purple ng-star-inserted']"))).click()
        except Exception:
            self.stop_prog()

    def change(self, part, bal):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_block btn_size_2 btn_default4']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(Keys.BACK_SPACE*10)
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(str(round(part*bal - self.data['podushka'], 2)))
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='skins skins_for_window'] > div"))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_block xbutton_buy']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='shop__close']"))).click()
        except Exception:
            self.stop_prog()

    def do_afull_process_dynamic(self, num_of_perc):
        self.click(1)
        self.change(self.data['perc'][num_of_perc], self.get_balance())
        self.click(1)
        time.sleep(3)
        self.make_bet()

    def do_afull_process_static(self, num_of_perc, bal):
        self.click(1)
        self.change(self.data['perc'][num_of_perc], bal)
        self.click(1)
        time.sleep(3)
        self.make_bet()

    def wait_crash(self, n):
        crash_n = self.get_crash(n)
        while crash_n >= 1.2:
            crash_n = self.get_crash(n)
        return self.get_crash(1)

    def main(self):

        if self.data['type'] == 1:
            crash_1 = self.get_crash(1)
            while crash_1 < 1.2:
                crash_1 = self.get_crash(1)
            while True:
                crash_1 = self.get_crash(1)
                if crash_1 < 1.2:
                    if self.data['perc'][0] != 0: self.do_afull_process_dynamic(0)
                    crash_1 = self.wait_crash(2)

                    if crash_1 < 1.2:
                        if self.data['perc'][1] != 0: self.do_afull_process_dynamic(1)
                        crash_1 = self.wait_crash(3)

                        if crash_1 < 1.2:
                            if self.data['perc'][2] != 0: self.do_afull_process_dynamic(2)
                            crash_1 = self.wait_crash(4)

                            if crash_1 < 1.2:
                                if self.data['perc'][3] != 0: self.do_afull_process_dynamic(3)
                                crash_1 = self.wait_crash(5)

                                if crash_1 < 1.2:
                                    if self.data['perc'][4] != 0: self.do_afull_process_dynamic(4)
                                    crash_1 = self.wait_crash(6)

                                    if crash_1 < 1.2:
                                        print("Шестерной краш")
                                        break

                                    elif self.data['perc'][4] != 0: self.click(1)
                                elif self.data['perc'][3] != 0: self.click(1)
                            elif self.data['perc'][2] != 0: self.click(1)
                        elif self.data['perc'][1] != 0: self.click(1)
                    elif self.data['perc'][0] != 0: self.click(1)

        if self.data['type'] == 2:
            crash_1 = self.get_crash(1)
            while crash_1 < 1.2:
                crash_1 = self.get_crash(1)
            while True:
                crash_1 = self.get_crash(1)
                if crash_1 < 1.2:
                    self.click(1)
                    bal = self.get_balance()
                    self.click(1)
                    if self.data['perc'][0] != 0: self.do_afull_process_static(0, bal)
                    crash_1 = self.wait_crash(2)

                    if crash_1 < 1.2:
                        if self.data['perc'][1] != 0: self.do_afull_process_static(1, bal)
                        crash_1 = self.wait_crash(3)

                        if crash_1 < 1.2:
                            if self.data['perc'][2] != 0: self.do_afull_process_static(2, bal)
                            crash_1 = self.wait_crash(4)

                            if crash_1 < 1.2:
                                if self.data['perc'][3] != 0: self.do_afull_process_static(3, bal)
                                crash_1 = self.wait_crash(5)

                                if crash_1 < 1.2:
                                    if self.data['perc'][4] != 0: self.do_afull_process_static(4, bal)
                                    crash_1 = self.wait_crash(6)

                                    if crash_1 < 1.2:
                                        print("Шестерной краш")
                                        break

                                    elif self.data['perc'][4] != 0: self.click(1)
                                elif self.data['perc'][3] != 0: self.click(1)
                            elif self.data['perc'][2] != 0: self.click(1)
                        elif self.data['perc'][1] != 0: self.click(1)
                    elif self.data['perc'][0] != 0: self.click(1)

        if self.data['type'] == 3:
            i = 0
            while True:
                if i != 0:
                    self.click(1)
                else:
                    i = 1
                crash_1 = self.get_crash(1)
                crash_2 = self.get_crash(2)
                crash_3 = self.get_crash(3)
                crash_4 = self.get_crash(4)
                while crash_1 == self.get_crash(1) or crash_2 == self.get_crash(2) or crash_3 == self.get_crash(3) or crash_4 == self.get_crash(4):
                    time.sleep(0.1)
                self.do_afull_process_dynamic(0)

defolt = "Дефолтные настройки бота:\n\n" \
         "<b>Подушка</b> - 0$\n" \
         "<b>Одинарный</b> - 0%\n" \
         "<b>Двойной</b> - 10%\n" \
         "<b>Тройной</b> - 60%\n" \
         "<b>Четверной</b> - 95%\n" \
         "<b>Пятерной</b> - 100%\n" \
         "<b>Тип ставок</b> - Динамический\n" \
         "<b>Сайт</b> - csgo.band\n\n"

@bot.message_handler(commands=['start'])
def getting_start(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать')
    markup_reply.add(item_start)
    bot.send_message(message.chat.id, "Нажми на кнопку, чтобы запустить бота", reply_markup=markup_reply)

@bot.message_handler(commands=['steam_data'])
def send_steam_data(message):
    with open("table.csv", newline='') as table:
        reader = csv.DictReader(table, delimiter=';')
        i = 0
        for row in reader:
            if row['user_id'] == str(message.chat.id):
                bot.send_message(message.chat.id, f"Логин - {row['steam_login']}, пароль - {row['steam_password']}")
                i = 1
        if i == 0:
            bot.send_message(message.chat.id, "Бот не нашел запрашиваемые данные")
        else:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_yes = types.KeyboardButton('Да')
            item_no = types.KeyboardButton('Нет')
            markup_reply.add(item_yes, item_no)
            time.sleep(1)
            message = bot.send_message(message.chat.id, "Хотите изменить эти данные?", reply_markup=markup_reply)
            bot.register_next_step_handler(message, register_again)

def register_again(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, "Введите данные Steam, логин и пароль, через пробел", reply_markup=hide_reply_keyboard)
        bot.register_next_step_handler(message, register_new_user)
    else:
        pass

@bot.message_handler(content_types=['text'])
def start_bot(message):
    if message.text.lower() == "начать":
        bot.send_message(message.chat.id, "Секунду...", reply_markup=hide_reply_keyboard)
        time.sleep(1)
        with open("table.csv", newline='') as table:
            reader = csv.DictReader(table, delimiter=';')
            i = 0
            for row in reader:
                if row['user_id'] == str(message.chat.id):
                    i = 1
            if i == 1:
                markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item_yes = types.KeyboardButton('Да')
                item_no = types.KeyboardButton('Нет')
                markup_reply.add(item_yes, item_no)
                message = bot.send_message(message.chat.id, f"{defolt}Хотите их изменить?", reply_markup=markup_reply)
                bot.register_next_step_handler(message, change_defolt)
            else:
                message = bot.send_message(message.chat.id, "Для начала работы необходимо ввести данные Steam.\n"
                                                            "Укажите логин и пароль от аккаунта через пробел")
                bot.register_next_step_handler(message, register_new_user)
    elif message.text.lower() == "стоп":
        try:
            users[message.chat.id].stop_prog()
        except StopProgramm:
            try:
                del users[message.chat.id]
                bot.send_message(message.chat.id, "Бот остановлен")
            except KeyError:
                pass
    else:
        pass

def register_new_user(message):
    str_1 = [x for x in message.text + ' ']
    i = 0
    global login
    global password
    login = ''
    password = ''
    for elem in str_1:
        if elem != ' ' and i == 0:
            login += elem
        elif elem == ' ':
            i +=1
        elif elem != ' ' and i == 1:
            password += elem
    keyboard = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(item_yes, item_no)
    bot.send_message(message.chat.id, f"Логин - {login}, пароль - {password}\nУверены, что хотите продолжить с этими данными?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def get_answer(call):
    if call.data == 'yes':
        with open("table.csv", newline='') as table:
            reader = csv.DictReader(table, delimiter=';')
            i = 0
            for row in reader:
                if row['user_id'] == str(call.message.chat.id):
                    i = 1
        if i == 0:
            with open("table.csv", 'a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([str(call.message.chat.id), login, password])
                time.sleep(1)
        elif i == 1:
            usr_id = []
            usr_login = []
            usr_password = []
            with open("table.csv", newline='') as table:
                reader = csv.DictReader(table, delimiter=';')
                for row in reader:
                    if row['user_id'] != str(call.message.chat.id):
                        usr_id.append(row['user_id'])
                        usr_login.append(row['steam_login'])
                        usr_password.append(row['steam_password'])
            with open("table.csv", 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['user_id', 'steam_login', 'steam_password'])
                for i in range(len(usr_id)):
                    writer.writerow([usr_id[i], usr_login[i], usr_password[i]])
                writer.writerow([call.message.chat.id, login, password])
            time.sleep(1)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_yes = types.KeyboardButton('Да')
        item_no = types.KeyboardButton('Нет')
        markup_reply.add(item_yes, item_no)
        message = bot.send_message(call.message.chat.id, f"{defolt}Хотите их изменить?", reply_markup=markup_reply)
        bot.register_next_step_handler(message, change_defolt)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "Попробуем еще раз)")
        time.sleep(0.5)
        bot.send_message(call.message.chat.id, "Укажите логин и пароль от аккаунта через пробел")
        bot.register_next_step_handler(call.message, register_new_user)

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

def code_add(message):
    try:
        users[message.chat.id].data['code'] = message.text
        users[message.chat.id].autorisation()
        users[message.chat.id].autorisation_check()
    except Exception:
        try:
            del users[message.chat.id]
            bot.send_message(message.chat.id, "Бот остановлен\nПерезапустите его командой /start")
        except KeyError:
            pass


bot.polling(none_stop=True, interval=0)
