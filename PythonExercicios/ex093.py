jogador = dict()
kill = list()
tot = 0
jogador['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, partidas):
    ks = int(input(f'Quantos kills na partida {p}: '))
    kill.append(ks)
    tot += ks
jogador['kills'] = kill[:]
jogador['total'] = tot
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, c in enumerate(kill):
    print(f' => Na partida {p+1}, fez {c} kills.')
print(f'Foi um total de {tot} Kills!')
if tot > 10:
    print('Ele é demais!!')
else:
    print('Menino novo...')
