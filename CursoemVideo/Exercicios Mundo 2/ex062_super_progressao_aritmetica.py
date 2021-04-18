# Class Challenge 14

# Fazer o anterior, porém quando terminar, perguntat se quer saber mais termos
# Mostrar quantos termos o usuario está pedindo até o usuário digitar 0 (zero)

first = int(input('Digite o primeiro termo: '))
difference = int(input('Digite a razão: '))
i = 1
while i < 11:
    print(first, end=', ')
    first += difference
    i += 1
    if i == 11:
        n = int(input('\nDeseja saber mais quantos termos? '))
        i -= n
print('Fim!')
