import os
import time
from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

try:

    class CSGO_BAND:

        options = Options()
        options.add_argument("window-size=1920x1080")
        driver = webdriver.Firefox(options=options)
        driver.get("https://csgo.band/")

        data = {
            'login': '',
            'password': '',
            'perc': [0, 0.05, 0.28, 0.95, 1],
            'podushka': 0
        }

        def __init__(self, login='', password='', perc=[0.1, 0.05, 0.28, 0.95, 1], podushka=0):
            self.data['login'] = login
            self.data['password'] = password
            self.data['perc'] = perc
            self.data['podushka'] = podushka

        def get_crash(self, n):
            time.sleep(0.5)
            button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"[class='graph-labels'] :nth-child({n}) > span")))
            return float(button.text[:-1])

        def autorization(self):
            try:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn--green steam-login']"))).click()
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamAccountName']"))).send_keys(self.data['login'])
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamPassword']"))).send_keys(self.data['password'])
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='imageLogin']"))).click()
                try:
                    WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='error_display']"))).click()
                except TimeoutException:
                    pass
                print("введи код")
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(input())
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] > div"))).click()
                def enter(self):
                    print("введи код")
                    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(input())
                    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode'] > div"))).click()
                while True:
                    try:
                        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_incorrectcode']")))
                        enter(self)
                    except TimeoutException:
                        break
                # изменение настроек
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn-toggler chat-trigger active']"))).click()
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-sound"))).click()
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".field-input"))).send_keys(Keys.BACK_SPACE)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".field-input"))).send_keys('1.2')
            except Exception:
                self.autorization()

        def click(self, n):
            for i in range(n):
                time.sleep(0.4)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='checkbox-control__content']"))).click()

        def get_balance(self):
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='cur-u-drops-selected']")))
            sel = self.driver.find_element(By.CSS_SELECTOR, "[class='cur-u-drops-selected__selected']").text[2:]
            total = self.driver.find_element(By.CSS_SELECTOR, "[class='cur-u-drops-selected__total']").text[2:]
            return float(sel)+float(total)

        def make_bet(self):
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn-base btn btn--blue make-bet']"))).click()

        def change(self, part, bal):
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn--blue']"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='exchange-filter-maxPrice-field']"))).send_keys(Keys.BACK_SPACE*10)
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='exchange-filter-maxPrice-field']"))).send_keys(str(round(part*bal, 2)))
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='withdraw-list__inner'] > button"))).click()
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='withdraw-footer'] :nth-child(2)"))).click()

        def do_afull_process(self, num_of_perc):
            self.click(1)
            self.change(self.data['perc'][num_of_perc], self.get_balance())
            self.click(1)
            time.sleep(4)
            self.make_bet()

        def main(self):
            crash_1 = self.get_crash(1)
            while crash_1 < 1.2:
                crash_1 = self.get_crash(1)
            while True:
                crash_1 = self.get_crash(1)
                if crash_1 < 1.2 and self.data['perc'][0] != 0:
                    self.do_afull_process(0)
                    crash_2 = self.get_crash(2)
                    while crash_2 >= 1.2:
                        crash_2 = self.get_crash(2)
                    crash_1 = self.get_crash(1)

                    if crash_1 < 1.2 and self.data['perc'][1] != 0:
                        self.do_afull_process(1)
                        crash_3 = self.get_crash(3)
                        while crash_3 >= 1.2:
                            crash_3 = self.get_crash(3)
                        crash_1 = self.get_crash(1)

                        if crash_1 < 1.2 and self.data['perc'][2] != 0:
                            self.do_afull_process(2)
                            crash_4 = self.get_crash(4)
                            while crash_4 >= 1.2:
                                crash_4 = self.get_crash(4)
                            crash_1 = self.get_crash(1)

                            if crash_1 < 1.2 and self.data['perc'][3] != 0:
                                self.do_afull_process(3)
                                crash_5 = self.get_crash(5)
                                while crash_5 >= 1.2:
                                    crash_5 = self.get_crash(5)
                                crash_1 = self.get_crash(1)

                                if crash_1 < 1.2 and self.data['perc'][4] != 0:
                                    self.do_afull_process(4)
                                    crash_6 = self.get_crash(6)
                                    while crash_6 >= 1.2:
                                        crash_6 = self.get_crash(6)
                                    crash_1 = self.get_crash(1)

                                    if crash_1 < 1.2:
                                        print("Шестерной краш")
                                        break


    band = CSGO_BAND('#', '#')
    band.autorization()
    band.main()
finally:
    time.sleep(5)
    print("Бот завершил работу")