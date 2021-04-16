# Class Challenge 12

# Criar um programa que jogue Jokenpô
print('Vamos jogar Jokenpô')
from random import randint
computador = randint(0, 2) # 0 = Pedra, 1 = Papel, 2 = Tesoura
jogo = ['pedra', 'papel', 'tesoura']
print(jogo[computador])
print(computador)
# jogador = str(input('Digite sua escolha. Pedra, papel ou tesoura'))
# if jogador.lower() == 'pedra':
