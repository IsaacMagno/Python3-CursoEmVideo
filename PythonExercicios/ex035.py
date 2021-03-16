r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if (r1 + r2) > r3:
    if (r1 + r3) > r2:
        if (r3 + r2) > r1:
            print('Sim é possivel formar um triangulo')
        else:
            print('Não é possivel formar um triangulo')
    else:
        print('Não é possivel formar um triangulo!')
else:
    print('Nao é possivel formar um triangulo!')

#metodo da aula

rr1 = float(input('Digite o comprimento da primeira reta: '))
rr2 = float(input('Digite o comprimento da segunda reta : '))
rr3 = float(input('Digite o comprimento da terceira reta: '))
if rr1 < rr2 + r3 and rr2 < r1 + r3 and r3 < r1 + r2:
    print('Sim é possivel formar um triangulo!')
else:
    print('Não é possivel formar um triangulo!')
