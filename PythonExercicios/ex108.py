from modulo107 import moeda
num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumenta(num, 10))}')
print(f'Diminuindo 13% temos {moeda.moeda(moeda.diminui(num, 13))}')
