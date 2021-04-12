# Class Challenge 09

# Ler o nome completo de uma pessoa e mostar o primeiro e o último

nome = str(input('Digite o seu nome completo: ')).strip()
a = nome.split()
print('O primeiro nome é {} e o último é {}'.format(a[0], a[0]))

# Exemplo do Professor

print('\nExemplo do Professor\n')
print('Olá, muito prazer.')
print('Seu primeiro nome é: {}'.format(a[0]))
print('Seu útimo nome é: {}'.format(a[len(a)-1]))
