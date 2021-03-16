name = str(input('Digite seu nome completo: ')).strip().title()
nome = name.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)]))

#Quando len(lista) ele conta a partir do 1 e não do 0, sendo assim -1 seleciona o ultimo item da lista
