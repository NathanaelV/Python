# Class Challenge 17

# Ler 5 valores númericos e Guardar em uma lista.
# Mostrar qual o maior e qual o menor
# Mostrar a posição do maior e do menor
# Se aparecer mais de uma vez, deve mostrar todas as posições

position = ('first', 'second', 'third', 'fourth', 'fifth')
val = list()
for c in range(0, 5):
    val.append(int(input(f'Enter {position[c]} number: ')))

print(f'The largest is {max(val)} and appears in the position: ', end='')
for pmax, vmax in enumerate(val):
    if vmax == max(val):
        print(pmax+1, end='...')

print(f'\nThe smallest is {min(val)} and appears in the position: ', end='')
for pmin, vmin in enumerate(val):
    if vmin == min(val):
        print(pmin+1, end='...')
