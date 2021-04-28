# Class Challenge 21

# função leiaint(): funiona como um input() do Python
# Só deve aceitar valores númericos
# Ex.: n = leiaint('Digite um n')
# Erro em vermelho
# Adicionar as docstrings da função

def leiaint(txt):
    while True:
        a = input(txt)
        a = int(a)
        if type(a) == int:
            break
        else:
            print('ERROR!!! Enter a Inter number.')
    print(a)


# Programa Principal:
leiaint('Enter a number: ')
