"""Exercício Python 105:
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
1. Quantidade de notas
2. A maior nota
3. A menor nota
4. A média da turma
5. A situação (opcional)
"""
"""    soma = 0

    for n in nota:
        soma += n"""


def notas(*nota, situ=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param situ: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionários com várias informações sobre a situação da turma.
    """
    dados = {'total': len(nota),
             'maior': max(nota),
             'menor': min(nota),
             'media': sum(nota) / len(nota)}

    if situ:
        if dados['media'] >= 7:
            situ = 'BOM'
        elif dados['media'] < 7:
            situ = 'RUIM'
        elif dados['media'] >= 8:
            situ = 'EXCELENTE'
        dados['situação'] = situ

    return dados


# Programa Principal
resp = notas(9, 8.5, 7, 3.5, 4, 2, 10)
print(resp)
