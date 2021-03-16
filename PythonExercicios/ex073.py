times = ('DAMWON Gaming', 'Top Esports', 'DRX', 'Suning Gaming', 'AGO ROGUE', 'JD Gaming', 'mousesports',
         'FunPlus Phoenix', 'Invictus Gaming', 'K1ck Neosurf', 'Vodafone Giants', 'Nongshim Redforce', 'Edward Gaming',
         'Team WE', 'FC Schalke 04 Evolution', '9z Team', 'Team Aze', 'Origen SB', 'Afreeca Freecs', 'Nocturns Gaming')

print(f'Top 20 times de LoL Mundial: {times}')
print(f'Os cinco primeiros são: {times[0:5]}')
print(f'Os quatro ultimos são: {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print('FunPlus Phoenix está na {}ª posição.'.format(times.index('FunPlus Phoenix')+1))
