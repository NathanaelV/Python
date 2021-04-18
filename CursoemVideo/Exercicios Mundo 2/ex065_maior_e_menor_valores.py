# Class Challenge 14

# Ler vários números inteiros. Mostar no final o maior, menor e a média.
# Perguntar se quer continuar S/N digitando valores.

r = 'S'
s = c = bigger = smaller = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja digitar mais um número [S/N]: ')).strip().upper()
    if c == 0:
        bigger = n
        smaller = n
    else:
        if bigger < n:
            bigger = n
        if smaller > n:
            less = n
    s += n
    c += 1
print('A soma dos {} números digitados é {}.'.format(c, s))
print('E a média é {:.2f}'.format(s/c))
print('O maior é {} e o menor é {}'.format(bigger, smaller))
print('Fim!')
