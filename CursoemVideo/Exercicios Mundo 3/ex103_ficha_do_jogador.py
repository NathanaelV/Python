# Class Challenge 21

# Montar a função ficha():
# Que recebe parametros opcionais: NOME de um jogador e quantos GOLS
# O programa deve mostrar os dados, mesmo que um dos valores não tenha sido informado corretamente
# jogador <desconhecido> fez 0 gols
# Adicionar as docstrings da função

def ficha(name='<unknown>', goals=0):
    print(f'Player {name} scored {goals} goals.')


n = input('Whats player name: ')
g = input('How many goals player scored: ')

ficha(n, g)
