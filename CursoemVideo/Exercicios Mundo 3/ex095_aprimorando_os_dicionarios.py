# Class Challenge 19

# Aprimorar o 93
# fazer para vários jogadores:
# Montar um Menu com o Nº, nome, quantidade de gols e o total
# Detalhes de aproveitamento se usuario pedir.
#    Mostra os jogos e quantos gol marcados nesses jogos
#    999 para sair do Menu

team = [{'name': 'Alan F.', 'goal': [2, 0]}, {'name': 'Rogerio M.', 'goal': [1]}, {'name': 'Azanha M.', 'goal': [0, 0]},
        {'name': 'Pedro V.', 'goal': [2, 1, 2, 4]}, {'name': 'Joaquim S.', 'goal': []},
        {'name': 'Nathan C.', 'goal': [5, 6, 5, 3]}, {'name': 'Cristiano R.', 'goal': [0, 2, 1]},
        {'name': 'Joao Judas', 'goal': [2, 1, -3]}]

'''
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
'''

print('-=' * 30)
print(f'{"Nª":<4}{"Name":<15}{"Total":<6}{"Goals":<15}')
print('-' * 50)
for n, d in enumerate(team):
    print(f'{n+1:<3}{d["name"]:<15}{sum(d["goal"]):<6}{d["goal"]}')
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
