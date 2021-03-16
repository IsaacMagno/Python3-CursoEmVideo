from time import sleep
print('*' * 15, 'BEM VINDO', '*' * 15)
ask = 0
n1 = int(input('Digite um valor : '))
n2 = int(input('Digite um valor: '))
while ask != 5:
    print('''O que você deseja fazer com os valores digitados?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa''')
    ask = int(input('Digite: '))
    if ask == 1:
        print('Somando os valores {} + {} = {}'.format(n1, n2, n1 + n2))
        sleep(1.5)
    if ask == 2:
        print('Multiplicando os valores {} * {} = {}'.format(n1, n2, n1 * n2))
        sleep(1.5)
    if ask == 3:
        maior = n1
        menor = n1
        if n2 > maior:
            maior = n2
            print('O número {} é maior que {}.'.format(maior, menor))
            sleep(1.5)
        if n2 < menor:
            menor = n2
            print('O número {} é maior que {}.'.format(maior, menor))
            sleep(1.5)
        if n1 == n2:
            print('Os dois números são iguais.')
            sleep(1.5)
    while ask == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))
        print('''O que você deseja fazer com os valores digitados?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa''')
        ask = int(input('Digite: '))
        if ask == 1:
            print('Somando os valores {} + {} = {}'.format(n1, n2, n1 + n2))
        if ask == 2:
            print('Multiplicando os valores {} * {} = {}'.format(n1, n2, n1 * n2))
        if ask == 3:
            maior = n1
            menor = n1
            if n2 > maior:
                maior = n2
                print('O número {} é maior que {}.'.format(maior, menor))
            if n2 < menor:
                menor = n2
                print('O número {} é maior que {}.'.format(maior, menor))
            if n1 == n2:
                print('Os dois números são iguais.')
sleep(1.5)
if ask == 5:
    print('Encerrando...')
    sleep(2)