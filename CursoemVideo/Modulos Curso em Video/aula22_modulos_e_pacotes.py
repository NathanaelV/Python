# Challenge 107 - 112

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n*2


def triplo(n):
    return n*3


# Programa Principal
num = int(input('Enter a number: '))
fat = fatorial(num)
print(f'Factorial number of {num} is {fat}')
