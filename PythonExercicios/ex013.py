s= float(input('Digite seu salário: '))

ns = s * 15/100
nv = s + ns

print('Seu novo salário é de R$ {:.2f}'.format(nv))
print('Seu aumento foi de {:.2f}'.format(ns))
