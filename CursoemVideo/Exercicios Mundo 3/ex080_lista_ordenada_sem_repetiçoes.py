# Class Challenge 17

# Digirar 5 valores númericos
# Cadastrar em uma lista na posição correta. Sem usar o sort()
# A cada valor adicionado, mostrar em qual posição foi adicionado
# Ou está no primeiro ou último
# Mostrar a lista com os valores em ordem

order = list()
for v in range(1, 6):
    num = int(input(f'Enter {v}º number: '))
    if v == 1:
        print('Number added at the end of the list...')
        order.append(num)
    else:
        for pos, a in enumerate(order):
            if a > num:
                print(f'Number added in position {pos}...')
                order.insert(pos, num)
                break
            if num > max(order):
                print(f'Number added in the end of list...')
                order.append(num)
                break

print(f'All number entered in order are: {order}')

# Teacher Example:

print('\nTeacher Example:')
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'O valores digitados em ordem foram {lista}')
