# Class Challenge 09

# Ler o nome completo de uma pessoa e mostrar:
# todas as letras em minúsculas e depois em maiúscula
# Quantas letras sem contar os epaços
# Quantas letras o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
# Usar o strip no input

print('Nome:', nome)
print(nome.upper())
print(nome.lower())
a = nome.split()
print(a)
print('No primeiro nome tem {} letras.'.format(len(a[0])))
print('Quantas letras tem no nome c/ espaço: ', len(nome))
print('Nome sem espaço:', ''.join(a))
print('Quantas letras tem o nome completo: ', len(''.join(a)))

# Exemplo do Professor

print('\nExemplo do Professor: \n')
print('Analisando seu nome...')
print('Seu nome me maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minusculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
# Contas os espaçõs e subtrai da contagem total de letras

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# Conta a partir da primeira letra com 0, quando ele mostrar a posição do primeiro
# espaço será a quantidade de letras.
# Se a pessoa só colocar um nome vai dar problema
