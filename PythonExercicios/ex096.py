def area(a1, b1):
    mt2 = a1 * b1
    print(f'A área de um terreno {a1} x {b1} é de {mt2}m². ')


print('Controle de Terrenos')
print()
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a, b)
