# Challenge 16 - 21

# Importar a biblioteca de números aleatorios
import random
import emoji  #Tive que importar uma biblioteca que uma pessoa criou e disponibilizou
              #Fica na parte PyPI do site do Python

print(emoji.emojize('Hello World! :earth_americas:', use_aliases=True))
num = random.random()  #Gera um número aleatório entre 0 e 1
inteiro = random.randint(1, 4)  #Gera um ineiro dentro de um intervalo
                                #Os 2 nº estão inclusos
print(num, '\n', inteiro)
