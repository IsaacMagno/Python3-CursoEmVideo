from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print('Sorteando: ', end='')
    for c in range(0, 5):
        rnd = randint(0, 10)
        print(f'{rnd} ', end='')
        numeros.append(rnd)
        sleep(0.3)
    print('Pronto!')


def soma(lista):
    sma = 0
    print(f'Somando os números pares de {numeros}: ', end='')
    for n in numeros:
        if n % 2 == 0:
            sma += n
    print(f'Temos {sma}.')


sorteia(numeros)
soma(numeros)
