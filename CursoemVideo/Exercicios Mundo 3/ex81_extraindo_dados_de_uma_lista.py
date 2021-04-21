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
