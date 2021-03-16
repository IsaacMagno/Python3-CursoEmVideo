num = int(input('Digite um numero: '))
count = num
fat = 1
print('Calculando {}!: '.format(num), end='')
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fat *= count
    count -= 1
print('{}'.format(fat))
