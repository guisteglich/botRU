import telebot
from bs4 import BeautifulSoup

import requests

from web import get_time

CHAVE_API = "5230582028:AAEYZ0r4jNv1nO0tHqwZa1NP7r3qyq80oZ4"
html = requests.get("https://www.furg.br/estudantes/cardapio-ru/restaurante-universitario-i").content
soup = BeautifulSoup(html, 'html.parser')

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["ola"])
def response(message):
    txt = "Olá! Eu sou o Bot do RU da FURG."
    bot.reply_to(message, txt)

@bot.message_handler(commands=["horarios"])
def response_to_time(message):
    time = get_time(soup)
    bot.reply_to(message, "Os horário são: {}".format(time))

bot.polling()