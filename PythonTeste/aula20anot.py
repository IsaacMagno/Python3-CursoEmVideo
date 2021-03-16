# Funções
# Para criar uma função def nomeDaFunçao(parametro):
# Para desempacotar uma função

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os {valores} temos a {s}')


soma(3, 2, 5, 21)
soma(9, 3)

# Desempacotar utilizando uma lista

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 3, 4, 5, 6, 7]
dobra(valores)
print(valores)

# Outro exemplo de como desempacotar uma função

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Exemplo de como utilizar a função para somas

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(b=12, a=3)
soma(9, 3)
