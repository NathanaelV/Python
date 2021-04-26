# Challenge 96 - 100

# Bom para ser usado quando um comando é muito repetido.
def lin():
    print('-' * 30)


def título(msg):  # No lugar de msg, posso colocar qualquer coia.
    print('-' * 30)
    print(msg)
    print('-' * 30)


título('Im Learning Python')
lin()
print('Good Bye')


def soma(a, b):
    print(F'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


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


contfor(1, 2, 3, 5, 3, 2)
cont(1, 7, 3)
contar(3)

