# Class Challenge 20

# função área()
# Recebe largura e comprimento de um retângulo
# Mostra a área do retângulo


def área(larg, comp):
    a = larg * comp
    print(f'A área do retângulo de lado {larg} x {comp} é de {a}m²')


def tit(msg):

    print('-' * (len(msg) + 6))
    print(f'   {msg.upper()}')
    print('-' * (len(msg) + 6))


# Programa principal:
tit('Calculando área')
n1 = float(input('Largura: (m) '))
n2 = float(input('Comprimento: (m) '))
área(n1, n2)

# Teacher Example:

# Teacher example is similar.
