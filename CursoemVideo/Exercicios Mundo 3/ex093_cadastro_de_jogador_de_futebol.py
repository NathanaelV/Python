# Class Challenge 19

# Ler nome do jogador e quantas partidas jogou
# Ler quantos gols marcou em cada jogo. 4 partidas, 4 entradas
# Guardar os gols em uma lista

player = dict()
goal = list()
player['name'] = str(input('Soccer player name: '))
matches = int(input(f'How many matches {player["name"]} played: '))
player['goals'] = 0
player['total'] = 0
for c in range(0, matches):
    goal.append(int(input(f'   How many goals int the {c+1}º match: ')))
    player['total'] += goal[c]
    player['goals'] = goal.copy()  # Ou = goal[:]


print('-=' * 20)
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'The player {player["name"]} played {matches} matches')
for i, a in enumerate(goal):
    print(f'    => Matche {i+1}, he scored {a} goals.')
print(f'The total of goals was {player["total"]}')
print(player)

# Teacher Example:

print('\nTeacher Example:\n')
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome: ')).strip()
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantas gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')
