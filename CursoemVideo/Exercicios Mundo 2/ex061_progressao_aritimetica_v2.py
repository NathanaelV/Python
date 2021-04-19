# Class Challenge 14

# Ler o primeiro termo e a razão de uma PA. Mostrar os 10 primeiros números

primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
i = 0
while i < 10:
    print(primeiro, end=', ')
    primeiro += razao
    i += 1
print('Fim!')

# Exemplo do Professor:

print('\nExemplo do Professor:')
# Usar a razão do Exercício anterior.
primeiro = int(input('Digite o primeiro termo: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
