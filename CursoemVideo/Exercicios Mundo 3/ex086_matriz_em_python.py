# Class Challenge 18

# Make a 3x3 matrix with a values entered.
# Shows the matrix with the correct formatting.
# Using a single list with other lists.

matrix = list()
inter = list()
for m in range(0, 3):
    inter.append(int(input(f'Enter [{m}][0] number: ')))
    inter.append(int(input(f'Enter [{m}][1] number: ')))
    inter.append(int(input(f'Enter [{m}][2] number: ')))
    matrix.append(inter[:])
    inter.clear()
print('=+=' * 20)
print(f'[ {matrix[0][0]} ][ {matrix[0][1]} ][ {matrix[0][2]} ]')
print(f'[ {matrix[1][0]} ][ {matrix[1][1]} ][ {matrix[1][2]} ]')
print(f'[ {matrix[2][0]} ][ {matrix[2][1]} ][ {matrix[2][2]} ]')
