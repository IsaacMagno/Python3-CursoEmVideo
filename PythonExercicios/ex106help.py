from time import sleep
c = ['\033[m', '\033[1;30;47m', '\033[1;30;42m', '\033[1;7;40m']


def mensagem(txt, cor=0):
    print(c[cor], end='')
    print(txt)
    print(c[0], end='')


def ajuda(msg):
    ask = resp
    mensagem('Acessando manual de comando', 2)
    sleep(1)
    print(c[3], end='')
    help(ask)
    print(c[0], end='')


mensagem('sistema de ajuda Pyhelp', 1)
resp = ''
while True:
    mensagem('Função ou biblioteca', 1)
    resp = str(input('            '))
    if resp.upper() == "FIM":
        break
    else:
        ajuda(resp)
mensagem('Finalizando...', 1)
sleep(1)
