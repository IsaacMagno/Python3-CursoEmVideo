s = 0
c1 = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        c1 += 1
print('O resultado da soma de todos os {} numeros pares digitados é: {}'.format(c1, s))
