# Class Challenge 12

# Ler 3 segmentos de retas: Ver se pode formar um triângulo e qual será
# Equilátero, Isósceles ou Escaleno
print('-*' * 45)
print('\033[1;31mVamos verificar se é possível formar um triângulo e qual tipo de triângulo será.\033[m')
print('-*-' * 30)
r1 = int(input('Digite o primeiro valor de um segmento de reta: '))
r2 = int(input('Digite o segundo valro de um segmento de reta: '))
r3 = int(input('Digite o terceiro valor de um segmento de reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:  # Python permite essa syntaxe
        print('É possível formar um TRIÂNGULO EQUILATERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É possível formar um TRIÂNGULO ISÓSCELES.')
    else:
        print('É possível formar um TRIANGULO ESCALENO.')
else:
    print('NÃO é possível formar um TRIÂNGULO')

# Exemplo do professor
print('\nExemplo do professor:')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:  # Caso não colocque r3 != r1, vai permitir que r1 = r3
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Não é possível formar um triângulo.')