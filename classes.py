import time
import telebot
import openpyxl
from telebot import types
from config import tokens, admins
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


users = {}
token = tokens['bub']
book = openpyxl.open("base.xlsx")
base = book.active
bot = telebot.TeleBot(token, parse_mode="HTML")
hide_reply_keyboard = types.ReplyKeyboardRemove()

class StopProgramm(Exception):
    pass

class Crashes:

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--mute-audio")
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument("window-size=1920x1080")

    data = {
        'login': 0,
        'password': 0,
        'bets': [0],
        'part': 0,
        'podushka': 0,
        'type': 0,
        'id': 0,
        'code': 0
    }

    def __init__(self, array):
        self.data['login'] = array[0]
        self.data['password'] = array[1]
        self.data['bets'] = array[2]
        self.data['part'] = array[3]
        self.data['podushka'] = array[4]
        self.data['type'] = array[5]
        self.data['id'] = array[6]
        self.driver = webdriver.Chrome(options=Crashes.chrome_options)

    def __call__(self):
        self.autorisation()
        if str(self.data['id']) in users: self.autorisation_check()
        if str(self.data['id']) in users: self.main()

    def send_any_message(self, text):
        bot.send_message(self.data['id'], text)

    def stop_prog(self):
        try:
            self.driver.quit()
            raise StopProgramm
        except StopProgramm:
            try:
                del users[str(self.data['id'])]
                self.send_any_message('Бот остановлен\nПерезапустите его командой /start')
            except Exception:
                pass

    def wait_crash(self, n):
        crash_n = self.get_crash(n)
        while crash_n >= 1.2:
            crash_n = self.get_crash(n)
        return self.get_crash(1)

    def autorisation_check(self):
        try:
            save = 0
            for i in self.data['bets']:
                if i > 0:
                    save=i
                    break
            self.click(1)
            bal = self.get_balance()
            self.click(1)
            if save*bal < 0.25:
                self.send_any_message("На вашем балансе недостаточно средств")
                self.stop_prog()
            else:
                self.send_any_message("Отлично, на вашем балансе достаточно средств, бот начал работу")
        except Exception:
            self.stop_prog()

    def get_code(self):
        while self.data['code'] == 0:
            time.sleep(0.5)
        code = self.data['code']
        self.data['code'] = 0
        return code

class CsgoBand(Crashes):

    def autorisation(self):
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
                self.send_any_message("Вы указали неверные данные Steam, либо при попытке входа появляется CAPTCHA\nПроверьте правильность логина и пароля командой /steam_data")
                raise Exception
            except TimeoutException:
                pass
            self.send_any_message("Введите код Steam Guard")
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(self.get_code())
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] > div"))).click()

            def enter(self):
                self.send_any_message("Код неверный, попробуйте снова")
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(self.get_code())
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode'] > div"))).click()

            while True:
                try:
                    WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode']")))
                    enter(self)
                except TimeoutException:
                    break
            # изменение настроек
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn-toggler chat-trigger active']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-sound"))).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".field-input"))).send_keys(Keys.BACK_SPACE)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".field-input"))).send_keys(self.data['part'])
        except Exception:
            self.stop_prog()

    def get_crash(self, n):
        try:
            time.sleep(0.5)
            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"[class='graph-labels'] :nth-child({n}) > span")))
            return float(button.text[:-1])
        except Exception:
            self.stop_prog()

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

    def do_afull_process_dynamic(self, num_of_bets):
        self.click(1)
        self.change(self.data['bets'][num_of_bets], self.get_balance())
        self.click(1)
        time.sleep(3)
        self.make_bet()

    def do_afull_process_static(self, num_of_bets, bal):
        self.click(1)
        self.change(self.data['bets'][num_of_bets], bal)
        self.click(1)
        time.sleep(3)
        self.make_bet()

    def main(self):
        try:

            if self.data['type'] == 1:
                crash_1 = self.get_crash(1)
                while crash_1 < 1.2:
                    crash_1 = self.get_crash(1)
                while True:
                    crash_1 = self.get_crash(1)
                    if crash_1 < 1.2:
                        if self.data['bets'][0] != 0: self.do_afull_process_dynamic(0)
                        crash_1 = self.wait_crash(2)

                        if crash_1 < 1.2:
                            if self.data['bets'][1] != 0: self.do_afull_process_dynamic(1)
                            crash_1 = self.wait_crash(3)

                            if crash_1 < 1.2:
                                if self.data['bets'][2] != 0: self.do_afull_process_dynamic(2)
                                crash_1 = self.wait_crash(4)

                                if crash_1 < 1.2:
                                    if self.data['bets'][3] != 0: self.do_afull_process_dynamic(3)
                                    crash_1 = self.wait_crash(5)

                                    if crash_1 < 1.2:
                                        if self.data['bets'][4] != 0: self.do_afull_process_dynamic(4)
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
                        if self.data['bets'][0] != 0: self.do_afull_process_static(0, bal)
                        crash_1 = self.wait_crash(2)

                        if crash_1 < 1.2:
                            if self.data['bets'][1] != 0: self.do_afull_process_static(1, bal)
                            crash_1 = self.wait_crash(3)

                            if crash_1 < 1.2:
                                if self.data['bets'][2] != 0: self.do_afull_process_static(2, bal)
                                crash_1 = self.wait_crash(4)

                                if crash_1 < 1.2:
                                    if self.data['bets'][3] != 0: self.do_afull_process_static(3, bal)
                                    crash_1 = self.wait_crash(5)

                                    if crash_1 < 1.2:
                                        if self.data['bets'][4] != 0: self.do_afull_process_static(4, bal)
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
                    while crash_1 == self.get_crash(1) or crash_2 == self.get_crash(2) or crash_3 == self.get_crash(
                            3) or crash_4 == self.get_crash(4):
                        time.sleep(0.1)
                    self.do_afull_process_dynamic(0)

        except Exception:
            pass

