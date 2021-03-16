media = 0
sexof = 0
sexom = 0
nomem = str('')
for stats in range(1, 5):
    print(stats, 'ª pessoa')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    media += idade / 4
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'F' and idade < 20:
        sexof += 1
    if sexo == 'M':
        if idade > sexom:
            sexom = idade
            nomem = nome
    print('-' * 20)
print('A idadade média do grupo é de {} anos.'.format(media))
print('O homem mais velho no grupo tem {} anos e se chama {}.'.format(sexom, nomem))
print('Entre eles existem {} mulheres com menos de 20 anos de idade.'.format(sexof))
