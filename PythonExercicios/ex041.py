'''ano = int(input('Digite o ano em que você nasceu: '))
idade = 2020 - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
elif idade > 25:
    print('Categoria: MASTER')'''

#Método da aula

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <=14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação JUNIOR.')
elif idade <= 25:
    print('Classificação SENIOR.')
else:
    print('Classificação MASTER.')
