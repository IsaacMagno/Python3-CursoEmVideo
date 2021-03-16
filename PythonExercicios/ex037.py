numero = int(input('Digite um numero: '))
print('''Pressione:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
chose = int(input('Sua opção: '))

if chose == 1:
    print('{} em BINARIO é igual a {}'.format(numero, bin(numero)[2:]))
elif chose == 2:
    print('{} em OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif chose == 3:
    print('{} em HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida, tente novamente')
