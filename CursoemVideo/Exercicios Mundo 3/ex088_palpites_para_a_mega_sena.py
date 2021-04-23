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
    print(f'Game {n+1}: {m}')
    sleep(0.5)
print(f'{" < GOOD LUCK! > ":=^35}')
