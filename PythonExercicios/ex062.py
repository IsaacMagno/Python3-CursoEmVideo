a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
ask = 1
count = 0
count2 = 0
termo = a1
while ask != 0:
    while count < 10:
        print('{} > '.format(termo), end='')
        count += 1
        termo += r
        count2 += 1
    if count == 10:
        ask = int(input('Quantos termos você quer mostrar a mais?\nDigite: '))
        if ask == 0:
            print('Finalizando o programa com o total de {} termos mostrados.'.format(count2 + ask + 3))
        elif ask == 1:
            print('{} > '.format(termo), end='')
            count = (count - (ask - 1))
            termo += r
        else:
            ask -= 1
            print('{} > '.format(termo), end='')
            count = (count - ask)
            termo += r
