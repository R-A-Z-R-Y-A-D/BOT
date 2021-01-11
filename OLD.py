import pyautogui
import time
import pyperclip
def scan1():
    file = open("test.txt", 'w')
    # последний краш
    pyautogui.moveTo(1245 , 561)
    pyautogui.rightClick()
    # копировать для последнего краша
    pyautogui.click(1324 , 749)
    time.sleep(0.4)
    file.write(pyperclip.paste() + "\n")
    file.close()
    file = open("test.txt", 'r')
    b = file.readline()
    b = b[1:]
    b = float(b)
    file.close()
    return (b)

def scan2():
    file = open("test.txt", 'w')
    # ппредоследний краш
    pyautogui.moveTo(1296 , 558)
    pyautogui.rightClick()
    # копировать для предпоследнего краша
    pyautogui.click(1369 , 752)
    time.sleep(0.4)
    file.write(pyperclip.paste() + "\n")
    file.close()
    file = open("test.txt", 'r')
    a = file.readline()
    a = a[1:]
    a = float(a)
    file.close()
    return(a)

def wait_float(str=""):
    print(str)
    while True:
        a=input()
        try:
            float(a)
            return (float(a))
        except ValueError:
            print("uncorrect syntax")

def wait_int(str=""):
    print(str)
    while True:
        a=input()
        if (a.isdigit()):
            break
        print("uncorrect syntax")
    return (int(a))

def balance():
    file = open("sum.txt", 'w')
    # баланс (целая часть)(левая цифра)
    pyautogui.moveTo(1632, 132)
    pyautogui.doubleClick()
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    file.write(pyperclip.paste())
    file.close()
    file = open("sum.txt", 'r')
    vybrano = float(file.readline())
    file.close()
    return (vybrano)

def selected():
    # выбрать все (кнопка)
    #pyautogui.doubleClick(407, 903)
    file = open("sum.txt", 'w')
    # выбрано
    pyautogui.moveTo(136,640)
    pyautogui.doubleClick()
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.4)
    file.write(pyperclip.paste())
    file.close()
    file = open("sum.txt", 'r')
    vybrano = float(file.readline())
    file.close()
    return (vybrano)

def stavka_const(bet=float()):
    # нажать макс цена (поле для ввода)
    pyautogui.doubleClick(664 , 221)
    pyautogui.press('backspace')
    vmaxcenu = str(bet)
    print(vmaxcenu)
    for elem in vmaxcenu:
        pyautogui.press(elem)
        time.sleep(0.05)
    time.sleep(0.2)
    # верхний левый предмет в обмене
    pyautogui.click(560, 352)
    # второй предмет
    pyautogui.click(670, 325)
    # третий предмет
    pyautogui.click(761, 325)
    # четвертый предмет
    pyautogui.click(871, 326)
    # подтвердить
    pyautogui.click(689, 906)
    time.sleep(1)
    #первый предмет в инвентаре
    pyautogui.click(120,742)
    time.sleep(0.2)
    # начать
    for blabla in range(1):
        pyautogui.click(264 , 515)
        time.sleep(0.3)
    # выбрать все (кнопка)
    pyautogui.click(407, 903)

def stavka (chast=float(), balance=float()):
    vsego = balance
    # нажать макс цена (поле для ввода)
    pyautogui.doubleClick(664 , 221)
    pyautogui.press('backspace')
    vmaxcenu = str(round((vsego) * chast - 0.01, 2))
    for elem in vmaxcenu:
        pyautogui.press(elem)
        time.sleep(0.05)
    time.sleep(0.35)
    # верхний левый предмет в обмене
    pyautogui.click(560,352)
    # второй предмет
    pyautogui.click(670,325)
    # третий предмет
    pyautogui.click(761,325)
    # четвертый предмет
    pyautogui.click(871,326)
    #подтвердить
    pyautogui.click(689,906)
    time.sleep(0.3)
    #первый предмет в инвенте
    pyautogui.click(120,742)
    time.sleep(0.5)
    # начать
    for blabla in range(1):
        pyautogui.click(264 , 515)
        time.sleep(0.3)
    # выбрать все (кнопка)
    pyautogui.click(407, 903)


