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
