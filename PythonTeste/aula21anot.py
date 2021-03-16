# Funçoes

# Interactive help
# funçao que explica e ajuda como utilizar funcionalidades no python
# Comandos para chamar a função:
help(print)               #Exemplos
print(input.__doc__)


# Docstrings
# Uma string de documentaçao sobre uma funcionalidade
# Exemplo

def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem                       # Docstring
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')


contador(2, 10, 2)
help(contador)                  # --> Chama a docstring da funçao

# Parametros opcionais
# Exemplos


def somar(a=0, b=0, c=0):   # a/b/c=0 tornou os paramentros opcionais
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()  # com os paramentros opcionais setados, até mesmo um chamada sem valores funciona, tornando todos os valores 0

# Escopo de variaveis
# É o local onde a variavel vai existir e o local onde a variavel não vai existir


def teste():
    global n                                    # Com esse comando ele não cria um escopo local e utiliza o global
    n = 10                                      # Esse n se torna um escopo local e nao afeta o N do escopo global
    x = 8
    print(f'Na função teste, n vale {n}')       # x = faz parte de um escopo local, funcionando apenas dentro da
    print(f'Na função teste, x vale {x}')       # funçao que ele foi chamado


# Programa principal
n = 2                                       # n = faz parte de um escopo global //      Com o comando global ele perde
print(f'No programa principal n vale {n}')  # o valor de fora (escopo global) e utiliza o valor de dentro (escopo local)
teste()
# print(f'No programa principal, x vale {x}')   #Remover # para ver o erro
print()


# Retorno de valores
# Com o comando return a função retorna o resultado para o qual ela foi programada
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus calculos foram {r1} {r2} {r3}')

# Validação de dados
# Exemplo

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

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
