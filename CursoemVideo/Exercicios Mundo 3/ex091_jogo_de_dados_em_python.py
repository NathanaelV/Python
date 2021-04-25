# Class Challenge 19

# 4 players will roll a die and get random results
# Guardar tudo em um dicionario e mostrar em ordem (Não explicado em aula)
# Mostrar o resultado de cada jogador e depois mostrar um ranking com os resultados
from random import randint

game = dict()
for j in range(1, 5):
    game[f'player {j}'] = randint(1, 6)
print('-=' * 15)
for k, v in game.items():
    print(f'{k} played {v}.')
print('-' * 30)
print(f'{"RANKING":^30}')
print('-' * 30)
print(game)



