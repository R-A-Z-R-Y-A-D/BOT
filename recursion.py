import telebot
import requests
import config
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from telebot import types

def wait_int(str=""):
    print(str)
    while True:
        a = input()
        if (a.isdigit()):
            break
        print("uncorrect syntax")
    return (int(a))
def wait_float(str=""):
    print(str)
    while True:
        a = input()
        try:
            float(a)
            return (float(a))
        except ValueError:
            print("uncorrect syntax")

def download_logs():
    file = open("textfiles/logins.txt", 'r')
    login = file.readline()
    password = file.readline()
    file.close()
    return {'login': login, 'password': password}
def set_logs(login=str(), password=str()):
    file=open("textfiles/logins.txt",'w')
    file.write(login+'\n')
    file.write(password + '\n')
    file.close()
# def change_logs():
#     file = open("textfiles/logins.txt", 'w')
#     file.write(input("Введите логин: "))
#     file.write(input("Введите пароль: "))
#     file.close()
# def change_file():
#     type_of_bet = wait_int(
#         "Какой тип баланса будет использован?\n1. Динамический\n2. Статический\nВведите номер выбраного варианта ")
#     number_of_crash = wait_int("Введите номер очередного краша, после которого хотите ставить")
#     st = [0, 0, 0, 0, 0]
#     if type_of_bet == 1:
#         for i in range(number_of_crash, 6):
#             st[i - 1] = wait_int(
#                 "Введите часть баланса в %, которую вы хотите ставить после " + str(i) + "-ого краша") / 100
#             if (st[i - 1] == 1):
#                 for j in range(i + 1, 6):
#                     st[j - 1] = 1
#                 break
#     if type_of_bet == 2:
#         for i in range(number_of_crash, 6):
#             st[i - 1] = wait_float("Введите сумму в $, которую вы хотите ставить после " + str(i) + "-ого краша")
#     st1 = st[0]
#     st2 = st[1]
#     st3 = st[2]
#     st4 = st[3]
#     st5 = st[4]
#     stairs = wait_int("В какой ситуации вы хотите ставить"
#                       "\n1.Краш Некраш Краш"
#                       "\n2.Краш Некраш Краш Некраш Краш"
#                       "\n3.Ни в одной из этих ситуаций"
#                       "\nВведите номер выбраного варианта ")
#     if (stairs == 3): stairs = 0
#     if stairs != 0:
#         stL = wait_float("Введите сумму ставки в данной ситуации ($) ")
#     else:
#         stL = 0.0
#     podushka = wait_float("Введите несгораемую сумму:")
#     file = open("textfiles/textfail.txt", 'w')
#     file.write(str(podushka) + "\n")
#     file.write(str(stairs) + "\n")
#     file.write(str(stL) + "\n")
#     file.write(str(type_of_bet) + "\n")
#     file.write(str(st1) + "\n")
#     file.write(str(st2) + "\n")
#     file.write(str(st3) + "\n")
#     file.write(str(st4) + "\n")
#     file.write(str(st5) + "\n")
#     file.close()
def programm ():
    def autorisation():
        print("Начало авторизации")
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='btn btn_size_2 btn_success2']"))).click()
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamAccountName']"))).send_keys(id['login'])
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='steamPassword']"))).send_keys(id['password'])
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='imageLogin']"))).click()
        @bot.message_handler(content_types=['text'])
        def count_guard(message):
            code = message.text
            WebDriverWait(driver, 120).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='twofactorcode_entry']"))).send_keys(code)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[id='login_twofactorauth_buttonset_entercode'] :nth-child(1)"))).click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[class='xbutton xbutton_icon xbutton_size_x34 xbutton_toggle']"))).click()
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon volume_icon']"))).click()
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='icon icon_settings']"))).click()
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='control__label']"))).click()
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xmodal__close']"))).click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).clear()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='ratio']"))).send_keys(
            "1.2")
        print("Авторизация пройдена")
    def click(n):
        for i in range(n):
            time.sleep(0.4)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='inventory__toggle'] > label"))).click()
    def crash_from_end(n):
        string = "[class='xhistory__content ng-star-inserted'] :nth-child(" + str(n) + ")"
        button = float(driver.find_element(By.CSS_SELECTOR, string).text[:-1])
        return button
    def balance():
        save = driver.find_elements(By.CSS_SELECTOR, "[class='inventory__count symbol_usd']")
        vyb = float(save[0].text)
        bal = float(save[1].text)
        return round(bal + vyb, 2)
    def zakup(bal, bet, type):
        if type == 1:
            if round((bal - podushka) * bet) < 0.25:
                zakup(balance(), 0.25, 2)
                return 0
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[class='btn btn_block btn_size_2 btn_default4']"))).click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).clear()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(
                str(round(((bal - podushka) * bet), 2)))
            time.sleep(1)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='skins skins_for_window'] :nth-child(1)"))).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='xbutton xbutton_block xbutton_buy']"))).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='shop__close']"))).click()
            return 1
        if type == 2:
            if (bet > (bal - podushka)):
                return 0
            else:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[class='btn btn_block btn_size_2 btn_default4']"))).click()
                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).clear()
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='number']"))).send_keys(str(round((bet), 2)))
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[class='skins skins_for_window'] :nth-child(1)"))).click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[class='xbutton xbutton_block xbutton_buy']"))).click()
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='shop__close']"))).click()
                return 1
    def start():
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[class='btn btn_block btn_size_create btn_purple ng-star-inserted']"))).click()

    # def watch():
    #     time.sleep(1)
    #     try:
    #         driver.find_element(By.CSS_SELECTOR, "[class='skins skins_for_inventory'] > div")
    #         return True
    #     except NoSuchElementException:
    #         return False
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options, executable_path='C:\webdrivers\chromedriver.exe')
    driver.get("https://cs.fail")
    try:
        # menu()
        # print("Текущие настройки:")
        # print_file()
        # print("Если настройки верные, нажмите Enter. В ином случае введите любой символ\n"
        #       "ВНИМАНИЕ, ЕСЛИ ВЫ ЗАПУСКАЕТЕ ПРОГРАММУ ВПЕРВЫЕ, ТРЕБУЕТСЯ УКАЗАТЬ ДАННЫЕ АККАУНТА")
        # rubish=input()
        # if rubish!="":
        #     menu()
        # авторизация
        # options = Options()
        # options.add_argument("--headless")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--no-sandbox")
        # options.add_argument("window-size=1920x1080")
        # driver = webdriver.Firefox(options=options, executable_path='C:\webdrivers\geckodriver')
        # driver.get("http://cs.fail")
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
        print("Окно закрыто")
        driver.quit()
