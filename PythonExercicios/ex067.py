from time import sleep
mult = 1
vezes = 0
while True:
    mult = 1
    tab = int(input('Digite um número para gerar a tabúada [Negativo p/ parar]: '))
    if tab < 0:
        break
    while True:
        vezes = tab * mult
        print(f'{tab} * {mult:2} = {vezes}')
        mult += 1
        if mult == 11:
            break
print('Programa tábuada encerrando...')
sleep(1.5)
print('Volte sempre!')
