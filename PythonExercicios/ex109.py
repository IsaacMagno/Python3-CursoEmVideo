from modulo107 import moeda
num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num,True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10% temos {moeda.aumenta(num, 10, True)}')
print(f'Diminuindo 13% temos {moeda.diminui(num, 13, True)}')
