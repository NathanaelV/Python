# Class Challenge 13

# Soma de todos os números ímpares, multiplos de 3 entre 1 e 500
# Fazer também um exemplo usando if else
s = 0
for a in range(0, 501):
    if a % 2 == 1 and a % 3 == 0:
        s += a
print('Soma =', s)
print('Fim')

# Exercício do Professor
print('\nExercício do Professor:')
soma = 0
cont = 0
for a in range(3, 501, 3):
    if a % 2 == 1:
        soma += a
        cont += 1
print('A soma de todos os {} os valores solicitados é {}'.format(cont, soma))
