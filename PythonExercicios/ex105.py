def notas(*num, opc=False):
    """
    --> Função para analisar notas e situações de varios alunos.
    :param num: Uma ou mais notas dos alunos. (aceita várias)
    :param opc: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionario com varias informações sobre a situação da turma.
    """
    dados = list(num)
    situ = ['Boa', 'Ruim', 'Razoável']
    dici = dict()
    dici['total'] = len(dados)
    dici['maior'] = max(dados)
    dici['menor'] = min(dados)
    dici['media'] = sum(dados) / len(dados)
    if opc:
        if dici['media'] >= 7:
            dici['situaçao'] = situ[0]
        elif 5 <= dici['media'] < 7:
            dici['situaçao'] = situ[2]
        else:
            dici['situaçao'] = situ[1]
    return dici


result = notas(2, 7, 3, 8, 6, opc=True)
print(result)
help(notas)
