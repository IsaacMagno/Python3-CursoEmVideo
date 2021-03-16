'''import random
p1 = input('Digite o nome do primeiro aluno: ')
p2 = input('Digite o nome do segundo aluno: ')
p3 = input('Digite o nome do terceiro aluno: ')
nomes = random.choice([p1,p2,p3])
print('O escolhido foi: {}'.format(nomes))'''

import random
import playsound
print('Sorteando...')
playsound.playsound('rodajequiti.mp3')
nomes = random.choice(['Isaac', 'Esdras', 'Paulo', 'Isaac', 'Esdras', 'Paulo', 'Isaac', 'Esdras', 'Paulo'])
print('O escolhido para bolar o super beck insano foi:  {}'.format(nomes))
playsound.playsound('rodajequiti2.mp3')
