# Class Challenge 22

# Ao invés de usar uma função para formatar para 2 casas decimais
# Usar um parâmetro

from ex109 import moeda

p = float(input('Enter a Value: '))
print(f'Double of {moeda.moeda(p)} is {moeda.dobrar(p, False)}')
print(f'A half of {moeda.moeda(p)} is {moeda.metade(p, True)}')
print(f'{moeda.moeda(p)} with 15% increase is {moeda.aumentar(p, 15, True)}')
print(f'{moeda.moeda(p)} with 30% reduction is {moeda.diminuir(p, 30, True)}')
