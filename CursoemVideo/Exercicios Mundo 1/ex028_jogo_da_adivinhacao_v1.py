# Class Challenge 10

# Gerar um número entre 0 e 5. Escrever se acertou ou errou.

from random import randint

a = randint(0, 5)
print(a)
N = int(input('Adivinhe um número de 0 a 5: '))

if N == a:
    print('Parabéns! Você acertou!')
else:
    if N < a:
        print('Muito baixo. Você errou :(')
    else:
        print('Muito alto. Você errou :(')

print('\nObrigado por jogar!')
