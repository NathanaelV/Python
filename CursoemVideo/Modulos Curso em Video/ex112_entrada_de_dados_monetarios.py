# Class Challenge 22

# dentro de dado, criar função leia dinheiro, que funciona como input()
# Essa função deve ser capaz de ler um valor e saber se é númerico ou não
# Deve aceita se esse valor for digitado com virgula

from ex111.utilidades import dados
from ex111.utilidades.moeda import moeda
# Quando a funão é construida dentro do __init__.py, não precisa importar o arquivo

n = dados.leiadin('Enter a Value: ')
moeda.resumo(n, 35, 50)
