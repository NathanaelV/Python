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
print('\nFatorial Usando o While: ')
n = int(input('Digite o número: '))
nf = n
f = 1
while f != n:
    nf *= f
    f += 1
print('{}! = {}'.format(n, nf))

# Usando o for:

print('\nFatoria Usando o For')
nfor = n
for c in range(1, n):
    nfor *= c
print('{}! = {}'.format(n, nfor))

# Exemplo do professor:

print('\nExemplo do Professor: ')
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
