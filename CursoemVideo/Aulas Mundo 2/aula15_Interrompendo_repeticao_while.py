# Challenge 66 - 71

n = s = 0
while n != 999:
    s += n
    n = int(input('Digite um número: '))
print('A soma é: {}'.format(s))

# Usando o comando Break:

print('\nUsing Infinity While: ')
n = s = 0
while True:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    s += n
print('The sum is {}')
