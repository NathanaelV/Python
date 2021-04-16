# Class Challenge 13

# Ler 6 números inteiros e só vai somar se for par.
# Números impares serão ignorados.
s = 0  # Para somar os pares (Acumulador)
p = 0  # Contadores de pares
i = 0  # Para somar os ímpares (Acumulador)
im = 0  # Contador de impares
c = 0  # (Contador)
for a in range(1, 7):
    n = int(input('Digite o {}º número: '.format(a)))
    c += 1
    if n % 2 == 0:
        s += n
        p += 1
    else:
        i += n
        im += 1
print('Soma dos pares =', s)
print('Soma dos ímpares', i)

# Exemplo do professor:

print('\nExemplo do professro:')
print('Dos {} valores apresentados, {} é(são) par(es) e a soma é {}.'.format(c, p, s))
print('Dos {} valores apresentados, {} é(são) impar(es) e a soama é {}.'.format(c, im, i))
