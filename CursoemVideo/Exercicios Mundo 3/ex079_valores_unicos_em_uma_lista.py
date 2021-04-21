# Class Challenge 17

# Digitar vários valores númericos, perguntando se quer continuar
# Adicionar os números em uma lista. Não adicionar números repetidos
# Notificar se o valor foi adicionado ou não
# Exibir os valores em ordem crescente

group = list()
while True:
    print('-' * 30)
    num = int(input('Enter a numer: '))

    if num not in group:
        print('Number added to list...')
        group.append(num)
    else:
        print('This number has already been added to the list...')

    resp = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    while resp not in 'YN':
        print('\nInvalid response!')
        resp = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-'*30)
group.sort()
print(f'All values entered: {group}')
