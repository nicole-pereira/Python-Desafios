
def contador(i, f, p):
    # docstring
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


# interactive help
help(contador)


def somar(a=0, b=0, c=0):
    # parametros opcionais
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 5)


def somar(a=0, b=0, c=0):
    # return
    s = a + b + c
    return s


r1 = somar(3, 5, 6)
r2 = somar(6, 2)
r3 = somar(9)

print(f'Os resultados foram {r1}, {r2} e {r3}')
