# Class Challenge 14

# Ler um número da tela e mostrar o fatorial desse número
# 5! = 5x4x3x2x1 = 120. Fazer usando o while e for

# Usando a biblioteca Math:

from math import factorial
print('Usando Math')
n = int(input('Digite o número: '))
nf = factorial(n)
print('{}! = {}'.format(n, nf))


# Usando While:
print('\nUsando o While: ')
n = int(input('Digite o número: '))
nf = n
f = 1
while f != n:
    nf *= f
    f += 1
print('{}! = {}'.format(n, nf))

# Usando o for:

print('\nUsando o For')
nfor = int(input('Digite um número: '))
nfor2 = nfor
for c in range(1, nfor):
    nfor2 *= c
print('{}! = {}'.format(nfor, nfor2))
