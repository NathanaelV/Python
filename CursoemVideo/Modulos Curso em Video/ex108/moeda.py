# Class Challenge 22

def aumentar(num, increase=0):
    n = num + num * (increase / 100)
    return n


def diminuir(num, reduction=0):
    n = num - num * (reduction / 100)
    return n


def dobrar(num):
    n = num * 2
    return n


def metade(num):
    n = num / 2
    return n


def moeda(num, moeda='R$ '):
    n = f'{moeda}{num:.2f}'.replace('.', ',')
    return n
