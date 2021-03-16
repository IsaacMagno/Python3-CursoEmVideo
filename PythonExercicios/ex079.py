valores = list()
while True:
    val = int(input('Digite um valor: '))
    if val in valores:
        print('Este número já está na lista e não foi adicionado.')
    else:
        print('Valor adicionado a lista!')
        valores.append(val)
    ask = ' '
    while ask not in 'SsNn':
        ask = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if ask == 'N':
        break
valores.sort()
print(f'Você digitou os valores: {valores}')
