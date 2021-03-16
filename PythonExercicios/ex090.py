aluno = {}

for c in range(0, 1):
    aluno['nome'] = str(input('Nome: ')).title()
    aluno['media'] = float(input('Media: '))
    if aluno['media'] >= 7:
        aluno['situaçao'] = 'Aprovado'
    else:
        aluno['situaçao'] = 'Reprovado'
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
print(f'A situação é igual a {aluno["situaçao"]}')
