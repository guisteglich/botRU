from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.furg.br/estudantes/cardapio-ru/restaurante-universitario-i").content

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

# valores = soup.find(class_="content-category")
# x = valores.find_all(class_="pagina__conteudo")

# # print(valores.prettify())
# print(x[1].prettify())

def get_price(soup):
    content = soup.find(class_="content-category")
    x = content.find_all(class_="pagina__conteudo")
    print(x[0].prettify())

    return x[0].prettify()


def get_time(soup):
    content = soup.find(class_="content-category")
    x = content.find_all(class_="pagina__conteudo")
    list = []
    for i in x[1]:
        print(i)
        list.append(i)
    # print(x[1].prettify())

    return list

get_time(soup)