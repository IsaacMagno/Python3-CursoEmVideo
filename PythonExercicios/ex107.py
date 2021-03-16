from modulo107 import moeda
num = float(input('Digite o preço: R$ '))
print(f'A metade de {num:.2f} é {moeda.metade(num):.2f}')
print(f'O dobro de {num:.2f} é {moeda.dobro(num):.2f}')
print(f'Aumentando 10% temos {moeda.aumenta(num, 10):.2f}')
print(f'Diminuindo 13% temos {moeda.diminui(num, 13):.2f}')
