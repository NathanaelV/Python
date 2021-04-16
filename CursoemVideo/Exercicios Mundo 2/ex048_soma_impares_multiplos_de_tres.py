# Class Challenge 13

# Soma de todos os números ímpares, multiplos de 3 entre 1 e 500
# Fazer também um exemplo usando if else
s = 0
for a in range(0, 51):
    if a % 2 == 1 and a % 3 == 0:
        print(a)
        s += a
print('Soma =', s)
print('Fim')
