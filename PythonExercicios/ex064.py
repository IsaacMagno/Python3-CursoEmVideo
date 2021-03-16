n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite o numero [999 para parar] : '))
    soma += n
    c += 1
    if n == 999:
        soma = soma - 999
        print('A soma de todos os {} números foi: {}'.format(c - 1, soma))
