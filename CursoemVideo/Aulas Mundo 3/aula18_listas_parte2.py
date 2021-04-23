# Challenge 84 - 89

# Colocando listas dentro de listas

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
# Com esse comando, consigo fazer uma copia da estrutura
# Consigo editar uma sem interferir na outra.

print(f'Teste: {teste}')
print(f'Galera: {galera}')
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # Fazer teste retirando o [:]
# Criou uma ligação entre as duas estruturas.
# Se eu não usar o [:], no próximo print galera vai aparecer João no lugar de Maria
# Caso eu use, João não aparece no lugar de Maria.

print(f'Teste: {teste}')
print(f'Galera: {galera}')

teste[0] = 'João'
teste[1] = 15
print(f'Teste: {teste}')
print(f'Galera: {galera}')

gente = [['João', 23], ['Maria', 32], ['Joaquim', 43]]
print(f'Gente[2][1]: {gente[2][1]} e Gente[0][0]: {gente[0][0]}')

for p in gente:
    print(f'P = {p}')  # Mostra cada lista
    for a in range(0, len(p)):
        print(f'P[{a}] = {p[a]}')  #Mostra o primeiro intem da lista
    for a in range(0, len(p[0])):
        print(f'P[0][{a}]: {p[0][a]}')  # Mostra a letra de lista

print()
for p in gente:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('\nColetando Dados e colcando em listas:')

pesquisa = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pesquisa.append(dados[:])  # Caso eu não crie essa lista
    dados.clear()  # Cada vez que eu apagar dados, vai apagar tudo.
# Se eu não usar o clear, vou apenas adicionando os dados em uma única lista
#
print(pesquisa)

# Para ter somente os que são maiores de idade:

totmai = totmen = 0  # Esse comando só é possível com variaveis simples
# Não é possível fazer isso com listas.

for i in pesquisa:
    if i[1] >= 21:
        print(f'{i[0]} tem {i[1]} e é maior de idade(21).')
        totmai += 1
    else:
        print(f'{i[0]} tem {i[1]} e é menor de idade(21).')
        totmen += 1
print(f'Temos {totmen} menores e {totmai} maiores de idade')