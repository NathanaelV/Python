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
print()

# Teacher example:
print('\nTeacher example:')
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[0]
    else:
        if listanum[c] < men:
            men = listanum[c]
        if listanum[c] > mai:
            mai = listanum[c]
print('-=' * 30)
print(f'Os valores gitados foram: {listanum}')
print(f'O maior valor foi {mai} e apareceu nas posições: ', end='')

for p, v in enumerate(listanum):
    if v == mai:
        print(f'{p}... ', end='')
print()
print(f'O menor valor foi {men} e apareceu nas posições: ', end='')
for p, v in enumerate(listanum):
    if v == men:
        print(f'{p}... ', end='')
print()
