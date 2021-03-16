''' from math import cos, tan, sin
c = float(input('Digite o angulo: '))
co = cos(c)
ta = tan(c)
si = sin(c)
print('O angulo é {} e seu cosseno é {:.2f}\nA tangente é {:.2f}\nE o seno é {:.2f}.'.format(c, co, ta, si)) '''

import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
