# Class Challenge 21

# Montar a função ficha():
# Que recebe parametros opcionais: NOME de um jogador e quantos GOLS
# O programa deve mostrar os dados, mesmo que um dos valores não tenha sido informado corretamente
# jogador <desconhecido> fez 0 gols
# Adicionar as docstrings da função

def ficha(name='<unknown>', goals=0):
    """
    -> Function to read a player name and scored
    :param name: (Optional) If user don't enter a name, the program will print '<unknown>'
    :param goals: (Optional) If user don't enter number of goals, the program will print 0
    :return: No return
    """
    print(f'Player {name} scored {goals} goals.')


n = input('Whats player name: ')
g = input('How many goals player scored: ')

if n == '' and g == '':
    ficha()
elif n == '':
    ficha(goals=g)
elif g == '':
    ficha(n)
else:
    ficha(n, g)


# Teacher example:


def fichap(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')


# Principal Program
n = str(input('Nome do Jogador: '))
g = str(input('Número de gol(s): '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(goals=g)
else:
    ficha(n, g)
