# Class Challenge 13

# Ler 6 números inteiros e só vai somar se for par.
# Números impares serão ignorados.
s = 0
i = 0
for a in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
    else:
        i += n
print('Soma dos pares =', s)
print('Soma dos ímpares', i)
