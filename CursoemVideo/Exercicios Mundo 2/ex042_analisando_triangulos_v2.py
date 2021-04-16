# Class Challenge 12

# Ler 3 segmentos de retas: Ver se pode formar um triângulo e qual será
# Equilátero, Isósceles ou Escaleno
print('-*' * 45)
print('\033[1;31mVamos verificar se é possível formar um triângulo e qual tipo de triângulo será.\033[m')
print('-*-' * 30)
r1 = int(input('Digite o primeiro valor de um segmento de reta: '))
r2 = int(input('Digite o segundo valro de um segmento de reta: '))
r3 = int(input('Digite o terceiro valor de um segmento de reta: '))

if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('Não é possível formar um triângulo.')
if r1 + r2 > r3 or r1 + r3 > r2 or r2 + r3 > r1:
    if r1 == r2 and r1 == r3:
        print('É possível formar um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É possível formar um triângulo isóceles.')
    else:
        print('É possível formar um triângulo escaleno.')
else:
    print('2 Não é possível formar um triângulo')