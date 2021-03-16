def calculadoraAdicaoSubtracao(numero, outroNumero, operacao):
    soma = numero + outroNumero
    sub = numero - outroNumero
    op = 'operação inválida'
    if operacao == '+':
        return soma
    elif operacao == '-':
        return sub
    else:
        return op
