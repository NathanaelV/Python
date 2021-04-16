# Class Challenge 13

# Ler números inteiros e ver se é primo ou não
# Se é divisível somente por 1 e por ele mesmo

n = int(input('Digite um número: '))
s = 0
for a in range(1, n+1):
    if n % a == 0:
        s += a
if s == n+1:
    print('O número {} é PRIMO.'.format(n))
else:
    print('O número {} NÃO é PRIMO.'.format(n))

# Exemplo do professor:
print('\nExemplo do professor: ')
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi dividido {} vezes.'.format(n, tot))
if tot == 2:
    print('Por isso ele É PRIMO.')
else:
    print('Por isso ele NÃO é PRIMO')
