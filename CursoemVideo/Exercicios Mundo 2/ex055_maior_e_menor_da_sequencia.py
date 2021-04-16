# Class Challenge 13

# Ler o peso de 5 pessas e verificar qual é maior e o menor
maior = 0
menor = 100000
for c in range(0, 5):
    m = float(input('Digite um peso: (Kg)'))
    if m > maior:
        maior = m
    if m < menor:
        menor = m
