pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    ask = ' '
    while ask not in 'SsNn':
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if ask == 'N':
        break
print(f'O total de pessoas cadastradas é {len(pessoas)}.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {menor}. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
