# Challenge 028 - 035

# Sabendo se o carro é velho ou não


print('\nTEORIA!\n')
tempo = int(input('Quantos anos tem seu carro?\n'))
if tempo <= 3:
    print('Carro novo.')
else:
    print('Carro velho.')
print('---FIM---')

# Condição simplificada
print('CARRO NOVO' if tempo <= 3 else 'CARRO VELHO')


# Parte Prática:

print('\nAULA PRÁTICA!\n')
nome = input('Qual seu nome? ').strip()
if nome.lower() == 'gustavo':
    print('Que nome bonito você tem!')
if 'silva' in nome.lower():
    print('Seu nome tem silva.')

print('Bom dia, {}.'.format(nome))


# Calbulando uma Média

print('\nCALCULANDO MÉDIA!\n')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média é {:.2f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

print('PARABÉNS!!!' if m >= 6.0 else 'ESTUDAR MAIS!!!')
