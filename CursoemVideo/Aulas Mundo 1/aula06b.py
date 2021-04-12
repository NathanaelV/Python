'''
n = float(input('Digite um valor: '))
print(n, type(n))   # Mesmo que coloque um valor interiro 4 vai aparecer 4.0
                    # Quando for usado o comando float

# print(n.isnumeric())  # O isnumeric() e de derivados
                        # não pode ser usado com float, bool ou int
                        # É um comando que só pode ser usado com str

b = bool(input('Digite um valor: '))
print(b) # Ele imprime True ou False
# Digitando algum valor será True, tem valor
# Só dando enter será False, não tem valor

'''

a = input('Digite algo:')
print('O valor {} é númerico?:'.format(a), a.isnumeric())  # Para saber se é numérico
print('O valor {} é letra?: {}.'.format(a, a.isalpha()))   # Para saber se é letra
print(a.isalnum())  # Para saber se é alphanumerico, (letra e/ou número)
print(a.isupper())  # Para saber se só tem letras maiúscula
# is... tem uma série de teste para saber se é True or False

# Challenges 003, 004,
