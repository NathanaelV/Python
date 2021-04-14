# Class Challenge 10

# Calcular o preço da passagem de ônibus
# R$ 0,50 para viagens até 200 km
# R$ 0,45 para viages acima de 200 km

d = int(input('Qual a distância da sua viagem? '))

if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45

print('O preço da sua passagem é R$ {:.2f}'.format(p))

# Exemplo do professor

print('\nExemplo do professor!')
print('você está prestes a começar uma viagem de {} km'.format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será {:.2f}'.format(preço))
