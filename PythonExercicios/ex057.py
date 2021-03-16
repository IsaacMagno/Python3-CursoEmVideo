ask = str(input('Qual o seu sexo? ')).upper().strip()
if ask == 'M':
    print('Você é do sexo\033[34m Masculino\033[m')
if ask == 'F':
    print('Você é do sexo\033[35m Feminino\033[m')
while ask != 'M' and ask != 'F':
    print('\033[31mVocê digitou um valor incorreto, tente novamente com\033[m\033[32m [M / F]:\033[m')
    ask = str(input('Qual o seu sexo?\nResposta: ')).upper().strip()
    if ask == 'M':
        print('Você é do sexo\033[34m Masculino\033[m')
    if ask == 'F':
        print('Você é do sexo\033[35m Feminino\033[m')

#metodo da aula

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
