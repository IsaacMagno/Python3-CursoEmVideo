dados = dict()
kill = list()
killa = list()
jogador = list()
tot = 0
while True:
    dados['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for p in range(0, partidas):
        ks = int(input(f'Quantos kills na partida {p}: '))
        kill.append(ks)
        tot += ks
    dados['kills'] = kill[:]
    dados['total'] = tot
    jogador.append(dados.copy())
    killa.append(kill[:])
    dados.clear()
    kill.clear()
    tot = 0
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if ask == 'N':
        break
    print()
print()
print(f'{"cod":<5} {"NOME":<5} {"KILLS":>10} {"TOTAL":>10}')
for c, j in enumerate(jogador):
    print(f'{c:<5} {jogador[c]["nome"]:<5} {"":>5}{jogador[c]["kills"]}{jogador[c]["total"]:>10}')
print()
while True:
    ask2 = int(input('Mostrar dados de qual jogador? : '))
    print()
    if ask2 == 999:
        break
    if ask2 <= len(jogador) - 1:
        print(f'Levantamento do jogador {jogador[ask2]["nome"]}')
        for p, c in enumerate(killa[ask2]):
            print(f'Na partida {p+1} fez {c} kills')
    else:
        print(f'Não existe jogar com código {ask2}. Tente novamente.')
    print()
