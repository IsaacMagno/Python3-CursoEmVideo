#O comando title deixa a primeira letra de cada palavra em maiusculo
name = str(input('Qual seu nome completo? ')).title().strip()
print('Seu nome tem Silva? {}'.format('Silva' in name))

#metodo da aula
nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
