import random
import playsound
n = random.randint(1, 6)
print('Pensei em um número de 1 a 5, tente adivinhar!')
r = int(input('Digite o número em que pensei: '))
if r == n:
    print('Uau! Você adivinhou o que eu estava pensando, PARABENS!')
else:
    print('Que pena, você errou! O número em que pensei era {}.' .format(n))
    playsound.playsound('silviopena.mp3')
