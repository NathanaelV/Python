# Aula 006 - Tipos de Primitivos e Saída de Dados
# Go to Challenges 003 and 004

# Class Code 004

a = input('Digite um número:')  # int é usado para número inteiro
b = input('Digite outro número:')
c = a + b
print('A Soma é =', c)  # Answer = ab
print(type(c))  # Para saber qual o tipo primitivo

# Os quatro tipos primitivos mais usados
# int - Número Inteiros (Positivos, Negativos e 0)
# float - Número Reais / fracionados (Ponto flutuante)
# bool - Valores lógicos ou Booleanos (True, False) Primeira letra maiúscula
# str - O que estiver entre ' '.

# Class Code 006
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
# print('A = {}, b = {}, n1 = {}, n2 = {}'.format(a, b, n1, n2))

s = n1 + n2
print('A soma é =', s)
print('A soma vale {}!'.format(s))
print('O tipo primitivo é:', type(s))

print('A soma entre {} e {} é: {} e é do tipo: {}'.format(n1, n2, s, type(s)))
# Dentro dos {} só aceita a sequencia começando em 0...
# Mas se for usar o modo manual, deve ser feito em todos
# Quando usa-se o modo manual, é possivel mostrar em qualquer ordem
# {2} {0} {1}