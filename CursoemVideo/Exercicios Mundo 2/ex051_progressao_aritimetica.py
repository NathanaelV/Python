# Class Challenge 13

# Ler o primeiro termo e a razão da P.A. e mostrar os 10 primeiros números
print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))
t = int(input('Digite o 1º termo: '))
r = int(input('Digete a razão da PA: '))
for a in range(t, t + 10*r, r):
    print(a, end=', ')
print('\nFim!')
