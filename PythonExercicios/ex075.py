num =(int(input('Digite um número: ')),
    int(input('Outro número: ')),
    int(input('Mais um número: ')),
    int(input('Ultimo número: ')))
print(f'Os valores digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if num.count(3) > 0:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
