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
    file=open("../textfiles/textwin.txt", 'r')
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

    file=open("../textfiles/textwin.txt", 'w')
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
driver.get("https://csgowin.ru")

def autorisation():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-inventory > div > div > a"))).click()
    # ввод логина
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#steamAccountName"))).send_keys("#")
    # ввод пароля
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#steamPassword"))).send_keys("#")
    # войти
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#imageLogin"))).click()
    # крестик
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-chat > div > div > div > button"))).click()
    # ввод ставки
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > div.aside__controls.controls.controls_default > app-crash-editor > div > div.controls__coeff > input"))).clear()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > div.aside__controls.controls.controls_default > app-crash-editor > div > div.controls__coeff > input"))).send_keys("1.2")
    # выключить звук
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-header > header > div > div.header__left > div.header__volume.volume.volume_header.volume_on"))).click()
    # убрать анимацию
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-header > header > div > div.header__left > app-settings > div > button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-modals-container > app-modal > div > div > div > div > div:nth-child(3)"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-modals-container > app-modal > div > div > button"))).click()
autorisation()

def last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(1)")))
    savelast=driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(1)")
    lastcrash=savelast.text
    lastcrash=float(lastcrash[1:])
    return lastcrash

def pre_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(2)")))
    saveprelast=driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(2)")
    prelastcrash=saveprelast.text
    prelastcrash=float(prelastcrash[1:])
    return prelastcrash

def prex2_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(3)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(3)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[1:])
    return prelastcrash

def prex3_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(4)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(4)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[1:])
    return prelastcrash

def prex4_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(5)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(5)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[1:])
    return prelastcrash

def prex5_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(6)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.crash.crash_home > div.crash__information > div.crash__history.history.history_home > div > div > a:nth-child(6)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[1:])
    return prelastcrash

def balance():
    time.sleep(0.5)
    savebalance = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-header > header > div > div.header__right > div > div > div.profile__balance > div.coins.coins_default.profile__coins.symbol_usd")
    balance = savebalance.text
    balance = float(balance)
    return balance

def sell():
    # первый в инвенте
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-inventory > div > div > div.inventory__main.ng-star-inserted > div > div"))).click()
    # продать
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-inventory > div > div > div.inventory__head.ng-star-inserted > div.inventory__sell > button"))).click()

def start():
    # первый в инвенте
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-inventory > div > div > div.inventory__main.ng-star-inserted > div > div"))).click()
    # начать
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > div.aside__controls.controls.controls_default > div.controls__create.ng-star-inserted > button"))).click()

def zakup(bal, perc):
    # магазин скинов
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-inventory > div > div > div.inventory__footer > div > button"))).click()
    # цена
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-shop > div > div > div.shop__filters.filters.filters_shop > div.filter.filter_price > input"))).clear()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-shop > div > div > div.shop__filters.filters.filters_shop > div.filter.filter_price > input"))).send_keys(str(round(((bal-podushka) * perc), 2)))
    # первый предмет
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-shop > div > div > div.shop__main.ng-star-inserted > div > div:nth-child(1)"))).click()
    # подтвердить
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-shop > div > div > div.shop__button > button.button.button_primary.button_confirm"))).click()
    # крестик
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div > app-crash-home > div.aside.aside_default > app-shop > div > div > div.shop__close"))).click()

if choise==1:
    last = last_crash()
    while last < 1.2:
        last = last_crash()
    while 1:
        last = last_crash()
        time.sleep(0.5)
        if last < 1.2:
            if st1 != 0:
                bal = balance()
                zakup(bal, st1)
                start()
            a = pre_last_crash()
            while a >= 1.2:
                a = pre_last_crash()
            lastcheck = last_crash()

            if lastcheck < 1.2:
                if st2 != 0:
                    bal = balance()
                    zakup(bal, st2)
                    start()
                a = prex2_last_crash()
                while a >= 1.2:
                    a = prex2_last_crash()
                last1check = last_crash()

                if last1check < 1.2:
                    if st3 != 0:
                        bal = balance()
                        zakup(bal, st3)
                        start()
                    a = prex3_last_crash()
                    while a >= 1.2:
                        a = prex3_last_crash()
                    last2check = last_crash()

                    if last2check < 1.2:
                        if st4 != 0:
                            bal = balance()
                            zakup(bal, st4)
                            start()
                        a = prex4_last_crash()
                        while a >= 1.2:
                            a = prex4_last_crash()
                        last3check = last_crash()

                        if last3check < 1.2:
                            print("Пятерной краш")
                            if st5 != 0:
                                bal = balance()
                                zakup(bal, st5)
                                start()
                            a = prex5_last_crash()
                            while a >= 1.2:
                                a = prex5_last_crash()
                            last4check = last_crash()

                            if last4check < 1.2:
                                print("Шестерной краш")
                                break

                            else:
                                if st5 != 0:
                                    sell()

                        else:
                            if st4 != 0:
                                sell()

                    else:
                        if st3 != 0:
                            sell()

                else:
                    if st2 != 0:
                        sell()

            else:
                if st1 != 0:
                    sell()

elif choise==2:
    last = last_crash()
    while last < 1.2:
        last = last_crash()
    while 1:
        last = last_crash()
        time.sleep(0.5)
        if last < 1.2:
            bal=balance()
            if st1 != 0:
                zakup(bal, st1)
                start()
            a = pre_last_crash()
            while a >= 1.2:
                a = pre_last_crash()
            lastcheck = last_crash()

            if lastcheck < 1.2:
                if st2 != 0:
                    zakup(bal, st2)
                    start()
                a = prex2_last_crash()
                while a >= 1.2:
                    a = prex2_last_crash()
                last1check = last_crash()

                if last1check < 1.2:
                    if st3 != 0:
                        zakup(bal, st3)
                        start()
                    a = prex3_last_crash()
                    while a >= 1.2:
                        a = prex3_last_crash()
                    last2check = last_crash()

                    if last2check < 1.2:
                        if st4 != 0:
                            zakup(bal, st4)
                            start()
                        a = prex4_last_crash()
                        while a >= 1.2:
                            a = prex4_last_crash()
                        last3check = last_crash()

                        if last3check < 1.2:
                            print("Пятерной краш")
                            if st5 != 0:
                                zakup(bal, st5)
                                start()
                            a = prex5_last_crash()
                            while a >= 1.2:
                                a = prex5_last_crash()
                            last4check = last_crash()

                            if last4check < 1.2:
                                print("Шестерной краш")
                                break

                            else:
                                if st5 != 0:
                                    sell()

                        else:
                            if st4 != 0:
                                sell()

                    else:
                        if st3 != 0:
                            sell()

                else:
                    if st2 != 0:
                        sell()

            else:
                if st1 != 0:
                    sell()