# Class Challenge 10

# Gerar um número entre 0 e 5. Escrever se acertou ou errou.

from random import randint
from time import sleep
# Comando sleep faz o computador esperar um tempo em segundos

a = randint(0, 5)
print(a)
N = int(input('Adivinhe um número de 0 a 5: '))

if N == a:
    print('Parabéns! Você acertou!')
else:
    if N < a:
        print('Muito baixo. Você errou :(\nO número era {}'.format(a))
    else:
        print('Muito alto. Você errou :(\nO número era {}'.format(a))

print('\nObrigado por jogar!')

# Exemplo do professor

print('\nExemplo do Professor:')
computador = randint(0, 5)  # Escolhe um número de 0 a 5
print(computador)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
print('PENSANDO...')
sleep(1)
jogador = int(input('Em que número eu pensei?\n'))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS!, você me venceu.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador))
