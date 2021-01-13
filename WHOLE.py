import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
def last_crash():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(1)")))
    savelast=driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(1)")
    lastcrash=savelast.text
    lastcrash=float(lastcrash[:-1])
    return lastcrash
def last_crash_2():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(2)")))
    saveprelast=driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(2)")
    prelastcrash=saveprelast.text
    prelastcrash=float(prelastcrash[:-1])
    return prelastcrash
def last_crash_3():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(3)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(3)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[:-1])
    return prelastcrash
def last_crash_4():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(4)")))
    saveprelast = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > app-crash-sidebar > div.crash__history.xhistory.xhistory_home > div > div > a:nth-child(4)")
    prelastcrash = saveprelast.text
    prelastcrash = float(prelastcrash[:-1])
    return prelastcrash
def last_crash_5():
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
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__head > div.inventory__toggle > label > div"))).click()
        time.sleep(0.2)
def balance():
    savebalance = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__head > div.inventory__balance > div.inventory__count.symbol_usd")
    balance = float(savebalance.text)
    savevybrano = driver.find_element(By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__head > div.inventory__selected > div.inventory__count.symbol_usd")
    vybrano = float(savevybrano.text)
    vsego=round((balance+vybrano), 2)
    return vsego
def zakup(bal, bet, type):
    if type==1:
        # магазин скинов
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__footer > button"))).click()
        # цена
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__filters.filters.filter_shop > div.filter.filter_price > input"))).clear()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__filters.filters.filter_shop > div.filter.filter_price > input"))).send_keys(str(round(((bal-podushka) * bet), 2)))
        # первый предмет
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.window__inventory.ng-star-inserted > div > div > div:nth-child(1)"))).click()
        # подтвердить
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__controllers > div.shop__buy > button"))).click()
        # крестик
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__head > div.shop__close"))).click()
        return 1
    if type == 2:
        if (bet>(bal-podushka)): return 0
        else:
            # магазин скинов
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-inventory > div > div.inventory__footer > button"))).click()
            # цена
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__filters.filters.filter_shop > div.filter.filter_price > input"))).clear()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__filters.filters.filter_shop > div.filter.filter_price > input"))).send_keys(str(round((bet), 2)))
            # первый предмет
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.window__inventory.ng-star-inserted > div > div > div:nth-child(1)"))).click()
            # подтвердить
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__controllers > div.shop__buy > button"))).click()
            # крестик
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > app-root > app-wrapper > div > div.aside.aside_game.ng-tns-c79-0.ng-trigger.ng-trigger-gameSidebarAnimation > div > div > app-shop > div > div.shop__head > div.shop__close"))).click()
            return 1
def start():
    # начать
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > app-wrapper > div > div.container.container_main.ng-tns-c79-0.ng-trigger.ng-trigger-containerAnimation > div > app-crash-home > div > div.crash__controller > div.crash__information > div > button"))).click()

print("Введите любой символ, если хотите изменить параметры ставок или нажмите Enter, в этом случае будут выбраны последние настроенные параметры:")
file=open("textfail.txt", 'r')
type_of_bet=float(file.readline())
if type_of_bet == 1:
    stav=float(file.readline()); rubish=1
    while 1:
        print(rubish,"- й краш - ", stav*100, "% текущего баланса")
        stav = float(file.readline())
        rubish+=1
        if stav==1:
            print(rubish,"- й краш - ", stav*100, "% текущего баланса")
            break
    print("Динамический баланс" )
if type_of_bet==2:
    print("1-й краш - ",float(file.readline()),"$\n2-й краш - ",float(file.readline()),"$\n3-й краш - ",float(file.readline()),"$\n4-й краш - ",float(file.readline()),"$\n5-й краш - ",float(file.readline()), "$")
    print("Статический баланс")
file.close()
default=input()
if default=="":
    time.sleep(1)
    file=open("textfail.txt", 'r')
    type_of_bet = int(file.readline());st1=float(file.readline()); st2=float(file.readline()); st3=float(file.readline()); st4=float(file.readline()); st5=float(file.readline())
    file.close()
