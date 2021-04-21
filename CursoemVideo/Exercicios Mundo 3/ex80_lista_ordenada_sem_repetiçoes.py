# Class Challenge 17

# Digirar 5 valores númericos
# Cadastrar em uma lista na posição correta. Sem usar o sort()
# A cada valor adicionado, mostrar em qual posição foi adicionado
# Ou está no primeiro ou último
# Mostrar a lista com os valores em ordem

order = list()
for v in range(1, 6):
    num = int(input(f'Enter {v}º number: '))
    # if v == 1:
    # print('First value added to the list.')
    order.append(num)
    for n in order:
        if num > n:
            order.append(num)
        if num < n:
            order.insert(0, num)
    print(order)

print(order)
