# Class Challenge 20

# função área()
# Recebe largura e comprimento de um retângulo
# Mostra a área do retângulo


def área(a, b):
    c = a * b
    print(f'A área do retângulo de lado {a} x {b} é de {c}m²')


def tit(msg):
    t = len(msg) + 6
    print('-' * (len(msg) + 6))
    print(f'   {msg.upper()}')
    print('-' * (len(msg) + 6))


tit('Calculando área')
a = float(input('Largura: (m) '))
b = float(input('Comprimento: (m) '))
área(a, b)
