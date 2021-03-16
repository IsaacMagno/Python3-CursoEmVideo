completo = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        completo[0].append(valor)
    else:
        completo[1].append(valor)
completo[0].sort()
print(f'\nOs valores pares digitados foram: {completo[0]}')
completo[1].sort()
print(f'Os valores impares digitados foram: {completo[1]}')
