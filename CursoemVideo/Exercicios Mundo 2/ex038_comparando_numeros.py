# Class Challenge 12
# Entra 2 números interiros e devolve falando quem é maior ou se são iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é maior que o {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o {}'.format(n2, n1))
else:
    print('Os dois números são iguais')
