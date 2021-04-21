# Class Challenge 17

# Ler vaios números
# Ter duas listas extras, só com pares e ímpares
# Mostrar as 3 listas
# Dica: Primeiro le os valores, depois monta as outras duas listas

big = list()
par = list()
impar = list()

while True:
    big.append(int(input('Enter a number: ')))
    resp = ' '
    while resp not in 'YN':
        resp = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'All numbers entered have been: {big}')
for a in big:
    if a % 2 == 0:
        if a not in par:
            par.append(a)
    if a % 2 == 1:
        if a not in impar:
            impar.append(a)
print(f'All the even numbers that appear are: {par}')
print(f'All the odd numbers that appear are: {impar}')
