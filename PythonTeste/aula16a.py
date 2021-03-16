lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')



#Se precisar da posição da tupla

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#tuplas são imutáveis

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')

#Sorted = em ordem
print(sorted(lanche))
