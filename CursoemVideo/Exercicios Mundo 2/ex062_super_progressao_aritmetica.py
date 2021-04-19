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

# Exemplo do Professor:

print('\nExemplo do Professor:')
# Usar a razão do Exercício anterior.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais? '))
    print('Foram exibidos {} termos'.format(cont))
