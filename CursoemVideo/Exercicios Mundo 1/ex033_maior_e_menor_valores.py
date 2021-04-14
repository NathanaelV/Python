# Class Challenge 10

# Ler 3 números e decifrar qual o maior e qual o menor
a, b, c = input('Digite 3 números inteiros: ').split()
a, b, c = int(a), int(b), int(c)

if a > b:
    if a > c:
        print('O maior é {}'.format(a))
    else:
        print('O maior é {}'.format(c))
else:
    if b > c:
        print('O maior é {}'.format(b))
    else:
        print('O maior é {}'.format(c))

print('A = {}, B = {} e C = {}'.format(a, b, c))