else:
    type_of_bet = wait_int("Какой баланс? (введите номер выбраного варианта)\n1. Динамический\n2. Статический")
    number_of_crash=wait_int("Введите номер очередного краша, после которого хотите ставить")
    st=[0,0,0,0,0]
    if type_of_bet == 1:
        for i in range(number_of_crash, 6):
            st[i-1]=wait_int("Введите часть баланса в %, которую вы хотите ставить после "+str(i)+"-ого краша")/100
            if (st[i-1]==1):
                for j in range (i+1, 6):
                    st[j-1]=1
                break
    if type_of_bet== 2:
        for i in range(number_of_crash, 6):
            st[i-1]=wait_float("Введите сумму в $, которую вы хотите ставить после "+str(i)+"-ого краша")
    st1=st[0];st2=st[1];st3=st[2];st4=st[3];st5=st[4]
    file=open("textfail.txt", 'w')
    file.write(str(type_of_bet) + "\n"); file.write(str(st1) + "\n"); file.write(str(st2) + "\n"); file.write(str(st3) + "\n"); file.write(str(st4) + "\n"); file.write(str(st5) + "\n")
    file.close()
    print("Итак, бот ставит по следующей стратегии:")
    if type_of_bet==1:
        rubish=0
        while 1:
            print(rubish+1,"- й краш - ", st[rubish]*100, "% текущего баланса")
            rubish+=1
            if st[rubish]==1:
                print(rubish+1,"- й краш - ", st[rubish]*100, "% текущего баланса")
                break
        print("Динамический баланс" + "\n")
    else:
        print("1-й краш - ", st1, "$\n2-й краш - ", st2,"$\n3-й краш - ", st3,"$\n4-й краш - ", st4,"$\n5-й краш - ", st5,"$")
        print("Статический баланс" + "\n")
podushka=wait_float("Введите несгораемую сумму:")

# авторизация
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get("https://cs.fail")
autorisation()

while 1:
    time.sleep(0.5)
    a= last_crash()
    if a < 1.2:
        if st1 != 0:
            click(1)
            bal = balance()
            zakup(bal, st1, type_of_bet)
            click(2)
            start()
            click(1)
        a2 = last_crash_2()
        while a2 >= 1.2:
            a2= last_crash_2()
        a = last_crash()
        if a < 1.2:
            if st2 != 0:
                print("Двойной", st2)
                click(1)
                bal = balance()
                zakup(bal, st2, type_of_bet)
                click(2)
                start()
                click(1)
            a3 = last_crash_3()
            while a3 >= 1.2:
                a3 = last_crash_3()
            a = last_crash()
            if a < 1.2:
                if st3 != 0:
                    if st2==1:
                        break
                    print("Тройной", st3)
                    click(1)
                    bal = balance()
                    zakup(bal, st3, type_of_bet)
                    click(2)
                    start()
                    click(1)
                a4 = last_crash_4()
                while a4 >= 1.2:
                    a4 = last_crash_4()
                a = last_crash()
                if a < 1.2:
                    if st4 != 0:
                        if st3 == 1:
                            break
                        print("Четверной", st4)
                        click(1)
                        bal = balance()
                        zakup(bal, st4, type_of_bet)
                        click(2)
                        start()
                        click(1)
                    a5 = last_crash_5()
                    while a5 >= 1.2:
                        a5 = last_crash_5()
                    a = last_crash()
                    if a < 1.2:
                        print("Пятерной краш")
                        if st5 != 0:
                            if st4 == 1:
                                break
                            click(1)
                            bal = balance()
                            zakup(bal, st5, type_of_bet)
                            click(2)
                            start()
                            click(1)
                        a5 = prex5_last_crash()
                        while a5 >= 1.2:
                            a5 = prex5_last_crash()
                        a = last_crash()
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
