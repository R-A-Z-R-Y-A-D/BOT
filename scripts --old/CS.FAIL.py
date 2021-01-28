import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


print("Введите любой символ, если хотите настроить бота, в противном случае нажмите Enter:")
nastr=input()
if nastr=="":
    time.sleep(1)
    file=open("../textfiles/textfail.txt", 'r')
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

    file=open("../textfiles/textfail.txt", 'w')
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
driver.get("https://cs.fail")

def autorisation():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div > div.empty__login > a"))).click()
    # ввод логина
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#steamAccountName"))).send_keys("povarenok005")
    # ввод пароля
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#steamPassword"))).send_keys("Razryad777")
    # войти
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#imageLogin"))).click()
    # крестик
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.container.container_main.ng-tns-c79-0.ng-trigger.ng-trigger-containerAnimation > app-chat > div > div.aside__toggle > button"))).click()
    # ввод ставки
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.container.container_main.ng-tns-c79-0.ng-trigger.ng-trigger-containerAnimation > div > app-crash-home > div > div.crash__controller > div.crash__information > app-crash-editor > div.information__coeff.ng-star-inserted > div.information__input.form.form_theme_default > input"))).clear()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.container.container_main.ng-tns-c79-0.ng-trigger.ng-trigger-containerAnimation > div > app-crash-home > div > div.crash__controller > div.crash__information > app-crash-editor > div.information__coeff.ng-star-inserted > div.information__input.form.form_theme_default > input"))).send_keys("1.2")
    # выключить звук
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-sidebar > div > div.sidebar__content > div.sidebar__volume.volume.volume_header.volume_on"))).click()
    # убрать анимацию
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > app-sidebar > div > div.sidebar__content > app-settings > div"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > app-modals-container > app-modal > div > div > div > div > div:nth-child(3)"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > app-modals-container > app-modal > div > div > button"))).click()
    # нажать книпку в наличии

autorisation()

def last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(1)")))
    savelast=driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(1)")
    lastcrash=savelast.text
    lastcrash=float(lastcrash[:-1])
    return lastcrash

def pre_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(2)")))
    saveprelast=driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(2)")
    prelastcrash=saveprelast.text
    prelastcrash=float(prelastcrash[:-1])
    return prelastcrash

def prex2_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(3)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(3)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[:-1])
    return prelastcrash

def prex3_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(4)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(4)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[:-1])
    return prelastcrash

def prex4_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(5)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(5)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[:-1])
    return prelastcrash

def prex5_last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(6)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(6)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[:-1])
    return prelastcrash

def click(n):
    for i in range (n):
        # выбрать все
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__head > div.inventory__toggle > label > div"))).click()

def balance():
    savebalance = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__head > div.inventory__balance > div.inventory__count.symbol_usd")
    balance = float(savebalance.text)
    savevybrano = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__head > div.inventory__selected > div.inventory__count.symbol_usd")
    vybrano = float(savevybrano.text)
    vsego=round((balance+vybrano), 2)
    return vsego

def zakup(bal, perc):
    # магазин скинов
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__footer > button"))).click()
    # цена
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__filters.filters.filter_shop > div.filter.filter_price > input"))).clear()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__filters.filters.filter_shop > div.filter.filter_price > input"))).send_keys(str(round(((bal-podushka) * perc), 2)))
    # первый предмет
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.window__inventory.ng-star-inserted > div > div > div:nth-child(1)"))).click()
    # подтвердить
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__controllers > div.shop__buy > button"))).click()
    # крестик
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__head > div.shop__close"))).click()

def start():
    # начать
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.container.container_main.ng-tns-c79-0.ng-trigger.ng-trigger-containerAnimation > div > app-crash-home > div > div.crash__controller > div.crash__information > div > button"))).click()

if choise==1:
    last=last_crash()
    time.sleep(0.5)
    while last<1.2:
        last=last_crash()
    while 1:
        last = last_crash()
        if last < 1.2:
            if st1 != 0:
                click(1)
                bal = balance()
                zakup(bal, st1)
                click(2)
                start()
            a = pre_last_crash()
            while a >= 1.2:
                a = pre_last_crash()
            lastcheck = last_crash()

            if lastcheck < 1.2:
                if st2 != 0:
                    click(1)
                    bal = balance()
                    zakup(bal, st2)
                    click(2)
                    start()
                a = prex2_last_crash()
                while a >= 1.2:
                    a = prex2_last_crash()
                last1check = last_crash()

                if last1check < 1.2:
                    if st3 != 0:
                        click(1)
                        bal = balance()
                        zakup(bal, st3)
                        click(2)
                        start()
                    a = prex3_last_crash()
                    while a >= 1.2:
                        a = prex3_last_crash()
                    last2check = last_crash()

                    if last2check < 1.2:
                        if st4 != 0:
                            click(1)
                            bal = balance()
                            zakup(bal, st4)
                            click(2)
                            start()
                        a = prex4_last_crash()
                        while a >= 1.2:
                            a = prex4_last_crash()
                        last3check = last_crash()

                        if last3check < 1.2:
                            print("Пятерной краш")
                            if st5 != 0:
                                click(1)
                                bal = balance()
                                zakup(bal, st5)
                                click(2)
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
                                    click(1)

                        else:
                            if st4 != 0:
                                click(1)

                    else:
                        if st3 != 0:
                            click(1)

                else:
                    if st2 != 0:
                        click(1)

            else:
                if st1 != 0:
                    click(1)

elif choise==2:
    last = last_crash()
    time.sleep(0.5)
    while last < 1.2:
        last = last_crash()
    while 1:
        last = last_crash()
        if last < 1.2:
            bal = balance()
            if st1 != 0:
                click(1)
                zakup(bal, st1)
                click(2)
                start()
            a = pre_last_crash()
            while a >= 1.2:
                a = pre_last_crash()
            lastcheck = last_crash()

            if lastcheck < 1.2:
                if st2 != 0:
                    click(1)
                    zakup(bal, st2)
                    click(2)
                    start()
                a = prex2_last_crash()
                while a >= 1.2:
                    a = prex2_last_crash()
                last1check = last_crash()

                if last1check < 1.2:
                    if st3 != 0:
                        click(1)
                        zakup(bal, st3)
                        click(2)
                        start()
                    a = prex3_last_crash()
                    while a >= 1.2:
                        a = prex3_last_crash()
                    last2check = last_crash()

                    if last2check < 1.2:
                        if st4 != 0:
                            click(1)
                            zakup(bal, st4)
                            click(2)
                            start()
                        a = prex4_last_crash()
                        while a >= 1.2:
                            a = prex4_last_crash()
                        last3check = last_crash()

                        if last3check < 1.2:
                            print("Пятерной краш")
                            if st5 != 0:
                                click(1)
                                zakup(bal, st5)
                                click(2)
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
                                    click(1)
                        else:
                            if st4 != 0:
                                click(1)
                    else:
                        if st3 != 0:
                            click(1)
                else:
                    if st2 != 0:
                        click(1)
            else:
                if st1 != 0:
                    click(1)