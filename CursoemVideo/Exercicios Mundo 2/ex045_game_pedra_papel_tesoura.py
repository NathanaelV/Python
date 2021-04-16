# Class Challenge 12

# Criar um programa que jogue Jokenpô
from random import randint
from time import sleep

print('Vamos jogar JOKENPÔ:')
comp = randint(0, 2)  # 0 = Pedra, 1 = Papel, 2 = Tesoura
game = ['pedra', 'papel', 'tesoura']
print(game[comp])

player = str(input('Digite sua escolha. Pedra, papel ou tesoura. ')).strip().lower()
a = 'Parabéns'
result = 'GANHOU'

if player == 'pedra':
    if comp == 0:
        result = 'EMPATOU'
        a = 'Quase'
    elif comp == 1:
        result = 'PERDEU'
        a = 'Não foi dessa vez'
    else:
        result = 'GANHOU'
        a = 'Parabéns'
if player == 'tesoura':
    if comp == 0:
        result = 'PERDEU'
        a = 'Não foi dessa vez'
    elif comp == 1:
        result = 'GANHOU'
        a = 'Parabéns'
    else:
        result = 'EMPATOU'
        a = 'Quase'
if player == 'papel':
    if comp == 0:
        result = 'GANHOU'
        a = 'Parabéns'
    elif comp == 1:
        result = 'EMPATOU'
        a = 'Quase'
    else:
        resul = 'PERDEU'
        a = 'Não foi dessa vez'
else:
    print('Escolha uma opção válida. Tente novamente')

print('{}, você {}! Você escolheu {} e o computador escocheu {}.'
      .format(a, result, player.upper(), game[comp].upper()))

# Exemplo do professor:

print('\nExemplo do professor:')
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Vamos JOGAR JOKENPÔ!!!
Escolha uma das opões: 
    [ 0 ] - PEDRA
    [ 1 ] - PAPEL
    [ 2 ] - TESOURA''')
jogador = int(input('Qual será sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 12)
print('Você jogou {}.'.format(itens[jogador]))
print('O Computador jogou {}.'.format(itens[comp]))
print('-=' * 12)
if comp == 0:  # Computador Jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogadro VENCE')
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('Opção inválida. Tente 0, 1 ou 2')

elif comp == 1:  # Computador Jogou PAPEL
    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('Opção inválida. Tente 0, 1 ou 2')

elif comp == 2:  # Computador Jogou TESOURA
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opção inválida. Tente 0, 1 ou 2')
