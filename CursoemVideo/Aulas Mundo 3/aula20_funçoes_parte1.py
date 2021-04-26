# Challenge 96 - 100

# Bom para ser usado quando um comando é muito repetido.
def lin():
    print('-' * 30)


def título(msg):  # No lugar de msg, posso colocar qualquer coia.
    print('-' * 30)
    print(msg)
    print('-' * 30)
    print(len(msg))


título('Im Learning Python')

print('Good Bye')
lin()


def soma(a, b):
    print(F'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


print('\nSomando dois Valores')
soma(4, 6)
soma(b=5, a=8)  # Posso inverter a ordem, contanto que deixe explicito quem é quem

# Emapacotamento


def cont(*num):  # Vai pegar os parametros e desempacotar, não importq quantos
    print(num)  # Vai mostrar uma tupla, entre parenteses.
# Posso fazer tudo que faria com uma tupla


def contfor(*num):
    for v in num:
        print(f'{v}', end=', ')
    print('Fim')


def contar(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números')


print('\nContando o número de itens')
contfor(1, 2, 3, 5, 3, 2)
cont(1, 7, 3)
contar(3)


def dobra(lst):  # Por ser uma lista, não preciso usar o *
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


print('\nDobrando valores')
value = [5, 3, 6, 3, 8, 9, 0]
print(value)
dobra(value)
print(value)


def somamelhor(*num):
    s = 0
    for n in num:
        s += n
    print(f'A soma de {num} é igual a {s}.')


print('\nSoma varios valores')
somamelhor(3, 5, 1, 3)
somamelhor(3, 5)
