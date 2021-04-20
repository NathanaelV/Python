# Class Challenge 15

# Make a game to play 'par ou impar' (even or odd). The game will only stop if the player loses.
# Show how many times the player has won.
from random import randint

c = 0
print('Lets play Par ou Impar')

while True:
    comp = randint(1, 4)
    np = int(input('Enter a number: '))
    rp = str(input('type a guess [P/I]: ')).strip().upper()[0]
    while rp not in 'PpIi':
        rp = str(input('Enter a valid guess [P/I]: ')).strip().upper()[0]
    print(f'You played {np} and computer played {comp}')
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
        print('~~' * 20)
        print('The Computer win')
        print(f'You won {c} matches in a row')
        print('Try again.')
        print('~~' * 20)
        break

# Teacher Example:

print('\nTeacher example: ')
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 4)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar Novamente...')
print(f'GAME OVER. Você venceu {v} vez(es).')
