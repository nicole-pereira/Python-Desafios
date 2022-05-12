def moeda(num=0, cifrao='R$'):
    res = f'{cifrao}{num:.2f}'.replace('.', ',')


def dobro(num=0, formato=False):
    res = num * 2
    if not formato:
        return res
    else:
        moeda(res)


def metade(num=0, formato=False):
    res = num / 2
    if not formato:
        return res
    else:
        moeda(res)


def aumentar(num=0, taxa=0, formato=False):
    res = num + (num * taxa / 100)
    if formato is False:
        return res
    else:
        moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa / 100)
    if formato is False:
        return res
    else:
        moeda(res)
