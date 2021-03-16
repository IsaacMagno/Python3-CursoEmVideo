#metodo da aula
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')
'''n = int(input('Digite um número inteiro: '))
s = 0
for count in range(2, n):
    if n % count == 0:
        print('Multiplo de: ', count)
        s += 1
if s == 0:
    print('É primo')
else:
    print('Tem', s, 'multiplos acima de 2 e abaixo de', n)'''