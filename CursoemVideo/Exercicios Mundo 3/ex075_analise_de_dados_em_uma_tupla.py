# Class Challenge 16

# Ler 4 números pelo teclado:
# Colocar esses valores em um tupla e mostrar a tupla
# Quantas vezes o valor 9 aparece
# Qual a posição do valor 3
# Quais são os pares digitados
# Caso não tenha o número, falar que apareceu 0 vezes
# Ou que não encontrou em nenhuma posição.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
d = int(input('Enter fourth number: '))

num = (a, b, c, d)
print('-' * 30)
print(f'The enter numbers are: {num}')
print(f'The number 9 appears {num.count(9)} times.')
if 3 in num:
    print(f'The number 3 appears in position: {num.index(3)+1}')
else:
    print('No number 3 was entered.')
print('Even number(s) is(are): ', end='')
for c in range(0, 4):
    if num[c] % 2 == 0:
        print(num[c], end=' ')
print('\n', '-' * 30)

# Teacher Example:

print('\nTeacher Example:')

numero = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')), int(input('Digite o último número: ')), )
print(f'Você digitou os números: {numero}')
print(f'O valor nove apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição')
else:
    print('O valor 3 não aparece em nenhuma posição.')
print(f'Os valore pares foram: ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')