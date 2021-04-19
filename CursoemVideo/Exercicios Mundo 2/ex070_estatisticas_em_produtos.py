# Class Challenge 15

# Read the name and price of various products and ask if you want to continue or not.
# In the end it should show:
# What is the total spent. How many products cost more than R$ 1000.
# Cheapest product name.

s = 0
over1000 = cheap = c = 0
cheapest = ''
while True:
    product = str(input('What is the product name? '))
    price = float(input('What is the product price? R$ '))
    answer = str(input('There is another product? [Y/N] ')).strip().upper()[0]
    while answer not in 'YN':
        print('\nINVALID! Enter a valid answer.')
        answer = str(input('There is another product? [Y/N] ')).strip().upper()[0]

    c += 1
    s += price
    if c == 1:
        cheap = price
        cheapest = product
    if price > 1000:
        over1000 += 1
    if cheap > price:
        cheap = price
        cheapest = product
    if answer == 'N':
        break
print('=' * 50)
print(f'The total spent is R$ {s}')
print(f'There are {over1000} products over R$ 1000.00.')
print(f'The cheapest product is the {cheapest.capitalize()} and coast R$ {cheap:.2f} ')
print('=' * 50)
