# Class Challenge 14

# Pedir a digitação do sexo de uma pessoa, M ou F, caso esteja errado, solicitar novamente

r = ''
while r != 'M' and r != 'F':
    r = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
print('Obrigado!')
