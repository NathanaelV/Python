# Challenge 72 - 77

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudin', 'Batata Frita')
# Posso criar puplas sem usar parenteses
# Semelhante ao fatiamento de strings
print(lanche)
print('lanche[1]: ', lanche[1])
print('lanche[-1]: ', lanche[-1])
print('lanche[1:3]: ', lanche[1:3])
print('lanche[-2:]', lanche[-2:])

# Não posso atribuir valores a elementos da tupla, tenho que trocar tudo
# lanche[1] = 'Refigerante'  # Esse comando é inválido

# Usando for:
print('\nUsando o for:')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muito.\n')

print('length de lanche: ', len(lanche))

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}. Na posição {cont}')

for pos, cont in enumerate(lanche):  # pos = enumerate; cont = lanche. Na ordem
    print(f'Eu vou comer {cont}. Na posição {pos}')

# Mostrar em ordem alfabetica
print(sorted(lanche))  # Para fazer isso ele monta uma lista
print(lanche)
lanche = sorted(lanche)  # Aqui lanche passa a ser uma lista e deixa de ser tupla
print(lanche)

# Criando uma nova tupla:
print('\nMontado uma tupla com int:')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(f'a + b = {a+b}')
print(f'b + a = c = {b+a}')
print(f'c.count(5): {c.count(5)}')  # Mostra quantos tem
print(f'c.count(4): {c.count(4)}')
print(f'c.count(0): {c.count(0)}')
print(f'c.index(8): {c.index(8)}')
print(f'c.index(4): {c.index(4)}')
print(f'c.index(2): {c.index(2)}')  # Pega a primeira vez que aparece
print(f'c.index(5): {c.index(5)}')
print(f'c.index(5, 1): {c.index(5, 1)}')  # Procura o número 5 a partir da posição 1

# Mexendo com diferentes tipos:
print('\nMexendo com tipos diferente dentro de uma TUPLA.')
pessoa = 'Gustavo', 23, 98.5, 'M'
print(pessoa)
del(pessoa)  # para apagar qualquer coisa
