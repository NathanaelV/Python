# Class Challenge 10

# Ler se é ano bissexto

a = int(input('Digite um ano: '))

if a <= 1582:
    print('O conceito de ano bissexto ainda não tinha sido aplicado no ano {}.'.format(a))
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

# Exemplo do professor:

print('\nOutro jeito de responder:')

from datetime import date

ano = int(input('Digite o ano que deseja analisar ou 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É ano bissexto!'.format(ano))
else:
    print('{} Não é ano bissexto!'.format(ano))
