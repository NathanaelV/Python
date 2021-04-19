# Class Challenge 15

# Show a multiplication table, only stop when the user enters a negative number
n = 0
while True:
    print('=' * 50)
    print('{:^50}'.format('MULTIPLICATION TABLE'))
    print('{:^50}'.format('Enter a negative number to EXIT!'))
    print('=' * 50)
    n = int(input('Enter a number to find your multiplication table: '))
    c = 1
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c:>2} = {n*c}')
        c += 1
