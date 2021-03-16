#meu metodo (funciona porque o capitalize deixa apenas a primeira letra maiscula)
#(logo se santo nao for a primeira palavra vai dar erro)

city = str(input('Em que cidade você nasceu? ')).strip().capitalize()
print('Santo' in city)


#metodo da aula
'''cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper()=='SANTO')'''


