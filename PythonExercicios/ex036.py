casa = float(input('Digite o valor do imóvel a ser adquirido: '))
salario = float(input('Digite o salario do comprador: '))
anos = int(input('Em quantos anos você pretende pagar a casa: '))

prest = casa / (anos * 12)
tax = salario * (30/100)

if prest > tax:
    print('NEGADO. O valor das prestações seria de: R$ {:.2f} excedendo o limite de 30% que é de R$ {:.2f}'.format(prest, tax))
elif prest < tax:
    print('APROVADO. O valor das prestações será de: R$ {:.2f} estando dentro do limite de 30% que é de R$ {:.2f}'.format(prest, tax))
