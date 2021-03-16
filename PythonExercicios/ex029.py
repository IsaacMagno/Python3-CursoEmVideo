n = float(input('Digite a velocidade atual do carro: '))
if n > 80:
    print('Você ultrapassou a velocidade limite e foi multado em R${},00. '.format((n-80)*7))
else:
    print('Voce está na velocidade ideal, Parabéns! ')
