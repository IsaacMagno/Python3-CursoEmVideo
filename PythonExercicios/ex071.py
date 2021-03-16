dinheiro = int(input('Qual valor você quer sacar? R$ '))
resto = 0
inteiro50 = inteiro20 = inteiro10 = inteiro01 = 0
while True:
    cinquenta = dinheiro % 50
    inteiro50 = dinheiro // 50
    resto = cinquenta
    if resto > 0:
        inteiro20 = resto // 20
        vinte = resto % 20
        resto = vinte
        if resto > 0:
            inteiro10 = resto // 10
            dez = resto % 10
            resto = dez
            if resto > 0:
                inteiro01 = resto // 1
                um = resto % 1
                resto = um
    if resto == 0:
        break
if inteiro50 > 0:
    print(f'Total de {inteiro50} cédulas de R$ 50')
if inteiro20 > 0:
    print(f'Total de {inteiro20} cédulas de R$ 20')
if inteiro10 > 0:
    print(f'Total de {inteiro10} cédulas de R$ 10')
if inteiro01 > 0:
    print(f'Total de {inteiro01} cédulas de R$ 1')
