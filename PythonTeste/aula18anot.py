# Listas 2

# Para copiar uma lista sem ligar ela a outra utilizar [:]
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Exemplo: caso o [] esteja preenchido com 0: apenas o nome será salvo
    dado.clear()           # Caso seja preenchido com 1: apenas a idade será salva (nesse caso)
print(galera)

# Para criar um laço que exiba os dados salvos em uma lista
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

# Para adicionar mais itens em outra lista manualmente
teste = list()
teste.append('Isaac')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Itzhak'
teste[1] = 23
galera.append(teste[:])
print(galera)

# Para exemplo de como criar um programa interativo com 2 listas ver aula18c
