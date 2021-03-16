from random import randint
from time import sleep
lista = list()
jogos = list()
ask = int(input('Quantos jogos você quer sortear? '))
tot = 1
while tot <= ask:
    cont = 0
    while True:
        random = randint(1, 60)
        if random not in lista:
            lista.append(random)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print(f'SORTEANDO {ask} JOGOS')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('\nBoa sorte!')
