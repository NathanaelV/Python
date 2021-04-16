# Class Challenge 12

# Criar um programa que jogue Jokenpô
print('Vamos jogar Jokenpô')
from random import randint
comp = randint(0, 2) # 0 = Pedra, 1 = Papel, 2 = Tesoura
jogo = ['pedra', 'papel', 'tesoura']
print(jogo[comp])
print(comp)
jogador = str(input('Digite sua escolha. Pedra, papel ou tesoura')).strip().lower()
print(jogador)
if jogador == 'pedra':

