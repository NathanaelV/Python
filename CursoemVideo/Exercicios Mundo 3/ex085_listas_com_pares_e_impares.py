# Class Challenge 18

# Read 7 integers numbers. Register in a single list.
# Separate odd(i) values from even(p).
# Show ever and odd numbers in ascending order.

allnumb = list()
even = list()
odd = list()
for n in range(0, 7):
    allnumb.append(int(input(f'Enter {n+1}º number: ')))
    print(allnumb)

    if allnumb[n] % 2 == 0:
        even.append(allnumb[n])
        print(even)

    else:
        odd.append(allnumb[n])
        print(odd)

allnumb.append(even)
allnumb.append(odd)
even.sort()
odd.sort()
print('=' * 30)
print(f'The even numbers are: {even}')
print(f'The odd numbers are:  {odd}')

# Teacher Example:

print('\nTeacher Example:')

núm = [[], []]

for c in range(1, 8):
    valor = int(input(f'Enter {c} value: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'The even values entered were: {núm[0]}')
print(f'The odd values entered were: {núm[1]}')
