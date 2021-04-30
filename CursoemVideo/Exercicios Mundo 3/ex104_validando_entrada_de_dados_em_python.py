# Class Challenge 21

# função leiaint(): funiona como um input() do Python
# Só deve aceitar valores númericos
# Ex.: n = leiaint('Digite um n')
# Erro em vermelho
# Adicionar as docstrings da função

def leiaint(txt):
    """
    -> Function to valid a inter number. While the user doesn't enter an integer number the function will continue in a
    loop asking for an integer.
    :param txt: Message for the user to type an integer number.
    :return: return variable X as an integer type
    """
    while True:
        x = str(input(txt)).strip()
        if x.isnumeric():
            x = int(x)
            return x
        else:
            print('\033[1;31mERROR!!! Enter a Inter number.\033[m')


# Programa Principal:
n = leiaint('Enter a number: ')
print(f'You enter number {n}')


# Teacher Example:


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[31m')
        if ok:
            break
    return valor


# Principal program
n = leiaInt('Digite um numero: ')
print(f'Você digitou o número {n}.')
