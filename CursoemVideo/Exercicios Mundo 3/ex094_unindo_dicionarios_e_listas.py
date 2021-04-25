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
    person['age'] = int(input('Age: '))
    people.append(person.copy())
    
    resp = ' '
    while resp not in 'NnYy':
        resp = str(input('Do you want to continue: ')).strip()[0]
    if resp in 'Nn':
        break

print('-=' * 25)
person['total'] = 0
for a in people:
    person['total'] += a['age']
media = person['total'] / len(people)
print(f'There are {len(people)} people registered')
print(f'Media of the ages are: {media:.1f} years')
print('Women in the list are: ', end='')

for n, m in enumerate(people):
    if m['gender'] == 'F':
        print(f'{m["name"]}', end=', ')
print()
print('People who are above average age:')

for n, m in enumerate(people):
    if m['age'] > media:
        print('')
        for k, v in m.items():
            print(f'{k.capitalize()} = {v}', end='; ')
        # print('')
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
