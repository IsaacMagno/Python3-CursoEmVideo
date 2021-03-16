matriz = list()
num = list()
par = col3 = 0
for c in range(0, 9):
    if c < 3:
        valor = int(input(f'Digite um valor para a posição [{c + 1}]: '))
        num.insert(c, valor)
        matriz.append(num[:])
        num.clear()
        if valor % 2 == 0:
            par += valor
        if c == 2:
            col3 += valor
    elif 3 <= c < 6:
        valor = int(input(f'Digite um valor para a posição [{c + 1}]: '))
        num.insert(c, valor)
        matriz.append(num[:])
        num.clear()
        if valor % 2 == 0:
            par += valor
        if c == 5:
            col3 += valor
    elif c >= 6:
        valor = int(input(f'Digite um valor para a posição [{c + 1}]: '))
        num.insert(c, valor)
        matriz.append(num[:])
        num.clear()
        if valor % 2 == 0:
            par += valor
        if c == 8:
            col3 += valor
print(f'\n{matriz[0]} {matriz[1]} {matriz[2]}')
print(f'{matriz[3]} {matriz[4]} {matriz[5]}')
print(f'{matriz[6]} {matriz[7]} {matriz[8]}')
print(f'\nA soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {max(matriz[3:6])}')
