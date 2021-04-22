# Class Challenge 17

# Digirar 5 valores númericos
# Cadastrar em uma lista na posição correta. Sem usar o sort()
# A cada valor adicionado, mostrar em qual posição foi adicionado
# Ou está no primeiro ou último
# Mostrar a lista com os valores em ordem

order = list()
for v in range(1, 9):
    num = int(input(f'Enter {v}º number: '))
    if v == 1:
        z = 0
    for pos, a in enumerate(order):
        print(f'Posição: {pos}, Iten: {a}')
        if a < num:
            print('Item < NUM: Z = pos')
            z = pos
        else:
            print('ELSE: Item > NUM: Z = len')
            z = len(order)
    print(f'Z: {z}')
    order.insert(z, num)
    print(order)

print(order)
