alunos = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[1] + dados[2]) / 2
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if ask == 'N':
        break
print('-' * 20)
print(f'N° Nome       Média')
print('-' * 20)
for c, v in enumerate(alunos):
    print(f'{c}  {alunos[c][0]:<10} {alunos[c][3]:>5.1f}')
print('-' * 20)
while True:
    print()
    ask = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    if ask == 999:
        break
    elif ask >= len(alunos):
        print('Excedeu o número de alunos, tente novamente.')
    else:
        print(f'\nAs notas de {alunos[ask][0]} são: [{alunos[ask][1]}, {alunos[ask][2]}]')
