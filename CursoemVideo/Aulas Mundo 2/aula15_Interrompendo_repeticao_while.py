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
    n = int(input('Enter a number: [Type 999 to exit] '))
    if n == 999:
        break
    s += n
print('The sum is {}'.format(s))
# Usando um comando f string
# Posso colocar o s no meio das {}, só tenho que colocar um f no começo

print(f'The sum is {s}')

# Using f string
name = 'Jose'
age = 35
wage = 956.2
print(f'{name:~^20} is {age} years old and earns R$ {wage:.2f}')
