# def split(s):
#     texto = s

#     r = texto.split("<p>")
#     dinner = r[3]
#     lunch = r[2]

#     a = lunch.replace("<br/>Segunda", "de Segunda")
#     b = a.replace("<br/>Sábados", "\nAos Sábados")
#     c = b.replace("13:30</p>", "13:30")

#     az = dinner.replace("<br/>Segunda", "de Segunda")
#     bz = az.replace("<br/>Sábados", "\nAos Sábados")
#     cz = bz.replace("19:30</p>, ' ']", "19:30")


#     print(c)
#     print("------------------")
#     print(cz)

#     return c + cz




# a = txt.replace('''<div class="pagina__conteudo">
# <p> </p>
# <p>''', "\n")

# #print(a)

# b = a.replace("<br/>Segunda", "de Segunda")
# c = b.replace("<br/>Sábados", "Aos Sábados")
# d = c.replace("13:30</p>", "13:30")
# e = d.replace("<p>Jantar", "Jantar")
# f = e.replace("19:30</p> </div>", "19:30")

# print(f)

def split(txt):
    a = txt.replace('''<div class="pagina__conteudo">
<p> </p>
<p>''', "\n")

    b = a.replace("<br/>Segunda", "de Segunda")
    c = b.replace("<br/>Sábados", "Aos Sábados")
    d = c.replace("13:30</p>", "13:30")
    e = d.replace("<p>Jantar", "Jantar")
    f = e.replace("19:30</p> </div>", "19:30")

    print(f)

    return f

# txt = ''' <div class="pagina__conteudo">
# <p> </p>
# <p>Almoço <br/>Segunda a sexta: das 11:00 às 14:00 <br/>Sábados, domingos e feriados: das 12:00 às 13:30</p>
# <p>Jantar <br/>Segunda a sexta: das 18:00 às 21:00 <br/>Sábados, domingos e feriados: das 18:30 às 19:30</p> </div>'''
# a = split(txt)

