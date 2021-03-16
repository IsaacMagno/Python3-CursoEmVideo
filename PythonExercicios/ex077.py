palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro', 'exercicios', 'importante')
count2 = A = E = I = O = U = 0
for c in palavras:
    if palavras[count2].count('a') > 0:
        A = palavras[count2].count('a')
    if palavras[count2].count('e') > 0:
        E = palavras[count2].count('e')
    if palavras[count2].count('i') > 0:
        I = palavras[count2].count('i')
    if palavras[count2].count('o') > 0:
        O = palavras[count2].count('o')
    if palavras[count2].count('u') > 0:
        U = palavras[count2].count('u')
    print(f'\nNa palavra {c} temos:', end='  ')
    for c1 in range(0, A):
        print('A', end=' ')
    for c1 in range(0, E):
        print('E', end=' ')
    for c1 in range(0, I):
        print('I', end=' ')
    for c1 in range(0, O):
        print('O', end=' ')
    for c1 in range(0, U):
        print('U', end=' ')
    count2 += 1
    A = E = I = O = U = 0
