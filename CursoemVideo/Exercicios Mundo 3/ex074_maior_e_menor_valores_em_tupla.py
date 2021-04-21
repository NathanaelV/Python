# Class Challenge 16

# Gerar 5 números aleatórios e colocar em uma tupla
# Mostrar a lista dos 5 números
# Mostrar o maior e o menor da Tupla

from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(num)
order = sorted(num)
print(f'The largest number is {order[len(order)-1]}')
print(f'The smallest number is {order[0]}')
