from datetime import date
ano = date.today().year
sexom = sexof = d1 = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        d1 += 1
    while True:
        sexo = str(input('Sexo [M/F] :')).upper().strip()[0]
        if sexo == 'M':
            sexom += 1
            break
        if sexo == 'F':
            dz = idade
            if dz < 20:
                sexof += 1
            break
        else:
            sexo = str(input('Sexo [M/F] :')).upper().strip()[0]
            if sexo == 'M':
                sexom += 1
                break
            if sexo == 'F':
                dz = idade
                if dz < 20:
                    sexof += 1
                break
    while True:
        ask = str(input('Quer continuar? [S/N] : ')).upper().strip()[0]
        if ask == 'N':
            break
        if ask == 'S':
            break
        else:
            ask = str(input('Quer continuar? [S/N] : ')).upper().strip()[0]
            if ask == 'N':
                break
            if ask == 'S':
                break
    if ask == 'N':
        break
print(f'Total de pessoas com mais de 18 anos foi {d1}.')
print(f'Ao todo temos {sexom} homens cadastrados.')
print(f'E temos {sexof} mulher com menos de 20 anos.')
