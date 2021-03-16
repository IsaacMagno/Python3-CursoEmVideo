a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
n = int(input('Digite o numero alvo: '))
for pa in range(a1, r * n + a1, r):
    print(pa, end=' > ')


#metodo da aula

'''a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
n = a1 + (10 - 1) * r
for pa in range(a1, n + r, r):
    print(pa)'''