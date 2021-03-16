def metade(n, mon=False):
    m = n / 2
    if mon:
        return moeda(m)    # ex 109
    return m


def dobro(n, mon=False):
    d = n * 2
    if mon:
        return moeda(d)    # ex 109
    return d


def aumenta(n, p, mon=False):
    a = (n * p / 100) + n
    if mon:
        return moeda(a)   # ex 109
    return a


def diminui(n, p1, mon=False):
    d = n - (n * p1 / 100)
    if mon:
        return moeda(d)    # ex 109
    return d


# ex108
def moeda(n=0, coin='R$'):
    return f'{coin} {n:.2f}'.replace('.', ',')


# ex110
def resumo(n, a, b):
    print('-' * 33)
    print(f'{"RESUMO DO VALOR":^33}')
    print('-' * 33)
    print(f'Preço analisado:  {moeda(n)}')
    print(f'Dobro do preço:   {dobro(n, True)}')
    print(f'Metade do preço:  {metade(n, True)}')
    print(f'{a}% de aumento:   {aumenta(n, a, True)} ')
    print(f'{b}% de desconto:  {diminui(n, b, True)}')
    print('-' * 33)
