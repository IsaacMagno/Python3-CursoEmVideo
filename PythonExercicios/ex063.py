n = int(input('Quantos termos você quer mostrar? '))
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print('1')
else:
    print('0 > 1 > 1 > ', end='')
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print('{} > '.format(termo), end='')
print('Aqui estão os {} primeiros termos da sequencia Fibonacci.'.format(n))
