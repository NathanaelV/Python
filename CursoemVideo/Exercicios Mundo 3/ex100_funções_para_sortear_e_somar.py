# Class Challenge 20

# lista com números.
# Criar uma função sorteia. Sorteia 5 números e coloca na lista
# Criar uma função somaPar(). pega a funão anterior e soma só os pares

from random import randint
from time import sleep


def sorteia(lst):
    print('Os números sorteados são: ', end='')
    for c in range(0, 5):
        sort = randint(0, 9)
        print(sort, end=' ')
        sleep(0.3)
        lst.append(sort)
    print('PRONTO!')


def somapar(lst):
    print(f'Os pares são (', end=' ')
    s = 0
    for a, n in enumerate(lst):
        if n % 2 == 0:
            print(n, end=' ')
            s += n
    print(f'). A soma dos pares é {s}.')


num = list()
sorteia(num)
somapar(num)
