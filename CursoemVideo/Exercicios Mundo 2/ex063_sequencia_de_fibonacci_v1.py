# Class Challenge 14

# Ler um número n e mostrar os n primeiros números de Fibonacci
# 0, 1, 1, 2, 3, 5, 8...

n = int(input('Digite enéssimo número que deseja saber da sequencia de Fibonacci: '))
a1 = 0
a2 = 1
a3 = 0
i = 0
while i < n:
    print(a3, end=', ')
    a3 = a1 + a2
    a2 = a1
    a1 = a3
    i += 1
print('Fim!')

# Exemplo do professor:

print('\nExemplo do professor:')
print('-' * 30)
print('SEQUENCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')
print('~~' * 30)
