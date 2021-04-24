# Class Challenge 18

# Read Name and Weight of several people.
# How many people were registered.
# Show people with greater weight
# Show people with less weight

print('=' * 30)
print(f'{"REGISTRATION OF PEOPLE":^30}')
print('-' * 30)
person = list()
group = list()
count = wmax = wmin = 0
while True:
    print('-' * 30)
    person.append(str(input('Enter your name: ')))
    person.append(int(input('Enter your weight: ')))
    group.append(person[:])
    count += 1  # I don't need to use that, I can you use len(group) in the end.
    resp = ' '
    if count == 1:
        wmax = wmin = person[1]
    else:
        if wmax < person[1]:
            wmax = person[1]
        if wmin > person[1]:
            wmin = person[1]

    person.clear()

    while resp not in 'NnYy':
        resp = str(input('Do you want to continue? [Y/N] ')).strip()[0]
    if resp in 'Nn':
        break

print('=-' * 40)
print(f'There are {count} people registered: {len(group)}')  # I don't need that. I could use len(group)
print(f'The biggest weight is {wmax}. The people who have that weight are: ', end='')
for p in group:
    if p[1] == wmax:
        print(p[0], end=', ')
print(f'\nThe smallest weight is {wmin}. The people who have that weight are: ', end='')
for p in group:
    if p[1] == wmin:
        print(p[0], end=', ')

# Teacher Example:
# Teacher Example is Similar:
# They don't use a counter, he use a len(group) to know how many people are registration.
