r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim é possivel formar um triangulo!')
    if r1 == r2 == r3:
        print('É um triangulo EQUILÁTERO e tem todos os lados iguais.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É  um triangulo ISÓCELES e tem dois lados iguais.')
    elif r1 != r2 != r3 != r1:
        print('É um triangulo ESCALENO e todos os lados são diferentes.')
else:
    print('Não é possivel formar um triangulo!')
