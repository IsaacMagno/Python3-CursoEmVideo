total = mil = c = 0
prodt = ''
menor = 0
while True:
    while True:
        produto = str(input('Nome do produto: ')).title().strip()
        if produto.isalpha():
            True
            break
        else:
            produto = str(input('Nome do produto: ')).title().strip()
    preço = float(input('Preço R$: '))
    c += 1
    if c == 1:
        menor = preço
        prodt = produto
    else:
        if preço < menor:
            menor = preço
            prodt = produto
    if preço >= 1000:
        mil += 1
    total += preço
    while True:
        ask = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if ask == 'S':
            break
        if ask == 'N':
            break
        else:
            ask = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if ask == 'N':
        break
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {mil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {prodt} que custa R$ {menor:.2f}.')
