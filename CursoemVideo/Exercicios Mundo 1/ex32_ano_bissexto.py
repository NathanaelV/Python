# Class Challenge 10

# Ler se é ano bissexto

a = int(input('Digite um ano: '))

if a <= 1582:
    print('O conceito de ano bissexto ainda não tinha sido aplicado nesse ano.')
else:
    if a % 400 == 0 and a % 100 == 0:
        print('É ano bissexto!')
    else:
        if a % 100 == 0:
            print('Não é ano bissexto!')
        else:
            if a % 4 == 0:
                print('É ano bissexto!')
            else:
                print('Não é ano bissexto!')

# Outro jeito:
print('\nOutro jeito de responder:')
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('É ano bissexto!')
else:
    print('Não é ano bissexto!')
