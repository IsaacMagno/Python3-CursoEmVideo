text = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase'.format(text.count('a')))
print('A primeira letra A apareceu na posição {}'.format(text.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(text.rfind('a')+1))

#igual ao metodo usado na aula, unica diferença que ele usou upper ao inves de lower