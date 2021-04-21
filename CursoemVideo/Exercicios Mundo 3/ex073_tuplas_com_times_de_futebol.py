# Class Challenge 16

# Criar uma Tupla com os 20 primeiros tipes do Brasileirão
# Mostrar só os 5 primeiros
# Mostrar só os 4 últimos
# Mostrar em ordem alfabética
# Procurar o time da Chapecoense
# Times: Corinthians, Palmeiras, Santos, Gremio, Cruzeiro, Flamengo, Vasco
# Chapecoense, Atlético, Botafogo, Bahia, São Paulo, Fluminense, Esporte Recife,
# EC Vitoria, Coritíba, Avaí, Ponte Preta e Atletico Goianiense

teams = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Bahia', 'São Paulo', 'Fluminense', 'Esporte Recife', 'EC Vitoria', 'Coritíba', 'Avaí',
         'Ponte Preta', 'Atletico Goianiense')
print('-=' * 30)
print(f'The teams list: {teams}')
print('-=' * 30)
print(f'The first four: {teams[:4]}')
print('-=' * 30)
print(f'The last four: {teams[-4:]}')
print('-=' * 30)
print(f'The teams in alphabetic order: {sorted(teams)}')
print('-=' * 30)
print('Chapecoense team show in {}ª position.'.format(teams.index('Chapecoense')+1))
print('_' * 60)
print(f'Chapecoense team show in {teams.index("Chapecoense")}ª position.')
