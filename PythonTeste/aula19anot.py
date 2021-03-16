# Dicionarios
# Você pode juntar Listas, tuplas e dicionarios
# Para iniciar um dicionario
nomedodicionario = {}
nomedodicionario2 = dict()

# Ex de dicionario
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}


# Values pega todos os valores presentes no dicionario. Ex: Star Wars, 1977 e George Lucas são os valores do ex acima.
print(filme.values())
print()

# Keys para pegar apenas as chaves que indicam os valores no dicionario. Ex: titulo, ano, diretor
print(filme.keys())
print()

# Items se quiser pegar ambos os valores
print(filme.items())
print()

# Exemplo de como criar um lanço usando um dicionario
for k, v in filme.items():
    print(f'O {k} é {v}.')
print()

# Para adicionar um dicionario a uma lista (aula19b com ex)
locadora = list()
locadora.append(filme)                  # Varios dicionarios podem ser adicionados a uma mesma lista
# Ex de como mostrar o conteudo do dicionario usando uma lista
print(locadora[0]['titulo'])
print()

# Ex de como criar uma string formatada usando elementos presentes em um dicionario
pessoas = {'nome': 'Isaac', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()

# Ex de como adicionar um item ao dicionario
pessoas['peso'] = 80.0
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
# Ex de como remover um item de um dicionario
del pessoas['peso']

# Ex de como modificar um valor já existente em um dicionario
pessoas['nome'] = 'Esdras'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Ex de como adicionar itens a um dicionario usando range
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())      # Para fazer uma copia de um dicionario p/ uma lista

# Ex de prints possiveis
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

# Ex de como ordenar um dicionario utilizando uma lista
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos Jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}')
    sleep(1)

