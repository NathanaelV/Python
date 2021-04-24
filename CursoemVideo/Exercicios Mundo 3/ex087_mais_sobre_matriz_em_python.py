# Class challenge 18

# Using the same statement as in exercise 86:
# Show the sum of all even values.
# Show the sum of the third column.
# Show the highest value in the second row.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for m in range(0, 3):
    for n in range(0, 3):
        matrix[m][n] = int(input(f'Enter the value [{m}][{n}]: '))
print('=+=' * 15)
for m in range(0, 3):
    for n in range(0, 3):
        print(f'{matrix[m][n]:^5}', end='')
    print()
print('=+=' * 15)

even = 0
for m in matrix:
    for a in range(0, 3):
        if m[a] % 2 == 0:
            even += m[a]
print(f'The sum of all even numbers is {even}')

column = 0
for m in matrix:
    column += m[2]
print(f'The sum of all third column is: {column}')

print(f'The highest value in the second row: {max(matrix[1])}')

# Teacher Example:

print('\nTeacher Example:')

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mai = 0
for m in range(0, 3):
    for n in range(0, 3):
        matrix[m][n] = int(input(f'Enter the value [{m}][{n}]: '))
print('=+=' * 15)
for m in range(0, 3):
    for n in range(0, 3):
        print(f'{matrix[m][n]:^5}', end='')
        if matrix[m][n] % 2 == 0:
            spar += matrix[m][n]
    print()
print('=+=' * 15)
print(f'A soma de todos os valores pares é {spar}')

for m in range(0, 3):
    scol += matrix[m][2]
print(f'A soma dos valores da terceira coluna é {scol}')

for n in range(0, 3):
    if n == 0:
        mai = matrix[1][n]
    else:
        if mai < matrix[1][n]:
            mai = matrix[1][n]
print(f'O maior valor da segunda coluna é {mai}')
