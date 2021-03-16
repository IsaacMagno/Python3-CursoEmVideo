salario = float(input('Digite seu salário: R$ '))

if salario > 1250.00:
    print('Seu novo salario é R$ {:.2f}'.format(salario * 10 / 100 + salario))
else:
    print('Seu novo salario é R$ {:.2f}'.format(salario * 15 / 100 + salario))
