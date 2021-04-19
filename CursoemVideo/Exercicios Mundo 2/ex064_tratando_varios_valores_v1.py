# Class Challenge 14

# Ler vários números inteiros até o usuario digitar 999.
# Mostrar quantos foram digitados e mostrar a soma, disconciderando o 999

cont = 0
s = 0
n = 0
while n != 999:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n != 999:
        cont += 1
        s += n
print('Foram digitados {} numeros e a soma é {}'.format(cont, s))
