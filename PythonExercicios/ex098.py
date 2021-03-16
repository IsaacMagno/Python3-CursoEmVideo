from time import sleep


def contador(a, b, c):
    print(f'Contando de {a} a {b} pulando de {c} em {c}:')
    if a < b:
        b += 1
        for c in range(a, b, c):
            print(f'{c} ', end='')
            sleep(0.5)
        print()
    if b < a:
        if b == 0:
            b -= 2
        else:
            b -= 1
        for c in range(a, b, -c):
            print(f'{c} ', end='')
            sleep(0.5)
        print()


contador(1, 10, 1)
contador(10, 0, 2)
a1 = int(input('Inicio: '))
b1 = int(input('Fim: '))
c1 = int(input('Passo: '))
if c1 < 0:
    c1 = c1 * -1
elif c1 == 0:
    c1 = 1
contador(a1, b1, c1)
