from random import randint
numalt = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = numalt[0]
print(f'Os números sorteados foram: {numalt[0]}, {numalt[1]}, {numalt[2]}, {numalt[3]}, {numalt[4]}.')
for c in range(0, len(numalt)):
    if numalt[c] > maior:
        maior = numalt[c]
    elif numalt[c] < menor:
        menor = numalt[c]
print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')
