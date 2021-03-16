def leiaDinheiro(txt):
    ok = False
    while not ok:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido! \033[m')
        else:
            ok = True
            return float(entrada)


def leiaInt(txt):
    ok = False
    num = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return num
