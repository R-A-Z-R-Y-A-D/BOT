from telebot import types
import telebot
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

TOKEN='1622405338:AAHkL_FBzftlUe2DYtA-cQQ9JRKSt_qpmCc'
bot = telebot.TeleBot(TOKEN)
welcome_text="Привет 🥰.\n" \
             "Вот список доступных команд:\n" \
             "/list - просмотреть список текущих настроек\n" \
             "/begin - запустить бота\n" \
             "/set - изменить настройки"
perc = ["", "", "", "", ""]
type = 0
podushka = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    start_text = "Привет 😜\n" \
                 "Перед тем как запустить бота необходимо сделать некоторые настройки,\n" \
                 "чтобы бот работал корректно. Это не займет больше двух минут.\n\n" \
                 "Введи пять чисел от 0 до 100 через пробел, отражающие процент ставок:\n" \
                 "(наши рекомендации: 0 5 30 95 100)"
    bot.send_message(message.chat.id, start_text)
    @bot.message_handler(content_types=['text'])
    def perc(message):
        str=[x for x in message.text+"  "]
        global perc
        j = 0
        for i in range(5):
            while str[j]!=" ":
                perc[i]+=str[j]
                j+=1
            j+=1
            perc[i]=round(float(perc[i])/100, 2)
        text_type = "Введи тип ставок:\n\n" \
                    "1. Динамический\n" \
                    "2. Статический"
        bot.send_message(message.chat.id, text_type)
    bot.register_next_step_handler(message, )
    @bot.message_handler(content_types=['text'])
    def type(message):
        global type
        type = float(message.text)
        print(perc[1])
        print(type)
bot.polling()