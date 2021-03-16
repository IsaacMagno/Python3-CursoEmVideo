from random import randint
cpu = randint(1, 10)
erro = 0
print('Pensei em um número de 1 a 10, tente adivinhar!')
r = int(input('Digite o número em que pensei: '))
if r == cpu:
    print('Uau! Você adivinhou o que eu estava pensando, PARABÉNS!')
while r != cpu:
    print('Não foi dessa vez, mas tente novamente. ', end='')
    if r < cpu:
        print('Quem sabe dessa vez com um numero maior...')
    elif r > cpu:
        print('Quem sabe dessa vez com um numero menor...')
    erro += 1
    r = int(input('Resposta: '))
    if r == cpu:
        print('Boa!! Até que enfim você acertou, já estava quase dormindo aqui, ha³.')
        print('Você tentou {} vezes antes de adivinhar que {} era o número em que eu estava pensando.'.format(erro, cpu))

#metodo da aula

'''from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))'''
