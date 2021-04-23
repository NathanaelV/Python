# Class challenge 18

# Using the same statement as in exercise 86:
# Show the sum of all even values.
# Show the sum of the third column.
# Show the highest value in the second row.

inter = list()
matrix = list()

for m in range(0, 3):
    inter.append(int(input(f'Enter a number for Matrix [{m}][0]: ')))
    inter.append(int(input(f'Enter a number for Matrix [{m}][1]: ')))
    inter.append(int(input(f'Enter a number for Matrix [{m}][2]: ')))
    matrix.append(inter[:])
    inter.clear()
print('=+=' * 30)
print(f'[ {matrix[0][0]} ][ {matrix[0][1]} ][ {matrix[0][2]} ]')
print(f'[ {matrix[1][0]} ][ {matrix[1][1]} [] {matrix[1][2]} ]')
print(f'[ {matrix[2][0]}')