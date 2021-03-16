from random import randint
print('Vamos jogar PAR ou ÌMPAR?')
wins = 0
while True:
    cpu = randint(0, 10)
    player = int(input('Digite seu número: '))
    ask = str(input('Par ou Ìmpar? [P / I]: ')).upper().strip()[0]
    while ask != 'P' and ask != 'I':
        ask = str(input('Par ou Impar? [P / I]: ')).upper().strip()[0]
    if ask == 'P':
        print(f'Você jogou {player} e o computador {cpu}. ', end='')
        soma = player + cpu
        resto = soma % 2
        if resto == 0:
            print('Você Venceu!')
            wins += 1
        if resto == 1:
            print('Você perdeu!')
            break
    elif ask == 'I':
        print(f'Você jogou {player} e o computador {cpu}. ', end='')
        soma = player + cpu
        resto = soma % 2
        if resto == 0:
            print('Você Perdeu!')
            break
        if resto == 1:
            print('Você Venceu!')
            wins += 1
print(f'GAME OVER! Você venceu {wins} vezes.')
