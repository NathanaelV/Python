# Challenge 57 - 65

# While é usado quando eu não sei o limite.
# Estrutura de repetição com teste lógico.
# Quando eu sei o limite, é mais prático usar o for

print('Usando o For:.')
for c in range(1, 10):
    print(c, end=',')
print('Fim!')

print('\nUsando o While:')
c = 1
while c < 10:
    print(c, end=',')
    c += 1
print('Fim!\n')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!\n')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!\n')

# Ler uma quantidade de valores e diferênciar se são pares ou impares

par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números ímpares e {} números pares.'.format(impar, par))
print('Acabou!\n')
