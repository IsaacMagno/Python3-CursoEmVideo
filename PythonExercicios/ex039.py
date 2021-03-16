'''ano = int(input('Em que ano você nasceu? '))
alist = 2020 - ano

if alist < 18:
    print('Em cerca de {} anos você precisa se alistar.'.format(18 - alist))
if alist > 18:
    print('Você já deveria ter se alistado a cerca de {} anos.'.format(alist - 18))
if alist == 18:
    print('Você deve se alistar esse ano!')'''

#Metodo da aula

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
