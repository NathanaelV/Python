# Class Challenge 17

# Ler varios números
# Mostrar quantos valores foram digitados
# Mostrar a Lista de valores em ordem decrescente
# Se o cinco foi digitado ou não e em qual posição.

value = list()
i = 0
while True:
    value.append(int(input('Enter a number: ')))
    i += 1
    resp = ' '
    while resp not in 'yn':
        resp = str(input('Do you want to continue? [Y/N] ')).strip().lower()[0]

    if resp == 'n':
        print('-' * 30)
        break

print(f'{i} values were entered.')
if 5 in value:
    print(f'The number 5 appeared in the positions: ', end='')
    for pos, v in enumerate(value):
        if v == 5:
            print(pos+1, end=', ')
else:
    print('There is no number 5 in the list.', end='')
value.sort(reverse=True)
print(f'\nIn ascending order: {value}')

# Teacher Example:

print('\nTeacher example:')
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
