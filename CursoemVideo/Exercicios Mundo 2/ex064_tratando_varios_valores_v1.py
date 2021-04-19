# Class Challenge 14

# Ler vários números inteiros até o usuario digitar 999.
# Mostrar quantos foram digitados e mostrar a soma, disconciderando o 999

cont = 0
s = 0
n = 0
while n != 999:  # O númeor de parada é o Flag
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n != 999:
        cont += 1
        s += n
print('Foram digitados {} numeros e a soma é {}'.format(cont, s))

# Exemplo do professor:

print('\nExemplo do professor:')
cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} número(s) e a soma entre eles foi {}.'.format(cont, soma))