id=download_logs()
file=open("textfiles/textfail.txt", 'r')
podushka=float(file.readline())
stairs=int(file.readline())
stL=float(file.readline())
type_of_bet = int(file.readline());st1=float(file.readline()); st2=float(file.readline()); st3=float(file.readline()); st4=float(file.readline()); st5=float(file.readline())
file.close()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, ""
             "Привет 🥰." 
             "С этим ботом ты сможешь автоматизировать свои ставки на csgo-крашах.\n"
             )
    change_user(message)
@bot.message_handler(commands=['list'])
def send_list(message):
    file_in_messege()
    list_text=''
    for_send=open("textfiles/messege.txt","r")
    for i in for_send:
        list_text+=i
    bot.send_message(message.chat.id, list_text)
    for_send.close()
    send_comamnds(message)
@bot.message_handler(commands=['begin'])
def begin(message):
    bot.send_message(message.chat.id, "Бот запущен\nВведите код Steam Guard:")
    programm()
    send_comamnds(message)
@bot.message_handler(commands=['set_user'])
def send_id(message):
    bot.send_message(message.chat.id, "Сейчас вы авторизованы как:"
                                      f"{id.get('login')}\n"
                                      "Хотите изменить данные аккаунта?(Y или N)\n"
                                      "*Y-да; N-нет")
    bot.register_next_step_handler(message,change_user)
def change_user(unswer):
    rubish=unswer.text
    if rubish=='Y' or rubish=='/start':
        bot.send_message(unswer.chat.id, "Введите ваш логин")
        bot.register_next_step_handler(unswer,change_pass)
    elif unswer.text=='N':
        pass
    else:
        bot.send_message(unswer.chat.id, "Введите только Y (для корректировки данных) или N (для выхода)")
        change_user(bot.message_handler(content_types=['text']))
def change_pass(log):
        id['login']=log.text
        bot.send_message(log.chat.id, "Введите ваш пароль")
        bot.register_next_step_handler(log, smsg_logs)
def smsg_logs(passw):
    id['password'] = passw.text
    set_logs(id.get('login'), id.get('password'))
    bot.send_message(passw.chat.id, "Настройки успешно сохранены!")
    send_comamnds(passw)
bot.polling(none_stop=True, interval=0)