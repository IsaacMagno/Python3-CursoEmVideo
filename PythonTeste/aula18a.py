teste = list()
teste.append('Isaac')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Itzhak'
teste[1] = 23
galera.append(teste[:])
print(galera)
