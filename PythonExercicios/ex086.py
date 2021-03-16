matriz = list()
num = list()
for c in range(0, 9):
    if c < 3:
        valor = int(input(f'Digite um valor para a posição [{c + 1}]: '))
        num.insert(c, valor)
        matriz.append(num[:])
        num.clear()
    elif 3 <= c < 6:
        valor = int(input(f'Digite um valor para a posição [{c + 1}]: '))
        num.insert(c, valor)
        matriz.append(num[:])
        num.clear()
    elif c >= 6:
        valor = int(input(f'Digite um valor para a posição [{c + 1}]: '))
        num.insert(c, valor)
        matriz.append(num[:])
        num.clear()
print(f'\n{matriz[0]} {matriz[1]} {matriz[2]}')
print(f'{matriz[3]} {matriz[4]} {matriz[5]}')
print(f'{matriz[6]} {matriz[7]} {matriz[8]}')
