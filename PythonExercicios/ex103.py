def ficha(name, kills):
    dados = [name, kills]
    if dados[0] == '':
        dados[0] = 'desconhecido'
    if dados[1] == '':
        dados[1] = '0'
    return f'O jogador {dados[0]} fez {dados[1]} kill(s) no campeonato.'


nome = str(input('Nome do jogador: '))
kill = str(input('Quantos kills? '))
print(ficha(nome, kill))
