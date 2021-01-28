import os
import time
from selenium import webdriver
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def wait_int(str=""):
    print(str)
    while True:
        a=input()
        if (a.isdigit()):
            break
        print("uncorrect syntax")
    return (int(a))
def wait_float(str=""):
    print(str)
    while True:
        a=input()
        try:
            float(a)
            return (float(a))
        except ValueError:
            print("uncorrect syntax")
def autorisation():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_size_2 btn_success2']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamAccountName']"))).send_keys(id['login'])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamPassword']"))).send_keys(id['password'])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='imageLogin']"))).click()
    print("Введите код Steam Guard:")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(input())
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] :nth-child(1)"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_icon xbutton_size_x34 xbutton_toggle']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon volume_icon']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon icon_settings']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='control__label']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xmodal__close']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).send_keys("1.2")
    print("Авторизация пройдена\nРезультаты работы:")

def click(n):
    for i in range(n):
        time.sleep(0.4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='inventory__toggle'] > label"))).click()

def crash_from_end(n):
    string = "[class='xhistory__content ng-star-inserted'] :nth-child(" + str(n) + ")"
    button = float(driver.find_element(By.CSS_SELECTOR, string).text[:-1])
    return button
def balance():
    save = driver.find_elements(By.CSS_SELECTOR, "[class='inventory__count symbol_usd']")
    vyb = float(save[0].text)
    bal = float(save[1].text)
    return round(bal + vyb,2)
def zakup(bal, bet, type):
    if type==1:
        if round((bal-podushka) * bet)<0.25:
            zakup(balance(),0.25,2)
            return 0
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_block btn_size_2 btn_default4']"))).click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).clear()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(str(round(((bal-podushka) * bet), 2)))
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='skins skins_for_window'] :nth-child(1)"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_block xbutton_buy']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='shop__close']"))).click()
        return 1
    if type == 2:
        if (bet>(bal-podushka)): return 0
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_block btn_size_2 btn_default4']"))).click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).clear()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(str(round((bet), 2)))
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='skins skins_for_window'] :nth-child(1)"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_block xbutton_buy']"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='shop__close']"))).click()
            return 1
def start():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_block btn_size_create btn_purple ng-star-inserted']"))).click()
def print_file():
    file=open("textfail.txt", 'r')
    podushka = float(file.readline())
    stairs=float(file.readline())
    stL = float(file.readline())
    print("Основные ставки после нескольких крашей подряд:")
    type_of_bet=float(file.readline())
    if type_of_bet == 1:
        print("Динамический баланс" )
        stav=float(file.readline()); rubish=1
        while 1:
            print(rubish,"- й краш - ", stav*100, "% текущего баланса")
            stav = float(file.readline())
            rubish+=1
            if stav==1:
                print(rubish,"- й краш - ", stav*100, "% текущего баланса")
                break
    if type_of_bet==2:
        print("Статический баланс")
        print("1-й краш - ",float(file.readline()),
              "$\n2-й краш - ",float(file.readline()),
              "$\n3-й краш - ",float(file.readline()),
              "$\n4-й краш - ",float(file.readline()),
              "$\n5-й краш - ",float(file.readline()), "$")
    if stairs == 1:
        print("А так же после ситуации К НК К производится ставка на сумму:", stL, "$."
                " Ставка делается, если в основных ставках после первого краша ставки нет.")
    if stairs == 2:
        print("А так же после ситуации К НК К НК К производится ставка на сумму:", stL, "$."
                " Ставка делается, если в основных ставках после первого краша ставки нет.")
    if stairs == 0:
        print("После лесенок ставки производиться не будут")
    print("Сумма из вашего баланса, недоступная для ставок - ", podushka, "$")
    file.close()
    print("")
def watch():
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, "[class='skins skins_for_inventory'] > div")
        return True
    except NoSuchElementException:
        return False
def change_file():
    type_of_bet = wait_int("Какой тип баланса будет использован?\n1. Динамический\n2. Статический\nВведите номер выбраного варианта ")
    number_of_crash = wait_int("Введите номер очередного краша, после которого хотите ставить")
    st = [0, 0, 0, 0, 0]
    if type_of_bet == 1:
        for i in range(number_of_crash, 6):
            st[i - 1] = wait_int(
                "Введите часть баланса в %, которую вы хотите ставить после " + str(i) + "-ого краша") / 100
            if (st[i - 1] == 1):
                for j in range(i + 1, 6):
                    st[j - 1] = 1
                break
    if type_of_bet == 2:
        for i in range(number_of_crash, 6):
            st[i - 1] = wait_float("Введите сумму в $, которую вы хотите ставить после " + str(i) + "-ого краша")
    st1 = st[0];st2 = st[1];st3 = st[2];st4 = st[3];st5 = st[4]
    stairs = wait_int("В какой ситуации вы хотите ставить"
                      "\n1.Краш Некраш Краш"
                      "\n2.Краш Некраш Краш Некраш Краш"
                      "\n3.Ни в одной из этих ситуаций"
                      "\nВведите номер выбраного варианта ")
    if (stairs==3):stairs=0
    if stairs != 0:
        stL = wait_float("Введите сумму ставки в данной ситуации ($) ")
    else:
        stL = 0.0
    podushka = wait_float("Введите несгораемую сумму:")
    file = open("textfail.txt", 'w')
    file.write(str(podushka)+"\n")
    file.write(str(stairs) + "\n")
    file.write(str(stL) + "\n")
    file.write(str(type_of_bet) + "\n")
    file.write(str(st1) + "\n");file.write(str(st2) + "\n");file.write(str(st3) + "\n");file.write(str(st4) + "\n");file.write(str(st5) + "\n")
    file.close()
