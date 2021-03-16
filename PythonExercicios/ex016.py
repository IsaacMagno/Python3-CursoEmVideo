from math import ceil, floor
n = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(n, floor(n)))
print('E arredondado para cima {}'.format(ceil(n)))
