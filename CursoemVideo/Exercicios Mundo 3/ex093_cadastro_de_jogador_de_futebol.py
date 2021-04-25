# Class Challenge 19

# Ler nome do jogador e quantas partidas jogou
# Ler quantos gols marcou em cada jogo. 4 partidas, 4 entradas
# Guardar os gols em uma lista

player = dict()
goal = list()
player['name'] = str(input('Soccer player name: '))
matches = int(input('How many matches: '))
player['goals'] = 0
player['total'] = 0
for c in range(0, matches):
    goal.append(int(input(f'How many goals int the {c+1}º match: ')))
    player['goals'] = goal.copy()
    player['total'] += goal[c]

print('-=' * 20)
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'The player {player["name"]} played {matches} matches')
for i, a in enumerate(goal):
    print(f'    => Matche {i+1}, he scored {a} goals.')
print(f'The total of goals was {player["total"]}')
