# Class Challenge 22

def aumentar(num, increase=0, form=False):
    n = num + num * (increase / 100)
    if form:
        n = moeda(n)
    return n


def diminuir(num, reduction=0, form=False):
    n = num - num * (reduction / 100)
    return n if form is False else moeda(n)


def dobrar(num, form=False):
    n = num * 2
    return n if not form else moeda(n)


def metade(num, form=False):
    n = num / 2
    return n if form is False else moeda(n)


def moeda(num):
    n = f'R$ {num:.2f}'.replace('.', ',')
    return n


def resumo(n, a=0, d=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado:":<21}{moeda(n)}')
    print(f'{"Dobro do Preço:":<21}{dobrar(n, True)}')
    print(f'{"Metade do Preço:":<21}{metade(n, True)}')
    print(f'{a:<3}{"% de aumento:"}\t{aumentar(n, a, True)}')
    print(f'{d:<3}{"% de redução:"}\t{diminuir(n, d, True)}')
    print('-' * 30)
