n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('{} é o numero de MAIOR valor'.format(n1))
if n2 > n1:
    print('{} é o numero de MAIOR valor'.format(n2))
if n1 == n2:
    print('{} e {} tem o MESMO valor'.format(n1, n2))