def menu():
    while True:
        print("Список доступных команд:"
              "\n1.Просмотреть текущие настройки"
              "\n2.Изменить настройки"
              "\n3.Начать")
        punkt=wait_int("Введите номер выбраного вырианта ")
        if punkt==1:print_file()
        if punkt==2:change_file()
        if punkt ==3:break

try:
    menu()
    file=open("textfail.txt", 'r')
    podushka=float(file.readline())
    stairs=int(file.readline())
    stL=float(file.readline())
    type_of_bet = int(file.readline());st1=float(file.readline()); st2=float(file.readline()); st3=float(file.readline()); st4=float(file.readline()); st5=float(file.readline())
    file.close()
    print("Текущие настройки:")
    print_file()
    print("Если настройки верные, нажмите Enter. В ином случае введите любой символ")
    rubish=input()
    if rubish!="":
        menu()
    # авторизация
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options, executable_path='C:\webdrivers\chromedriver.exe')
    driver.get("https://cs.fail")
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")
    # options.add_argument("window-size=1920x1080")
    # driver = webdriver.Firefox(options=options, executable_path='C:\webdrivers\geckodriver')
    # driver.get("http://cs.fail")
    id={'login':"povarenok005", 'password':"Razryad777"}
    autorisation()

    while 1:
        time.sleep(0.5)
        a= crash_from_end(1)
        if a < 1.2:
            obmen=0
            if st1 != 0:
                click(1)
                zakup(balance(), st1, type_of_bet)
                click(2)
                start()
                obmen=1
            #Лесенка
            else:
                if(stairs==1 and crash_from_end(3)<1.2):
                    print("Лесенка К НК К")
                    click(1)
                    zakup(balance(), stL, 2)
                    click(2)
                    start()
                    zakup(balance(), 0.25, 2)
                    obmen = 1
                if(stairs==2 and crash_from_end(3)<1.2 and crash_from_end(5)<1.2):
                    print("Лесенка К НК К НК К")
                    click(1)
                    zakup(balance(), stL, 2)
                    click(2)
                    start()
                    zakup(balance(), 0.25, 2)
                    obmen = 1
            a2 = crash_from_end(2)
            while a2 >= 1.2:
                a2= crash_from_end(2)
            a = crash_from_end(1)
            if a < 1.2:
                if (st2 != 0):
                    print("Двойной", st2)
                    if (st1==0 or stairs==1 or stairs==2):
                        click(1)
                    zakup(balance(), st2, type_of_bet)
                    click(2)
                    start()
                    obmen = 1
                a3 = crash_from_end(3)
                while a3 >= 1.2:
                    a3 = crash_from_end(3)
                a = crash_from_end(1)
                if a < 1.2:
                    if st3 != 0:
                        if st2==1:
                            print("Закончились средства для ставок")
                            break
                        print("Тройной", st3)
                        if st2==0:
                            click(1)
                        zakup(balance(), st3, type_of_bet)
                        click(2)
                        start()
                        obmen = 1
                    a4 = crash_from_end(4)
                    while a4 >= 1.2:
                        a4 = crash_from_end(4)
                    a = crash_from_end(1)
                    if a < 1.2:
                        if st4 != 0:
                            if st3 == 1:
                                print("Закончились средства для ставок")
                                break
                            print("Четверной", st4)
                            if st3==0:
                                click(1)
                            zakup(balance(), st4, type_of_bet)
                            click(2)
                            start()
                            obmen = 1
                        a5 = crash_from_end(5)
                        while a5 >= 1.2:
                            a5 = crash_from_end(5)
                        a = crash_from_end(1)
                        if a < 1.2:
                            print("Пятерной краш")
                            if st5 != 0:
                                if st4 == 1:
                                    print("Закончились средства для ставок")
                                    break
                                if st4==0:
                                    click(1)
                                zakup(balance(), st5, type_of_bet)
                                click(2)
                                start()
                                obmen = 1
                            a5 = crash_from_end(6)
                            while a5 >= 1.2:
                                a5 = crash_from_end(6)
                            a = crash_from_end(1)
                            if a < 1.2:
                                print("Шестерной краш")
                                break
                            else:
                                if st5 == 1: break
                        else:
                            if st4 == 1: break
                    else:
                        if st3 == 1: break
                else:
                    if st2 == 1: break
            else:
                if st1 == 1: break
            if obmen==1:
                click(2)
                zakup(balance(),0.25,2)
                click(1)
finally:
    driver.quit()
