numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    ask = ' '
    while ask not in 'SsNn':
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if ask == 'N':
        break
print(f'\nVocê digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os números digitados em ordem decrescente foram {numeros}')
if 5 in numeros:
    print(f'O número cinco foi digitado {numeros.count(5)} vezes e foi encontrado pela primeira vez na posição'
          f' {numeros.index(5)}.')
else:
    print('O número cinco não está na lista!')
