# Class Challenge 21

# Criar a Função fatorial que recebe dois parametros:
# O número que será calculado
# Se quer ver o processo do cálculo ou só o resultado (valor lógico opcional)
#    Só mostrar se pedir
# fatorial(5, show=True)

# help(fatorial):
#    -> Calcula o fatorial de um número.
#    :param n: O número a ser calculado.
#    :param show: (opcional) Mostrar ou não a conta
#    :return: O valor de Fatorial de um número n.

def fatorial(n, show=False):
    """
    -> Function to calculate the factorila of a number
    :param n: The number to be calculated.
    :param show: (optional) Show or not calculate
    :return: The factorial value of a number n.
    """
    f = n
    print(f'{n}! = ', end='')
    if show:
        for c in range(1, n):
            f *= c
            print(f'{c} x', end=' ')
        print(n, end=' = ')
    else:
        for c in range(1, n):
            f *= c
    return f


print('~' * 30)
print(f'{"FACTORIAL":^30}')
print('~' * 30)

fat = int(input('Which number do you want to calculate the factorial of? '))
mos = input('Do you want to see the count? [S/N] ')  # .strip().upper()[0]

if mos in 'Ss':
    s = True
else:
    s = False

resp = fatorial(fat, s)
print(f'{resp}')

help(fatorial)


# Teacher Example:


def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Principal program:
print(fatorial(5, show=True))
