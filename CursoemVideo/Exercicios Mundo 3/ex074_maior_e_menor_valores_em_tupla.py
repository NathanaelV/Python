# Class Challenge 16

# Gerar 5 números aleatórios e colocar em uma tupla
# Mostrar a lista dos 5 números
# Mostrar o maior e o menor da Tupla

from random import randint
while True:
    num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
    print(num)
    order = sorted(num)
    print(f'The largest number is {order[len(order)-1]}')
    print(f'The smallest number is {order[0]}')
    user = str(input('Do you want to draw another number? [Y/N] ')).strip().upper()[0]
    while user not in 'YN':
        print('Invalid! Please enter a Valid option.')
        user = str(input('Do you want to draw another number? [Y/N]')).strip().upper()[0]
    if user == 'N':
        break

# Teacher Example:

print('\nTeacher example:')
print(f'The numbers draw was:', end=' ')
for n in num:
    print(f' {n}', end=' ')
print(f'\nThe largest number is: {max(num)}')
print(f'The smallest number is: {min(num)}')
