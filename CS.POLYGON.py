import os
import time
from selenium import webdriver
from uuid import getnode as get_mac
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


print("Введите любой символ, если хотите настроить бота, в противном случае нажмите Enter:")
nastr=input()
if nastr=="":
    time.sleep(1)
    file=open("../textfiles/textpolygon.txt", 'r')
    st1=float(file.readline()); st2=float(file.readline()); st3=float(file.readline()); st4=float(file.readline()); st5=float(file.readline()); choise=int(file.readline())
    file.close()
else:
    print("Введите пять чисел от 0 до 100 через пробел:")
    stavki=input()
    st1=""; st2=""; st3=""; st4=""; st5=""; i=0
    while True:
        while stavki[i]!=' ':
            st1+=stavki[i]
            i+=1
        i+=1
        while stavki[i]!=' ':
            st2+=stavki[i]
            i+=1
        i+=1
        while stavki[i]!=' ':
            st3+=stavki[i]
            i+=1
        i+=1
        while stavki[i]!=' ':
            st4+=stavki[i]
            i+=1
        i+=1
        for i in range(i, len(stavki)):
            st5+=stavki[i]
            i+=1
        break
    st1=int(st1)/100; st2=int(st2)/100; st3=int(st3)/100; st4=int(st4)/100; st5=int(st5)/100

    print("Какой баланс?")
    print("1. Динамический")
    print("2. Статический")
    choise=int(input())

    file=open("../textfiles/textpolygon.txt", 'w')
    file.write(str(st1) + "\n"); file.write(str(st2) + "\n"); file.write(str(st3) + "\n"); file.write(str(st4) + "\n"); file.write(str(st5) + "\n"); file.write(str(choise) + "\n")
    file.close()

print("Итак, бот ставит по следующей стратегии:")
print(st1, st2, st3, st4, st5)
if choise == 1:
    print("Динамический баланс" + "\n")
if choise == 2:
    print("Статический баланс" + "\n")

print("Введите несгораемую сумму:")
podushka=float(input())

# авторизация
driver = webdriver.Chrome()
driver.get("https://csgopolygon.gg")

def autorisation():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.window.sign_in.style\=.opened > div.window_box.default_box > form > a"))).click()
    # ввод логина
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#steamAccountName"))).send_keys("#")
    # ввод пароля
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#steamPassword"))).send_keys("#")
    # войти
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#imageLogin"))).click()
    # crash
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.main.scrollable.clearing > div.leftSide > div.games > ul > li:nth-child(4)"))).click()
    # выключить звук
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > header > div.side > div.sound.on"))).click()
    # настройки
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > header > div.side > div.user > div.settings"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > header > div.side > div.user > div.settings > div > ul > li:nth-child(1) > a"))).click()
    # скрыть чат
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.window.change_your_settings.opened > div.window_box.default_box > form > div:nth-child(5)"))).click()
    # выключить снег
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.window.change_your_settings.opened > div.window_box.default_box > form > div:nth-child(6)"))).click()
    # сохранить
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.window.change_your_settings.opened > div.window_box.default_box > form > div.window_double_buttons > button.window_default_green_button_inline"))).click()
    # окей
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(34) > div > button.confirm"))).click()
    time.sleep(2)
    # ввод ставки
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#crash_auto_cashout"))).clear()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#crash_auto_cashout"))).send_keys("1.2")
autorisation()

def last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(1) > span")))
    savelast=driver.find_element(By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(1) > span")
    lastcrash=savelast.text
    lastcrash=float(lastcrash)
    return lastcrash

def pre_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(2) > span")))
    saveprelast=driver.find_element(By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(2) > span")
    prelastcrash=saveprelast.text
    prelastcrash=float(prelastcrash)
    return prelastcrash

def prex2_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(3) > span")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(3) > span")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash)
    return prelastcrash

def prex3_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(4) > span")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(4) > span")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash)
    return prelastcrash

def prex4_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(5) > span")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(5) > span")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash)
    return prelastcrash

def prex5_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(6) > span")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(6) > span")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash)
    return prelastcrash

def prex6_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(7) > span")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "#select_crash > div.crash_game_history > div.latest_games > div > ul > li:nth-child(7) > span")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash)
    return prelastcrash

def balance():
    savebalance = driver.find_element(By.CSS_SELECTOR, "#balance_p")
    balance = float(savebalance.text)
    return balance

def stavka(bal, perc):
    # ввод суммы
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#crash_amount"))).clear()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#crash_amount"))).send_keys(str(round((bal-podushka) * perc)))
    time.sleep(5)
    # поставить
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select_crash > div.crash_game_top > div.crash_bet > div > div:nth-child(5) > span"))).click()

if choise==1:
    last = last_crash()
    while last < 1.2:
        last = last_crash()
    while True:
        file=open("count.txt", 'a')
        last = last_crash()
        if last < 1.2:
            if st1 != 0:
                bal=balance()
                stavka(bal, st1)
            a = pre_last_crash()
            while a >= 1.2:
                a = pre_last_crash()
            lastcheck = last_crash()

            if lastcheck < 1.2:
                if st2 != 0:
                    bal = balance()
                    stavka(bal, st2)
                a = prex2_last_crash()
                while a >= 1.2:
                    a = prex2_last_crash()
                last1check = last_crash()

                if last1check < 1.2:
                    if st3 != 0:
                        bal = balance()
                        stavka(bal, st3)
                    a = prex3_last_crash()
                    while a >= 1.2:
                        a = prex3_last_crash()
                    last2check = last_crash()

                    if last2check < 1.2:
                        if st4 != 0:
                            bal = balance()
                            stavka(bal, st4)
                        a = prex4_last_crash()
                        while a >= 1.2:
                            a = prex4_last_crash()
                        last3check = last_crash()

                        if last3check < 1.2:
                            if st5 != 0:
                                bal = balance()
                                stavka(bal, st5)
                            a = prex5_last_crash()
                            while a >= 1.2:
                                a = prex5_last_crash()
                            last4check = last_crash()

                            if last4check < 1.2:
                                file.write(" 6")

                            else:
                                file.write(" 5")
                        else:
                            file.write(" 4")
                    else:
                        file.write(" 3")
                else:
                    file.write(" 2")
            else:
                file.write(" 1")
