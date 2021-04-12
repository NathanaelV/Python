# Class Challenge 09

# Ler um numero entre 0 e 9999 e mostrar os números separadamente
# Unidade, Dezena, Centena, Milhar
# Fazer usando String e Matematicamente

# Matematicamente

n = input('Digite um número entre 0 e 9999: ')
num = int(n)
M = num // 1000
C = (num - M*1000) // 100
D = (num - M*1000 - C*100) // 10
U = (num - M*1000 - C*100 - D*10)
print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(M, C, D, U))

# Por Manipulação de Texto
ns = ('{:0>4}'.format(n))  # Essencial para usar como uma String
print('\nMilhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(ns[0], ns[1], ns[2], ns[3]))

# Exemplo do professor:

# No modo de String, a resolução foi a mesma.
print('\nExemplo do Professor:')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o número {}\n'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
