a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
termo = a1
while c <= 10:
    print('{}'.format(termo), end='')
    print(' > ' if c < 10 else '', end=''),
    termo += r
    c += 1
print('\nEsses são os dez primeiros termos da PA solicitada.')