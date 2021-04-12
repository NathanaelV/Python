
# Class challenge 007
# Mostrar o antecessor e o sucessor de um numero inteiro

n = int(input('\nDigite Um numero inteiro: '))
a = n - 1
s = n + 1
print('O antecessor do numero {} é {}.'.format(n, a), end=' ')
print('E o sucessor é {}'.format(s))

# Exemplo do professor

n = int(input('Digite um número: '))
print('O antecessor de {} é {} e o sucessor é {}.'.format(n, n-1, n+1))