# Challenge Class 007
# Mostrar o Dobro, triplo e raiz Quadrada

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do número {} é {}, o triplo é {}'.format(n, d, t), end=' ')
print('e a raiz quadrada é {:.4f}.'.format(r))

#Exemplo do professor:

n = int(input('Digite um número: '))
print('O Dobro: {}. O triplo: {}. E a raiz quadrada: {:.4f}.'.format(n*2, n*3, pow(n, 1/2)))
