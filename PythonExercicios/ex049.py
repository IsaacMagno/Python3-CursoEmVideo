n = int(input('Digite um número para gerar sua tabuada: '))
for t in range(1, 11):
    print('{} x {:2} : {}'.format(n, t, n * t))
