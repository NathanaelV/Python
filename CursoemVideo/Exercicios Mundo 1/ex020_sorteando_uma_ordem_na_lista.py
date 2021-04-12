# Class Challenge 08

# Escolher ordem de apresentação dos alunos
import random

a1 = int(input('Nome do 1º aluno: '))
a2 = int(input('Nome do 2º aluno: '))
a3 = int(input('Nome do 3º aluno: '))
a4 = int(input('Nome do 4º aluno: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)  # Serve para embaralhar a lista
print('Ordem de apresentação é: '.format(lista))
