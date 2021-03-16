cmplt = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um número: '))
    cmplt.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    ask = ' '
    while ask not in 'SsNn':
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if ask == 'N':
        break
print(f'\nA lista completa é {cmplt}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
