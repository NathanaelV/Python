# Class Challenge 10

# Ler 3 números e decifrar qual o maior e qual o menor
a, b, c = input('Digite 3 números inteiros: ').split()
a, b, c = int(a), int(b), int(c)

if a > b:
    if a > c:
        maior = a
        menor = c if c < b else b
    else:
        maior = c
        menor = b
else:
    if b > c:
        maior = b
        menor = a if a < c else c
    else:
        maior = c
        menor = a
print('O maior é {} e o menor é {}'.format(maior, menor))
print('A = {}, B = {} e C = {}'.format(a, b, c))

# Exemplo do professor:

print('\nExemplo do professor: ')

menor = a  # Um chute, caso não seja a, vai ser trocado ao longo do código
if b < a and b < c
    menor = b
if c < a and c < b
    menor = c
maior = a
if b > a and b > c
    maior = b
if c > a and c > b
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
