import os
import time
from selenium import webdriver
from time import strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

try:
    perc = [0, 0, 0, 0, 0]
    podushka = [0]
    type = [0]

    def settings():
        file = open("heroku/test.txt", 'r')
        print("Текущие настройки бота:\n")
        for i in range(5):
            perc[i] = float(file.readline())
        print("Одинарный: " + str(round(perc[0] * 100)) + " %", end="\n")
        print("Двойной: " + str(round(perc[1] * 100)) + " %", end="\n")
        print("Тройной: " + str(round(perc[2] * 100)) + " %", end="\n")
        print("Четверной: " + str(round(perc[3] * 100)) + " %", end="\n")
        print("Пятерной: " + str(round(perc[4] * 100)) + " %", end="\n")
        type[0] = float(file.readline())
        print("Тип баланса:", "Статический" if type == 2 else "Динамический", "\n")
        print("Нажмите q, если хотите изменить их или нажмите Enter, чтобы запустить бота:")
        choise = input()
        if choise == "q":
            file.close()
            print("Введите 5 чисел от 0 до 100 через пробел:")
            stavki = input()
            j = 0
            new = ["", "", "", "", ""]
            for i in range(4):
                while stavki[j] != " ":
                    new[i] += stavki[j]
                    j += 1
                j += 1
            for i in range(j, len(stavki)):
                new[4] += stavki[i]
            print("Введите тип ставки:")
            print("1. Динамический")
            print("2. Статический")
            type[0] = int(input())
            file = open("heroku/test.txt", 'w')
            for i in range(5):
                new[i] = round(float(new[i]) / 100, 2)
                file.write(str(new[i]) + "\n")
            file.write(str(type[0]))
            file.close()
            for i in range(5):
                perc[i] = new[i]
        print("Введите несгораемую сумму:")
        podushka[0] = float(input())

    settings()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://cs.fail")

    id = {'login': "spiviksj", 'password': "FghJJhgF16052659"}

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
        print("Введите код Steam Guard:")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(input())
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
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_block btn_size_2 btn_default4']"))).click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).clear()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(
            str(round((bal - podushka[0]) * pc, 2)))
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='skins skins_for_window'] :nth-child(1)"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_block xbutton_buy']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='shop__close']"))).click()


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
            save = watch()
            if save == True:
                print("Бот не сделал ставку" + "\n")
            else:
                print(strftime("%Y-%m-%d %H:%M:%S") + "\n")

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
                                print("Пятерной краш")
                                check(4, 0)
                                a = crash(6)
                                while a >= 1.2:
                                    a = crash(6)
                                last4check = crash(1)

                                if last4check < 1.2:
                                    print("Шестерной краш")
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
                                print("Пятерной краш")
                                check(4, bal)
                                a = crash(6)
                                while a >= 1.2:
                                    a = crash(6)
                                last4check = crash(1)

                                if last4check < 1.2:
                                    print("Шестерной краш")
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
    driver.quit()