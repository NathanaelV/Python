# Class Challenge 15

# Make a game to play 'par ou impar' (even or odd). The game will only stop if the player loses.
# Show how many times the player has won.
from random import randint

c = 0
print('Lets play Par ou Impar')

while True:
    comp = randint(1, 6)
    np = int(input('Enter a number: '))
    rp = str(input('type a guess [P/I]: ')).strip().upper()[0]
    while rp not in 'PpIi':
        rp = str(input('Enter a valid guess [P/I]: ')).strip().upper()[0]

    s = np + comp
    if s % 2 == 0:
        r = 'P'
    else:
        r = 'I'

    if rp == r:
        print('~~' * 20)
        print('CONGRATULATIONS! You Win.')
        print('Lets play again...')
        print('~~' * 20)
        c += 1
    else:
        print('The Computer win')
        print(f'You won {c} matches in a row')
        print('Try again.')
        break
