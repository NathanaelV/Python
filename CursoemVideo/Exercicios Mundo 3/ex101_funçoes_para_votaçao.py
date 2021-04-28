# Class Challenge 21

# Ler o ano de nascimento da pessoa. Calcular idade
# Calcular a idade e dizer se essa pessoa tem voto: Negado, Facultativo ou Obrigatório
# Retornar uma frase: Facultativo entre 16 e 17 e acima de 65 anos
# Adicionar as docstrings da função
from datetime import date


def voto(y):
    """
    -> Função para calcular idade e ver se a pesso pode votar
    :param y: Entrada do ano de nascimento.
    :return: Não retorna
    """
    x = date.today().year - y
    if x < 16:
        print(f'Você tem {x} anos, por isso ainda Você ainda NÃO PODE votar.')
    elif 16 <= x < 18 or x >= 65:
        print(f'Voto Facultativo. Você tem {x} anos, pode votar se quiser.')
        print('BOM VOTO!')
    else:
        print(f'Voto Obrigatório! Você tem {x} anos e terá que votar nas próximas eleições')
        print('BOM VOTO!')


print('~~' * 15)
print(' Descubra se você pode votar'.upper())
print('~~' * 15)
nasc = int(input('Qual ano você nasceu? '))
voto(nasc)
