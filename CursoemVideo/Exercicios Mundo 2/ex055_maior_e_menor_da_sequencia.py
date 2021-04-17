# Class Challenge 13

# Ler o peso de 5 pessas e verificar qual é maior e o menor
s = 0
maior = 0
menor = 100000  # Gambiarra. Evitar fazer.
for c in range(1, 6):
    m = float(input('Digite o peso da {}ª pessoa: (Kg) '.format(c)))
    s += m
    if m > maior:
        maior = m
    if m < menor:
        menor = m
media = s / 5
print('O mais pesado pesa {}'.format(maior))
print('O mais leve pesa {}'.format(menor))
print('A média dos pesos é {:.1f}'.format(media))

# Exemplo do professor:

print('\nExemplo do professor: ')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:  # O primeiro será o maior e o menor
        maior = peso
        menor = peso
    else:       # À partir do segundo começa a comparação
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
