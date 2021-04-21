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
print(f'The first four: {teams[:4]}')
print(f'The last four: {teams[-4:]}')
print(f'The teams in alphabetic order: {sorted(teams)}')
print('Chapecoense team show in {}ª position.'.format(teams.index('Chapecoense')+1))
