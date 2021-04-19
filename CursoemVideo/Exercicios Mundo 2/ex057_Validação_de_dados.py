# Class Challenge 14

# Pedir a digitação do sexo de uma pessoa, M ou F, caso esteja errado, solicitar novamente

r = ''
while r != 'M' and r != 'F':
    r = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
print('Obrigado!')

# Exemplo do professor:

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
# Pega só a primeira letra. Se digitar Masculino, pega só o M
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M/F]')).strip()[0]
print('O sexo {} foi registrado com sucesso.'.format(sexo.upper()))
