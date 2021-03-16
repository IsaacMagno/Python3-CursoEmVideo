n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('Você tirou {} e {} sua média é {}'.format(n1, n2, media))
if media < 5:
    print('Você foi REPROVADO.')
elif media >= 7:
    print('Você foi APROVADO!')
elif media > 5 and media <= 6.9:
    print('Você está de RECUPERAÇÃO.')
