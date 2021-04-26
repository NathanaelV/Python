# Challenge 101 - 106

# Interactive Help
# help()
# help(print())  - Para mostrar uma função específica.
# print(input.__doc__)  - Para ver ver de outro explicação de um comando


# Docstring: Documentação das string, um manual


# A Docstring é escrita com """ """ (3 aspas duplas) logo abaixo da função def
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Ass.: Aqui posso colocar o meu nome.
    """
# O Comando digitado acima aparece quando digitar help(contador)
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim!')


contador(0, 100, 10)
help(contador)
# Qualquer pessoa que importe essa função terá acesso a Docstring


# Parte Prática
def fatorial(num=1):  # Valor opcional. Caso eu não receba um número, vai retornar 1
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

print('\nFatorial: ')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


# Parametros opcionais:

# Caso só receba os valores a e b, c vai valer automaticamente 0
# Caso eu não informe a ou b, dará erro, a menos que eu informe os parametros opcionais
# Como foi o caso de c. Posso fazer isso para todas as variaveis
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')

print('\nSomar: ')
somar(1, 3, 2)  # Porém se informar mais de 3 dará erro.
somar(3, 4)  # Para mais n valores devo usar o descompactador: * num
somar()


# Escopo de Variavéis: Global e

print('\nESCOPO GLOBAL e LOCAL!')


def teste(b):  # b = n = 2
    global d  # quando usar esse comando o vou usar o d GLOBAL não o LOCAL
    b += 4  # b = 6
    d = 5  # Cria um ESCOPO LOCAL de n = 5. O GLOBAL ainda vale 2
    x = 8  # X não pode ser execultado fora teste. Tem um ESCOPO LOCAL
    print(f'Na função teste d vale {d}.')  # n pode, pois tem um ESCOPO GLOBAL
    print(f'Na função teste x vale {x}.')
    print(f'Na função teste b = {b}')


# Programa principal:
d = 2
print(d)
teste(d)
print(f'No programa principal n = {d}.')


# Retorno de Valores

print('\nRetorno de valores:')


def somando(a=0, b=0, c=0):
    s = a + b + c
    return s  # Com isso posso usar o f'{}'. Não só um print
# É bom quando quero personalisar a resposta


r1 = somando(3, 2, 5)  # Aqui vou recer a variálvel s e posso igualar a outra variável
r2 = somando(1, 7)
r3 = somando(4)
print(f'As somas são r1 = {r1}, r2 = {r2} e r3 = {r3}')


# Para retornar um Bool valor verdadeiro ou falso:
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print(f'{num} é par.')
else:
    print(f'{num} não é par')
