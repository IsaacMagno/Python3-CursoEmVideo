from random import randint
from time import sleep
jogos = list()
ask = int(input('Quantos jogos você quer sortear? '))
print(f'\nSORTEANDO {ask} JOGOS:')
sleep(1)
for c in range(0, ask):
    while True:
        random = randint(1, 60)
        if random not in jogos:
            jogos.append(random)
        if len(jogos) == 6:
            break
    print(f'Jogo {c + 1}: {jogos}')
    jogos.clear()
    sleep(1)
print('\nBoa sorte!')
