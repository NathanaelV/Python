# Class Challenge 15

# Make a game to play 'par ou impar' (even or odd). The game will only stop if the player loses.
# Show how many times the player has won.
from random import randint
comp = randint(1, 6)
n = c = 0
while c < 10:
    print(comp, end=' ')
    c += 1

