from datetime import date
ano = date.today().year
registro = dict()
registro['nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
idd = ano - idade
registro['ano'] = idd
registro['ctps'] = int(input('Carteira de trabalho: '))
if registro['ctps'] > 0:
    anoctt = int(input('Ano de contratação: '))
    registro['contrataçao'] = anoctt
    anoctt = (anoctt + 35) - idade
    registro['aposentadoria'] = anoctt
    registro['salario'] = float(input('Salario: '))
for k, v in registro.items():
    print(f'{k} tem o valor {v}')
