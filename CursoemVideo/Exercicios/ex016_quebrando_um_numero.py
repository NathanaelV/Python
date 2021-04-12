# Class Challenge 08

#Criar um programa que leia um nº real e mostre só a parte inteira

from math import floor, trunc
num = float(input('\nDigite um número com ponto: '))
print('A parte inteira do número {} é {}'.format(num, floor(num)))

# Teacher Exercise

print('A parte inteira do número {} é {}'.format(num, trunc(num)))

# Execultando o exercício sem usar a biblioteca de matemática
print('A parte interira do número {} é {}'.format(num, int(num)))
