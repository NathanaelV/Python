# Operação binarias são as operação que precisam de
# Pelo menos de 2 operadores

# == é usado para testar se uma coisa é igual a outra
# 5 + 2 é igual a quanto?
# Assim que se le o ==

'''
5 + 2 ==  # Adição +
5 - 2 ==  # Subtração -
5 * 2 ==  # Multiplicação *
5 / 2 ==  # Divisão /
5 ** 2 ==  # Potência **
pow(a,b) == a**b Porém perde a ordem de procedencia
5 // 2 ==  # Divisão inteira //
5 % 2 ==  # Resto da divisão ou modulo %
'''

# Ordem de precedência. Quem é resolvido primeiro
# 1º ()
# 2º **
# 3º *, /, //, % (Resolve quem aparecer primeiro)
# 4º +, - (Resolve quem aparecer primeiro)

# Em relação a calculo o Python não tem limite, o limite é a memeoria do PC
# Algusn exemplos de operadores que podem ser usados como String
# 'Oi'*4 = OiOiOiOi
# '  '*5 = '          '
print('='*20)

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!!!'.format(nome))
# Comando '{:20} escreve o que aparecer no espaço determinado, no caso 20
# Na falta de caracter ele completa com espaço

print('Prazer em te conhecer > :{:>20}!!!'.format(nome))
# :>20 Determina onde será o alinhamento. A direita

print('Prazer em te conhecer < :{:<20}!!!'.format(nome))
# Ou a esquerda

print('Prazer em te conhecer ^ :{:^20}!!!'.format(nome))
# Com o ^ ele fica centralizado.

print('Prazer em te conhecer .^ :{:.^20}!!!'.format(nome))
# Quando usa-se um ponto antes do ^, < ou >.
# O espaço será preenchido com esse ponto
# Funciona com (.,:;[]+-) um de cada vez


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma é {}.'.format(n1 + n2))
m = n1 * n2
d = n1 / n2
di = n1 // n2
dr = n1 % n2
e = n1 ** n2
print('Multiplicação: {}, Divisão: {:.4f}'.format(m, d), end=' !@! ')
# Para definir a quantidade de casas decimais
# end='' serve para não pulara linha
# O que for colocado entre os '' será reproduzido no final da linha
print('Divisão inteira: {}.\n Exponecial: {}'.format(di, e))
# Para pular linha no meio do print
# Só usar \n
print('Resto da Divisão: {}'.format(dr))
