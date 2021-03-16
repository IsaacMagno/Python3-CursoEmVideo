def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f' {c} ', end='')
            if c > 1:
                print('x', end='')
            else:
                print('= ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
print()
# help(fatorial)
