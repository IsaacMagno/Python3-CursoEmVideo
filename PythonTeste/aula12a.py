nome = str(input('Qual é seu nome? '))
if nome == 'Isaac':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'João':   #Estrutura condicional aninhada
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')

print('Tenha um bom dia {}'.format(nome))