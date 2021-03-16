contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num < 21:
            print(f'Você digitou o número {contagem[num]}.')
            break
    ask = ' '
    while ask not in 'SsNn':
        ask = str(input('Quer continuar? [S/ N]: ')).upper().strip()[0]
    if ask == 'N':
        break
