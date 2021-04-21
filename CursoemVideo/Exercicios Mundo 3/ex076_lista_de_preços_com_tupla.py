# Class Challenge 16

# Criar uma tupla com nome e preço dos produtos
# Mostrar os dados de forma tabular.
# Tudo em uma única tupla

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Caneta', 22.3, 'Livro', 34.9)
print('_' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('_' * 40)

for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f'R$ {listagem[c]:>6.2f}')
print('_' * 40)

# Using another for:
print('\nUsing another For:')
i = 0
for compra in listagem:
    if i % 2 == 0:
        print(f'{compra:.<30}', end='')
    else:
        print(f'R$ {compra:>6.2f}')
    i += 1
