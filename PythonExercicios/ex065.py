n = c = soma = maior = menor = 0
ask = 'S'
while ask != 'N':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    ask = str(input('Continuar? [S / N]: ')).upper()
print('A média entre todos os {} valores é {:.2f}.'.format(c, soma / c))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
