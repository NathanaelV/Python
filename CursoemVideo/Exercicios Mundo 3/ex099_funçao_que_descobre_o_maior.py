# Class Challenge 20

# Função maior() receberá varios parametros
# Deve mostrar qual é o maior.
# Falar quais foram os maiores valores


def maior(*num):
    print('-=' * 30)
    big = 0
    print('Analyzing past values...')
    for a, n in enumerate(num):
        print(n, end=' ')
        if a == 0:
            big = n
        elif n > big:
            big = n
    print(f':{len(num)} values were entered in all.')
    print(f'The highest value is {big}')


def tit(msg):
    t = len(msg)//2 + 2
    print('-=' * t)
    print(f'  {msg.title()}')
    print('-=' * t)


tit('Calculating the highest!')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(2, 1)
maior(6)
maior()

print('-=' * 30)
value = list()
p = int(input('How many values do you want to analyze? '))
for c in range(0, p):
    value.append(int(input('Enter a number: ')))
maior(value)

# Teacher Example:
# Teacher example is similar
