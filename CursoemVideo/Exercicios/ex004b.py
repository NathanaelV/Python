# Class Challenge 006

# Mostrar o tipo primitivo da valor e falar se é número, letra...
a = input('Digite algo: ')
print('No valor {} é do tipo:'.format(a), type(a))
print('No valor {} só tem número?: {}.'.format(a, a.isnumeric()))
print('No valor {} só tem letra?: {}.'.format(a, a.isalpha()))
print('No valor {} tem número e/ou letra?: {}.'.format(a, a.isalnum()))
print('No valor {} só tem letra maiúscula?: {}.'.format(a, a.isupper()))
print('No valor {} só tem letra minúscula?: {}.'.format(a, a.islower()))
print('No valor {} tem decimal?: {}.'.format(a, a.isdecimal()))
print('No valor {} só tem digitos?: {}.'.format(a, a.isdigit()))
print('O valor {} é uma Keyword no Python?: {}.'.format(a, a.isidentifier()))
print('O valor {} é Printable?: {}.'.format(a, a.isprintable()))
print('No valor {} só tem espaço?: {}.'.format(a, a.isspace()))
print('O valor {} é um titulo?: {}.'.format(a, a.istitle()))
print('Ufa!')
