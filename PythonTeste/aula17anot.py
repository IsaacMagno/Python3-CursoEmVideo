# Listas
# Listas podem ser iniciadas com:
valores = []
valores = list()

# Para adicionar valores a uma lista substituindo um valor já existente
valores[1, 2, 3, 4]
valores[3] = 5 # O terceiro elemento da lista passará a ser o número 5

# Para adicionar valores  a uma lista na ultima posição
num.append()

# Para adicionar valores a uma lista em um local especifico
# 2 = posição onde vai começar // 0 = valor a ser adicionado após a posição 2
num.insert(2, 0) # Entre os parenteses colocar o valor que deseja adicionar a lista



# Para organizar os valores em ordem crescente
num.sort()
# Para organizar os valores de ordem inversa
num.sort(reverse=True)

# Para saber quantos elementos existem em uma lista
len(num)

# Para remover um elemento
# Se () estiver vazia = remove ultimo elemento da lista
# Se preencher () com o número do elemento remove o elemento descrito
num.pop()

# O remove procura do inicio da lista a primeira ocorrencia do valor que você mandou eliminar e elimina
num.remove(2)
# Caso o valor não esteja presente na lista é apresentado um erro, para evita-lo use o seguinte metodo:
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')

# Para saber o indice e o valor de cada posição na lista
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

# Para ler valores pelo teclado e adiciona-los a uma lista
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# Se uma variavel recebe uma lista é criada uma ligação entre elas
# Para fazer uma copia sem a ligação entre a lista e a variavel use o seguinte metodo
a = [2, 3, 4, 7]
b = a[:] # Se não for especificado quais valores devem ser copiados da lista, a ligação entre a lista  e a variavel é feita
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Para criar uma lista a partir de range
valores = list(range(4, 11))
