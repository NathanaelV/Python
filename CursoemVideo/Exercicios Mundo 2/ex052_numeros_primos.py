# Class Challenge 13

# Ler números inteiros e ver se é primo ou não
# Se é divisível somente por 1 e por ele mesmo

n = int(input('Digite um número: '))
s = 0
for a in range(1, n+1):
    if n % a == 0:
        s += a
if s == n+1:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
