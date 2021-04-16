# Class Challenge 12

# Criar um programa que jogue Jokenpô
print('Vamos jogar Jokenpô')
from random import randint
computador = randint(4, 6) # 4 = Pedra, 5 = Papel, 6 = Tesoura
print(computador)
jogador = str(input('Digite sua escolha. Pedra, papel ou tesoura'))
if jogador.lower() == 'pedra':
