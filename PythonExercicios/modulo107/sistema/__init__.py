lista = list()
dicio = dict()
arquivo = open('pessoas.txt', 'a')


def menu():
    print('-' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('-' * 40)
    print('''         
1 - VER PESSOAS CADASTRADAS
2 - CADASTRAR NOVA PESSOA
3 - SAIR DO SISTEMA''')
    print()
    print('-' * 40)
    resp()


def resp():
    global arquivo
    global ask
    while True:
        try:
            ask = int(input('Digite uma opção: '))
            if ask > 3 or ask < 1:
                print('Opção invalida, tenta novamente!')
            else:
                break
        except:
            print('Erro! Você digitou uma opção invalida tente novamente!')
    if ask == 1:
        print('-' * 40)
        print('PESSOAS CADASTRADAS'.center(35))
        print('-' * 40)
        arquivo = open('pessoas.txt', 'r')
        for linha in arquivo:
            linha = linha.rstrip()
            print(linha)
        arquivo.close()
        return menu()
    if ask == 2:
        print('-' * 40)
        print('NOVO CADASTRO'.center(40))
        listaCadastro()
    if ask == 3:
        print('-' * 40)
        print('Saindo do sistema... Até logo!')
        exit()


def listaCadastro():
    global arquivo
    arquivo = open('pessoas.txt', 'a')
    ok = False
    ok1 = False
    while True:
        try:
            nome = str(input('Nome: '))
            ok = True
        except:
            print('Erro! Digite um nome valido!')
        if ok:
            break
    while True:
        try:
            idade = int(input('Idade: '))
            idade = str(idade)
            ok1 = True
        except:
            print('Erro! Digite uma idade valida!')
        if ok1:
            break
    dicio['nome'] = nome
    dicio['idade'] = idade
    lista.append(dicio.copy())
    arquivo.writelines(f'{lista[0]["nome"]:<30} {lista[0]["idade"]:>10} anos\n')
    arquivo.close()
    lista.clear()
    dicio.clear()
    print(f'Novo registro de {nome} adicionado.')
    return menu()
