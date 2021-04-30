def aumentar(num, increase=0):
    n = num + num * (increase / 100)
    return n


def diminuir(num, displacement=0):
    n = num - num * (displacement / 100)
    return n


def dobrar(num):
    n = num * 2
    return n


def metade(num):
    n = num / 2
    return n
