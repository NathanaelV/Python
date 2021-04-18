# Class Challenge 14

# Ler dois valores e mostrar um menu na tela:
# 1 - Somar, 2 - Multiplicar, 3 - Maior, 4 - Novos Números, 5 - Sair do programa
from time import sleep
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
m = 0
while m != 5:
    print('''\nMenu de Opções: 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    m = int(input('Opção: '))
    if m == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
        sleep(0.5)
    if m == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
        sleep(0.5)
    if m == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
            sleep(0.5)
        elif n2 > n1:
            print('{} < {}'.format(n1, n2))
            sleep(0.5)
        else:
            print('{} = {}'.format(n1, n2))
            sleep(0.5)
    if m == 4:
        n1 = float(input('Digite o 1º número: '))
        n2 = float(input('Digite o 2º número: '))
