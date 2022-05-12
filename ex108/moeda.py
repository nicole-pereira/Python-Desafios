def dobro(num=0):
    res = num*2
    return res


def metade(num=0):
    res = num/2
    return res


def aumentar(num=0, taxa=0):
    res = num + (num * taxa/100)
    return res


def diminuir(num=0, taxa=0):
    res = num - (num * taxa/100)
    return res


def formato(num=0, cifrao='R$'):
    res = f'{cifrao}{num:.2f}'.replace('.', ',')
    return res
