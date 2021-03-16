soma = cont = 0
while True:
    n = int(input('Digite os números que deseja somar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma total dos {cont} números digita é {soma}.')
