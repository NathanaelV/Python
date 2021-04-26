# Class Challenge 19

# Read Name, gender and age of several people.
# Guardando esse valor em um dicionário
# Mostrar:
#    Número de pessoa cadastradas: len()
#    A média da idade do grupo
#    Uma lista com todas as mulheres
#    Uma lista com as pessoas com idade acima da média

person = dict()
people = []

while True:
    person['name'] = str(input('Name: ')).strip()
    person['gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]
    while person['gender'] not in 'MF':
        print('ERROR! Please enter M or F: ')
        person['gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]
    person['age'] = int(input('Age: '))
    people.append(person.copy())

    resp = str(input('Do you want to continue? [Y/N] '))
    while resp not in 'NnYy':
        print('ERROR! Please enter Y or N.')
        resp = str(input('Do you want to continue? [Y/N] ')).strip()[0]
    if resp in 'Nn':
        break

print('-=' * 25)
person['total'] = 0
for a in people:
    person['total'] += a['age']
media = person['total'] / len(people)
print(f'A) There are {len(people)} people registered')
print(f'B) Media of the ages are: {media:.1f} years')
print('C) Women in the list are: ', end='')

for m in people:
    if m['gender'] == 'F':
        print(f'{m["name"]}', end=', ')
print()
print('D) People who are above average age:')

for m in people:
    if m['age'] > media:
        print('   - ', end='')
        for k, v in m.items():
            print(f'{k.capitalize()} = {v}', end='; ')
        print('')
print('\n<< ENCERRADO >>')

# Mostrando com , 'e' e ponto final:

print('\nTeste:')

old = 0
velho = list()  # List to save all category names
for p in people:  # Count how many people are in this group
    if p['age'] > person['total'] / len(people):
        velho.append(p['name'])
        old += 1
print('Pessoas com idade acima da média: ', end='')
for n, m in enumerate(velho):
    if n < old - 2:  # and m['age'] > person['total'] / len(people):
        print(m, end=', ')
    elif n < old - 1:  # and m['age'] > person["total"] / len(people):
        print(m, end=' and ')
    else:  # m['age'] > person['total'] / len(people):
        print(f"{m}.")


# Teacher Example:

print('\nTeacher Example:')

pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:.2f} anos')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=', ')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print(' << ENCERRADO >>')
