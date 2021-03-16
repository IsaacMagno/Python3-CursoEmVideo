def leiaInt(txt):
    ok = False
    num = 0
    while True:
        try:
            num = int(input(txt))
            ok = True
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar esse número.')
            num = 0
            ok = True
        except:
            print('ERRO! Digite um número inteiro válido!')
        if ok:
            break
    return num


def leiaFloat(txt):
    ok = False
    num = 0
    while True:
        try:
            num = float(input(txt))
            ok = True
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar esse número.')
            num = 0
            ok = True
        except:
            print('ERRO! Digite um número real válido!')
        if ok:
            break
    return num




n = leiaInt('Digite um número inteiro: ')
n1 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n} e o real {n1}')
