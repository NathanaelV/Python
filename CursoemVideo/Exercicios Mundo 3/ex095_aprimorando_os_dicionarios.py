# Class Challenge 19

# Aprimorar o 93
# fazer para vários jogadores:
# Montar um Menu com o Nº, nome, quantidade de gols e o total
# Detalhes de aproveitamento se usuario pedir.
#    Mostra os jogos e quantos gol marcados nesses jogos
#    999 para sair do Menu

team = []
player = dict()
goal = list()

while True:
    print('-' * 30)
    player['name'] = str(input('Soccer player name: '))
    matches = int(input(f'How many matches {player["name"]} played? '))
    for c in range(0, matches):
        goal.append(int(input(f'How many goals in {c+1}º game? ')))
    player['goal'] = goal[:]
    goal.clear()
    team.append(player.copy())

    resp = ' '
    while resp not in 'YyNn':
        resp = str(input('Do you want to continue? [Y/N] ')).strip()[0]
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"Nª":<4}{"Name":<15}{"Goals":<15}{"Total":>6}')
print('-' * 50)
for n, d in enumerate(team):
    print(f'{n+1:<4}{d["name"]:<15}{str(d["goal"]):<15}{sum(d["goal"]):>6}')
print('-=' * 30)

while True:
    J = int(input('Do you want to know more about which player? (999 to exit) ')) - 1
    print('-' * 60)
    if 0 <= J < len(team):  # Count go to 0 to 7, but len(team) = 8
        print(f'-- Levantamento do Jodador {team[J]["name"]}')
        for n, v in enumerate(team[J]['goal']):
            print(f'    Game {n+1}, {team[J]["name"]} scored {v} goals.')
    elif J != 998:
        print('    INVALID! Please enter a valid option')
        print(f'    Your options go from 1 to {len(team)}')

    if J == 998:
        print('  <<< CHECK BACK OFTEN! >>>')
        break
    print('-' * 60)

# Teacher Example:

print('\nTeacher Example')

team = []
player = dict()
goal = list()

while True:
    print('-' * 30)
    player['name'] = str(input('Soccer player name: '))
    matches = int(input(f'How many matches {player["name"]} played? '))
    for c in range(0, matches):
        goal.append(int(input(f'How many goals in {c+1}º game? ')))
    player['goal'] = goal[:]
    player['total'] = sum(goal)
    goal.clear()
    team.append(player.copy())

    while True:
        resp = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Answer only Y or N.')
    if resp in 'Nn':
        break

print('-=' * 30)
print('Cod ', end='')
for i in player.keys():
    print(f'{i.upper():<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(team):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual Jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(team):
        print(f'ERROR! Não existe jogador de código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {team[busca]["name"]}')
        for i, g in enumerate(team[busca]["goal"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 30)
print(' <<< VOLTE SEMPRE >>>')
