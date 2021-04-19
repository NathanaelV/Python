# Class Challenge 14

# Ler vários números inteiros. Mostar no final o maior, menor e a média.
# Perguntar se quer continuar S/N digitando valores.

r = 'S'
s = c = bigger = smaller = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja digitar mais um número [S/N]: ')).strip().upper()[0]
    if c == 0:
        bigger = n
        smaller = n
    else:
        if bigger < n:
            bigger = n
        if smaller > n:
            smaller = n
    s += n
    c += 1
print('A soma dos {} números digitados é {}.'.format(c, s), end=' ')
print('E a média é {:.2f}'.format(s/c))
print('O maior é {} e o menor é {}'.format(bigger, smaller))
print('Fim!')

# Exemplo do professor:

print('\nExemplo do Professor:')
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if maior < núm:
            maior = núm
        if menor > núm:
            menor = núm
    resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {:.2f}.'.format(quant, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
