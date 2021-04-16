# Class Challenge 13

# Ler o peso de 5 pessas e verificar qual é maior e o menor
s = 0
maior = 0
menor = 100000
for c in range(0, 5):
    m = float(input('Digite um peso: (Kg) '))
    s += m
    if m > maior:
        maior = m
    if m < menor:
        menor = m
media = s / 5
print('O mais pesado pesa {}'.format(maior))
print('O mais leve pesa {}'.format(menor))
print('A média dos pesos é {:.1f}'.format(media))