zapas = wait_float("Enter your save packet: ")
number_of_crash = wait_int("Enter number of running crash after which you wanna bet: ")
while True:
    typebet=wait_int("Enter wishful type of bet (1 or 2)\n1.dynamic\n2.const\n")

    if(typebet==1 or  2):
        break
    print()
if(typebet==2):
    fbet=wait_float("Enter minimal bet ($): ")
    bet_coef = wait_float("Enter coefficient between bets: ")
else:
    parts=[]
    for blabla in range (4-number_of_crash):
        parts.append(wait_float("Enter part of balance to bet after " + str(blabla + number_of_crash) + " crash"))

currentMouseX, currentMouseY = pyautogui.position()
# нажать магазин скинов
pyautogui.click(144 , 899)
# выбрать все (кнопка)
pyautogui.click(407, 903)
while(currentMouseX!=0 and currentMouseY!=0):
    currentMouseX, currentMouseY = pyautogui.position()
    a=scan1()
    bal = balance() + selected()-zapas
    if (a<1.2):
        print("single")
        if(number_of_crash<=1):
            if(typebet==2):
                if(bet_coef**(number_of_crash-1)*fbet>=bal):
                    number_of_crash+=1
                else:
                    stavka(bet_coef ** (number_of_crash - 1) * fbet)
            else:
                stavka(parts[0], bal)
        a = scan1()
        b = scan2()
        a_2=scan1()
        b_2=scan2()
        while (currentMouseX != 0 and currentMouseY != 0):
            currentMouseX, currentMouseY = pyautogui.position()
            a_2 = scan1()
            b_2 = scan2()
            if(a_2!=a or b_2!=b):
                break
        if (a_2<1.2):
            a_chek=scan1()
            if(a_chek<1.2):
                print("Double")
                bal = balance()+selected()-zapas
                if (number_of_crash <= 2):
                    if (typebet == 2):
                        if (bet_coef ** abs(number_of_crash - 2) * fbet >= bal):
                            number_of_crash += 1
                        else:
                            stavka(bet_coef ** abs(number_of_crash - 2) * fbet)
                    else:
                        stavka(parts[abs(number_of_crash-2)], bal)
                a_2 = scan1()
                b_2=scan2()
                a_3=scan1()
                b_3=scan2()
                while (currentMouseX != 0 and currentMouseY != 0):
                    currentMouseX, currentMouseY = pyautogui.position()
                    a_3 = scan1()
                    b_3 = scan2()
                    if(a_3!=a_2 or b_3!=b_2):
                        break
                if(a_3<1.2):
                    a_chek = scan1()
                    if (a_chek < 1.2):
                        print("triple")
                        bal=balance()+selected()-zapas
                        if (number_of_crash <= 3):
                            if (typebet == 2):
                                if (bet_coef ** abs(number_of_crash - 3) * fbet >= bal):
                                    number_of_crash += 1
                                    stavka(1,bal)
                                else:
                                    stavka(bet_coef ** abs(number_of_crash - 3) * fbet)
                            else:
                                stavka(parts[abs(number_of_crash - 3)], bal)
                        a_3 = scan1()
                        b_3 = scan2()
                        a_4=scan1()
                        b_4=scan2()
                        while (currentMouseX != 0 and currentMouseY != 0):
                            currentMouseX, currentMouseY = pyautogui.position()
                            a_4=scan1()
                            b_4=scan2()
                            if(a_4!=a_3 or b_4!=b_3):
                                break
                        if(a_4<1.2):
                            a_chek = scan1()
                            if (a_chek < 1.2):
                                print("quadruple")
                                bal = balance() + selected() - zapas
                                stavka(1, bal)
        # нажать макс цена (поле для ввода)
        pyautogui.doubleClick(664, 221)
        pyautogui.press('backspace')
        for elem in "0.25":
            pyautogui.press(elem)
            time.sleep(0.05)
        # выбрать все (кнопка)
        pyautogui.doubleClick(407, 903)
        time.sleep(0.35)
        # верхний левый предмет в обмене
        pyautogui.click(560, 352)
        # подтвердить
        pyautogui.click(689, 906)
        time.sleep(0.35)
        #первый предмет в инвенте
        pyautogui.click(120,742)
        print("\n")
    if(bal<=0):
        print("Now you have only your save packet")
        break