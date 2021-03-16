dados = dict()
pessoas = list()
media = 0
while True:
    dados['nome'] = str(input('Nome: ')).title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F')
    idade = int(input('Idade: '))
    media += idade
    dados['idade'] = idade
    pessoas.append(dados.copy())
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? ')).strip().upper()[0]
    if ask == 'N':
        break
print(f'A) O grupo tem {len(pessoas)} pessoas.')
print(f'B) A média de idade do grupo é {media / len(pessoas)} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for c, p in enumerate(pessoas):
    if pessoas[c]["sexo"] == 'F':
        print(f'{pessoas[c]["nome"]}  ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
print()
for c, p in enumerate(pessoas):
    if pessoas[c]["idade"] > media / len(pessoas):
        print(f'{pessoas[c]}')
