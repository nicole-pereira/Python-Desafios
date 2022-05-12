def dobro(num=0, formato=False):
    res = num * 2
    return res if not formato else moeda(res)


def metade(num=0, formato=False):
    res = num / 2
    return res if not formato else moeda(res)


def aumentar(num=0, taxa=0, formato=False):
    res = num + (num * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(num=0, cifrao='R$'):
    return f'{cifrao}{num:.2f}'.replace('.', ',')


def resumo(num=0, aumento=10, diminuicao=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t\t{moeda(num)}')
    print(f'Dobro do preço: \t\t{dobro(num, True)}')
    print(f'Metade do preço: \t\t{metade(num, True)}')
    print(f'Com {aumento}% do aumento: \t{aumentar(num, aumento, True)}')
    print(f'Com {diminuicao}% de redução: \t{diminuir(num, diminuicao, True)}')
