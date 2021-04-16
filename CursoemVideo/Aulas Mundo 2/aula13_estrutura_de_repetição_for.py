# Challenge 46 - 56

for a in range(0, 6):  # Repetirá 5 vezes. Conta o 1 mas não conta o 6
    print('Hello')     # Ele para no 6
    print(a)
print('Fim')

for a in range(6, 0, -1):  # Sem o -1 não funciona. O 3º diz a dinâmica
    print(a)
print('Fim 2')
for a in range(0, 6, 2):  # Vai contar de 2 em 2
    print(a)
print('Fim 3')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for a in range(i, f, p):
    print(a)
print('Fim')
print('\nRepetindo uma entrada de valores: ')
for a in range(1, 4):
    n = int(input('Digite um valor: '))
print('Fim')
print('\nSomando números')
s = 0
for c in range(1, 3):
    n = int(input('Digite um número'))
    s += n  # s = s + n
print('Fim')
