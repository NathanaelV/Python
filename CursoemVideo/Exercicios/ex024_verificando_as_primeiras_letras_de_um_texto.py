# Class Challenge 09

# Ler o nome da Cidade e ver se começa com a palavra 'Santo'

cidade = input('Digite o nome da sua cidade: ')
minusculo = cidade.lower().strip().split()
# primeira = minu.strip()
# p = primeira.split()
print('Essa cidade tem a palavra santo?: {}'.format('santo ' in minusculo))
print('Santo é a primeira palavra?: {}'.format('santo ' in minusculo[0]))
# Se escrever kjalSANTO ele avisa como True

# print('Posição sem espaços: {}'.format(minu.find('santo')))
print('A palavra Santo aparece na posição: {}'.format(cidade.lower().find('santo')))

# Exemplo do Professor

print('\nExemplo do Professor:')
cid = str(cidade).strip()
# Sempre que for ler uma String, usar o strip() para tirar os espaços indesejados

print(cid[:5].lower() == 'santo')
# Irá ler só até a 5ª lentra e comparar se é igual a santo
