import telebot
# from bs4 import BeautifulSoup

# import requests

# from web import get_time


# html = requests.get("https://www.furg.br/estudantes/cardapio-ru/restaurante-universitario-i").content
# soup = BeautifulSoup(html, 'html.parser')

bot = telebot.TeleBot(CHAVE_API)

# @bot.message_handler(commands=["horarios"])
# def response_to_time(message):
#     time = get_time(soup)
#     bot.reply_to(message, "Os horário são: {}".format(time))

@bot.message_handler(commands=["cardapio"])
def response_to_menu(message):
    bot.send_message(message.from_user.id, "o cardápio de hoje é sopa.")

def verify(message):
    return True

@bot.message_handler(func=verify)
def response(message):
    txt = """Olá! Eu sou o Bot do RU da FURG.

/horarios para saber os horários de funcionamento do RU.
/cardapio para saber o cardápio do dia no RU.

Clique em alguma das opções acima. 
    """
    bot.reply_to(message, txt)

# @bot.message_handler(commands=["horarios"])
# def response_to_time(message):
#     time = get_time(soup)
#     bot.reply_to(message, "Os horário são: {}".format(time))

bot.polling()