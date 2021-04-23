# Class Challenge 18

# Read 7 integers numbers. Register in a single list.
# Separate odd(i) values from even(p).
# Show ever and odd numbers in ascending order.

allnumb = list()
even = list()
odd = list()
for n in range(1, 8):
    num = int(input(f'Enter {n}º number: '))
    if num % 2 == 0:
        even.append(num)

    else:
        odd.append(num)

allnumb.append(even)
allnumb.append(odd)
print(allnumb)
even.sort()
odd.sort()
print('=' * 30)
print(f'The even numbers are: {even}')
print(f'The odd numbers are:  {odd}')
