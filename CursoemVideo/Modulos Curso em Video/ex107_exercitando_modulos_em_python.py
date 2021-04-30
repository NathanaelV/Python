# Class Challenge 22

# Criar um módulo chamado moeda.py
# Ter as funções aumentar() %; diminuir() %; dobrar() e metade()
# Fazer um programa(esse) que importa e usa esses módulos
# from ex107 import moeda

from ex107 import moeda

num = float(input('Enter a value: '))
print(f'Double of {num} is {moeda.dobrar(num)}')
print(f'A half of {num} is {moeda.metade(num)}')
print(f'{num} with 15% increase is {moeda.aumentar(num, 15)}')
print(f'{num} with 30% reduction is {moeda.diminuir(num, 30)}')
