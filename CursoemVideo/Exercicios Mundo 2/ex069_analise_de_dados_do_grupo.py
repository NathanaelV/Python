# Class challenge 15

# Read age and sex of several people.
# The computer must ask each person whether they want to continue or not.
# In the end it should show:
# How many are over 18. How many men have. How many women under 20.
# Validate the information, only accept if the information is correct.

older18 = men = women = 0
while True:
    print('-' * 40)
    print('{:^40}'.format('REGISTER PERSON'))
    print('-' * 40)
    age = int(input('Enter your age: '))
    gender = str(input('Enter your gender [M/F]: ')).strip().upper()[0]
    while gender not in 'MF':
        gender = str(input('\nInvalid! Enter a valid gender [M/F]: ')).strip().upper()[0]

    answer = str(input('Do you wish to continue? [Y/N] ')).strip().upper()[0]
    while answer not in 'YN':
        print('\nInvalid!!! Enter a valid alternative. ')
        answer = str(input('Do you wish to continue? [Y/N] ')).strip().upper()[0]

    if age > 18:
        older18 += 1
    if gender == 'M':
        men += 1
    if gender == 'F' and age < 20:
        women += 1
    if answer == 'N':
        break

print('-' * 40)
print(f'There are {older18} people over 18 years old.')
print(f'There are {men} men.')
print(f'There are {women} women under 20 years old.')

# Teacher example:

print('\nTeacher Example: ')

tot18 = totM = totM20 = tot = 0
while True:
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    tot += 1
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 40)
print(f'Das {tot} pessoas cadastradas, temos:')
print(f'Total de {tot18} pessoas com mais de 18 anos.')
print(f'Ao todo são {totM} homens cadastrados.')
print(f'E {totM20} mulheres com menos de 20 anos.')
