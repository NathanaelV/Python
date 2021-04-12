# Class Challenge 08

# Professor deve sortear um dos 4 alunos para apagar o quadro

import random
a1 = str(input('Nome do 1º aluno: '))
a2 = str(input('Nome do 2º aluno: '))
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')

aluno = [a1, a2, a3, a4]  #Lista
escolhido = random.choice(aluno)  #Escolhe um valor dentro da lista
# from random import choice
# escolhido = choice(aluno)
print('O aluno escolhido foi {}'.format(escolhido))

