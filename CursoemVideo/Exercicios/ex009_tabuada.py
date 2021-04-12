# Class Challenge 007
# Fazer a tabuada de um número


n = int(input('Digite um número: '))
print('{0} x 1 = {0}\n{0} x 2 = {1}\n{0} x 3 = {2}'.format(n, n*2, n*3))
print('{0} x 4 = {1}\n{0} x 5 = {2}\n{0} x 6 = {3}'.format(n, n*4, n*5, n*6))
print('{0} x 7 = {1}\n{0} x 8 = {2}\n{0} x 9 = {3}'.format(n, n*7, n*8, n*9))
print('{0} x 10 = {0}0'.format(n))


# Teacher Example
n = int(input('Digite um número para saber sua tabuada: '))
print('-'*13)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-'*13)
