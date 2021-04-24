# Class Challenge 18

# Ask the user how many guesses he wants.
# Draw 6 numbers for each guess in a list.
# In a interval between 1 and 60. Numbers can't be repeated
# Show numbers in ascending order.
# To use sleep(1)

from random import randint
from time import sleep

luck = list()
mega = list()

print('=' * 30)
print(f'{"MEGA SENNA!":^30}')
print('=' * 30)
guess = int(input('How many guesses would you like? '))

for a in range(0, guess):
    while True:
        num = randint(1, 60)
        if num not in luck:
            luck.append(num)
        if len(luck) == 6:
            break
    luck.sort()
    mega.append(luck[:])
    luck.clear()

print(f'\n=-=-=-=-= Drawing {guess} Games =-=-=-=-=')
sleep(0.5)
for n, m in enumerate(mega):
    print(f'Game {n+1:<2}: [ ', end='')
    for a in range(0, 6):
        if a < 5:
            print(f'{m[a]:>2}', end=' - ')
        else:
            print(f'{m[a]:>2} ]')
    sleep(0.5)
print(f'{" < GOOD LUCK! > ":=^35}')


# Teacher Example:


print('\nTeacher Example: ')

lista = list()
jogos = list()
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-=' * 5, f'{"< BOA SORTE >":^20}', '-=' * 5)
