from datetime import date
i = 0
i2 = 0
atual = date.today().year
for data in range(1, 8):
    ano = int(input('Digite o ano em que ano a {}ª pessoa nasceu: '.format(data)))
    if atual - ano >= 21:
        i += 1
    else:
        i2 += 1
print('Ao todo tivemos {} pessoas que são maiores de idade.'.format(i))
print('E também tivemos {} pessoas que são menores de idade.'.format(i2))
