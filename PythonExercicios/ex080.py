valores = list()
for cont in range(0, 5):
    val = int(input('Digite um valor: '))
    if cont == 0:
        valores.append(val)
        print('Valor adicionado ao final da lista!')
    elif cont >= 1:
        maior = max(valores)
        menor = min(valores)
        if val > maior:
            valores.append(val)
            print('Valor adicionado ao final da lista!')
        elif val < menor:
            valores.insert(0, val)
            print('Valor adicionado na posição 0 da lista!')
        else:
            valores.insert(-1, val)
            print('Valor adicionado na posição 1 da lista!')
print(f'\nOs valores digitados em ordem foram: {valores}')
