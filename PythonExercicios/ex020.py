from random import shuffle
p1 = input('Digite o primeiro nome: ')
p2 = input('Digite o segundo nome: ')
p3 = input('Digite o terceiro nome: ')
deck = [p1, p2, p3]
shuffle(deck)
print('A ordem de apresentação será: {}'.format(deck))
