# Class Challenge 15

# Show a multiplication table, only stop when the user enters a negative number

while True:
    print('=' * 50)
    print('{:^50}'.format('MULTIPLICATION TABLE'))
    print('{:^50}'.format('Enter a negative number to EXIT!'))
    print('=' * 50)
    n = int(input('Enter a number to find your multiplication table: '))
    c = 1
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c:>2} = {n*c}')
        c += 1

# Teacher's Example:

print('\nTeacher Example: ')
while True:
    n = int(input('Quer ver a tabuada de Qual número? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c:>2} = {n*c}')
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADA. Volte Sempre')
