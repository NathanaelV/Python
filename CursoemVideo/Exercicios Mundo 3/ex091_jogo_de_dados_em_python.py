# Class Challenge 19

# 4 players will roll a die and get random results
# Guardar tudo em um dicionario e mostrar em ordem (Não explicado em aula)
# Mostrar o resultado de cada jogador e depois mostrar um ranking com os resultados

from random import randint
from operator import itemgetter
from time import sleep

game = dict()
for j in range(1, 5):
    game[f'player {j}'] = randint(1, 6)
print('-=' * 15)
for k, v in game.items():
    print(f'{k} played {v}.')
    sleep(0.5)
print('-' * 30)
print(f'{"RANKING":^30}')
print('-' * 30)
sleep(0.5)
ranking = list()
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
# itemgetter(parte que quero ordenar. 0 são os jogadores, 1 são os números que os jogadores receberam
# Ele mostra em ordem crescente

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar:  {v[0].capitalize()} tirou {v[1]} nos dados.')
    sleep(0.5)
