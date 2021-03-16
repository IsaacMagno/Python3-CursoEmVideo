'''ca = float(input('Digite o cateto A: '))
cb = float(input('Digite o cateto B: '))
x1 = ca*ca, cb*cb, #(ca+cb**1/2)
x2 = ca+cb**1/2
#x3 = x1+x2
#x4 = (x3**(1/2))
print('A hipotenusa do triangulo retangulo é de: {}'.format(x2))
print('Os valores são: {}'.format(x1))'''

'''co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
