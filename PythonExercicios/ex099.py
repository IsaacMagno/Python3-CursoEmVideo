from time import sleep


def maior(*num):
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.2)
    print(f'Foram infomados {len(num)} valores ao todo.')
    if len(num) == 0:
        print(f'Nenhum valor foi informado.')
    else:
        print(f'E o maior número é {max(num)}.')
    print()


maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(2, 3, 4, 5, 6, 12, 999, 1)
maior(3, 2)
maior(6)
maior()
