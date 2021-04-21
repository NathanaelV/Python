# Challenge 78 - 83

# A grande vantagem da lista em relação a tupla, ela é mutável

# Adicionar:
# lanche.append('item novo') vai para o final
# lanche.insert(0, 'item novo') adiciona em uma posição específica.

# Apagar um intem da lista:
# del.lanche(2); lanche.pop(2) normalmente usado para remover o último valor
# lanche.remove('item')

# Declarar lista: Criar um lista com um comando
# valores = list(range(4,11)) - Cria valores de 4 a 10, não tem o último

# valores.sort() - Para organizar
# valores.sort(reverse=True) - Para colocar na ordem inversa

num = [2, 5, 9, 1]
print(f'Valor de num: {num}')
num[2] = 4
print(f'Valor de num: {num}')
print(f'num.sort(): {num.sort()}')  # Desse jeito não aparece
print(f'num.sort(reverse=True): {num.sort(reverse=True)}')  # Nem desse
print(num)  # aqui aparece o último comando do sort()
num.sort()  # Restabele a ordem crescente
print(num)
print(f'Essa lista tem {len(num)} elemetos.')

# Inserir valores:
num.insert(2, 0)  # o 0 na posição 2
print(num)

# Excluindo valores
num.pop()  # Tira o último valor
num.pop(1)  # Tira o valor da posição 1
print(f'Apos retirar o valor da última posição e o da primeira: ')
print(num)
num.insert(0, 2)
num.append(3)  # Adiciona no fim da lista
num.insert(3, 2)
print(num)
print(f'Usando o num.remove(f): ', end='')
num.remove(2)  # Se pedir para remover um número que não exite, vai dar erro
print(num)
print('Só retira o primeiro valor 2 que aparece.')
print('\nÉ possível remover um número')
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5.')
print(num)

print('\nComeçando uma nova lista vazia:')
valores = []  # ou valores = lista()

valores.append(2)
valores.append(3)
valores.append(8)
valores.append(5)

for v in valores:
    print(f'{v}...', end='')
print('\n\nAnother for:')

for c, v in enumerate(valores):
    print(f'Na {c+1}ª posição  tem o valor {v}.')

print('\nCriando uma lista com entrada de valores:')
val = list()
for a in range(0, 5):
    val.append(int(input('Digite um valor: ')))

for c, v in enumerate(val):
    print(f'Na posição {c} tem o valor {v}')

a = [2, 5, 6, 3]
b = a  # Essa função faz uma ligação entre as 2 listas
b[2] = 1  # Essa alteração vai acontecer na lista A e B
c = a[:]  # Desse jeito eu crio uma copia e não faço ligação
print(f'Lista A: {a}')
print(f'Lista B: {b}')
