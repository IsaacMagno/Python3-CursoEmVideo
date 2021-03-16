print('\033[31mOlá mundo')
print('\033[1;31;43mOlá mundo\033[m')
print('\033[4;30;45mOlá mundo\033[m')
print('\033[30mOlá mundo\033[m')
print('\033[37Olá mundo\033[m')
print('\033[7;30mOlá mundo\033[m')
print('\033[0;33;44mOlá mundo\033[m')
print('\033[7;33;44mOlá mundo\033[m')

a = 3
b = 5
print('Os valores são \033[33;40m{}\033[m e \033[33;40m{}\033[m!!!'.format(a,b))

nome = 'Isaac'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá muito prazer em te conhecer, {}{}{} !!!'.format(cores['pretoebranco'], nome, cores['limpa']))