class CsFail(Crashes):

    def autorisation(self):
        try:
            self.driver.get("https://cs.fail/")
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
                self.send_any_message("Вы указали неверные данные Steam, либо при попытке входа появляется CAPTCHA\nПроверьте правильность логина и пароля командой /steam_data")
                raise Exception
            except TimeoutException:
                pass
            self.send_any_message("Введите код Steam Guard")
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(self.get_code())
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] > div"))).click()

            def enter(self):
                self.send_any_message("Код неверный, попробуйте снова")
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(self.get_code())
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode'] > div"))).click()

            while True:
                try:
                    WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode']")))
                    enter(self)
                except TimeoutException:
                    break
            # изменение настроек
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_icon xbutton_size_x34 xbutton_toggle']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon volume_icon']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).clear()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).send_keys(self.data['part'])
        except Exception:
            self.stop_prog()

    def get_crash(self, n):
        try:
            time.sleep(0.5)
            button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[class='xhistory__content ng-star-inserted'] :nth-child({n})")))
            return float(button.text[:-1])
        except Exception:
            self.stop_prog()

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

    def do_afull_process_dynamic(self, num_of_bets):
        self.click(1)
        self.change(self.data['bets'][num_of_bets], self.get_balance())
        self.click(1)
        time.sleep(0.5)
        self.make_bet()

    def do_afull_process_static(self, num_of_bets, bal):
        self.click(1)
        self.change(self.data['bets'][num_of_bets], bal)
        self.click(1)
        time.sleep(1)
        self.make_bet()

    def main(self):
        try:

            if self.data['type'] == 1:
                crash_1 = self.get_crash(1)
                while crash_1 < 1.2:
                    crash_1 = self.get_crash(1)
                while True:
                    crash_1 = self.get_crash(1)
                    if crash_1 < 1.2:
                        if self.data['bets'][0] != 0: self.do_afull_process_dynamic(0)
                        crash_1 = self.wait_crash(2)

                        if crash_1 < 1.2:
                            if self.data['bets'][1] != 0: self.do_afull_process_dynamic(1)
                            crash_1 = self.wait_crash(3)

                            if crash_1 < 1.2:
                                if self.data['bets'][2] != 0: self.do_afull_process_dynamic(2)
                                crash_1 = self.wait_crash(4)

                                if crash_1 < 1.2:
                                    if self.data['bets'][3] != 0: self.do_afull_process_dynamic(3)
                                    crash_1 = self.wait_crash(5)

                                    if crash_1 < 1.2:
                                        if self.data['bets'][4] != 0: self.do_afull_process_dynamic(4)
                                        crash_1 = self.wait_crash(6)

                                        if crash_1 < 1.2:
                                            print("Шестерной краш")
                                            break

                                        elif self.data['bets'][4] != 0: self.click(1)
                                    elif self.data['bets'][3] != 0: self.click(1)
                                elif self.data['bets'][2] != 0: self.click(1)
                            elif self.data['bets'][1] != 0: self.click(1)
                        elif self.data['bets'][0] != 0: self.click(1)

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
                        if self.data['bets'][0] != 0: self.do_afull_process_static(0, bal)
                        crash_1 = self.wait_crash(2)

                        if crash_1 < 1.2:
                            if self.data['bets'][1] != 0: self.do_afull_process_static(1, bal)
                            crash_1 = self.wait_crash(3)

                            if crash_1 < 1.2:
                                if self.data['bets'][2] != 0: self.do_afull_process_static(2, bal)
                                crash_1 = self.wait_crash(4)

                                if crash_1 < 1.2:
                                    if self.data['bets'][3] != 0: self.do_afull_process_static(3, bal)
                                    crash_1 = self.wait_crash(5)

                                    if crash_1 < 1.2:
                                        if self.data['bets'][4] != 0: self.do_afull_process_static(4, bal)
                                        crash_1 = self.wait_crash(6)

                                        if crash_1 < 1.2:
                                            print("Шестерной краш")
                                            break

                                        elif self.data['bets'][4] != 0: self.click(1)
                                    elif self.data['bets'][3] != 0: self.click(1)
                                elif self.data['bets'][2] != 0: self.click(1)
                            elif self.data['bets'][1] != 0: self.click(1)
                        elif self.data['bets'][0] != 0: self.click(1)

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

        except Exception:
            pass