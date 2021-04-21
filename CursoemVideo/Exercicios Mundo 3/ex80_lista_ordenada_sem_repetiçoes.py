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
        print('First value added to the list.')
        order.append(num)
    else:
        '''
                if num >= max(order):
            print('Number added at the end of the list')
            order.append(num)
        elif num <= min(order):
            order.insert(0, num)
        else: 
        '''
        for p, a in enumerate(order):
            if a > num:
                print(f'P: {p} e A: {a}')

            else:
                print(f'Else P: {p} e A: {a}')
        order.append(num)
    print(order)

print(order)
