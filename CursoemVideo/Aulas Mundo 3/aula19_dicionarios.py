# Challenge 90 - 95

# dados = dict()
# dados = {'nome':'Pedro', 'idade':25} nome é o identificador e Pedro é o valor
# idade é o identificador e 25 é a idade.

# Para criar um novo elemento
# dados['sexo'] = 'M'.  Ele cria o elemento sexo e adiciona ao dicionario

# Para apagar
# del dados['idade']

# print(dados.values()) Ele retornará - 'Pedro', 25, 'M'
# print(dados.keys()) It will return - 'nome', 'idade', 'sexo'
# print(dados.items()) it will return all things - 'name', 'Pedro' ...
# Esses conceitos são bons para laços, for, while

filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
for k, v in filme.items():
    print(f'O {k} é {v}')
print()
person = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 40}
print(f'{person["nome"]} is {person["idade"]} years old.')  # Não posso usar person[0] ele não reconhece
print(f'Using person.keys(): {person.keys()}')
print(f'Using person.values(): {person.values()}')
print(f'Using person.items(): {person.items()}')

# Using for:

print('\nUsing for:')
print('\nUsing For k in person.key: or For k in person:')
for k in person.keys():  # = to use person
    print(k)
print('\nUsing k in person.values():')
for k in person.values():
    print(k)
print('\nUsing k, v in person.items():')
for k, v in person.items():
    print(f'V = {v}; K = {k}')
del person['sexo']
print("\nAfter using del person['sexo']")
for k, v in person.items():
    print(f'V = {v}; K = {k}')

# Alterando e adicionando elementos:

print('\nChanging the name and adding weight.')
person['peso'] = 98.5
person['nome'] = 'Leandro'
for k, v in person.items():
    print(f'V = {v}; K = {k}')

# Criando um dicionário dentro de uma lista:

Brazil = list()
estado1 = {'UF': 'Rio Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
Brazil.append(estado1)
Brazil.append(estado2)
print(f'Brazil: {Brazil}')
print(f'Estado 2: {estado2}')
print(f'Brazil[0]: {Brazil[0]}')
print(f"Brazil[0]['uf']: {Brazil[0]['UF']}")
print(f"Brazil[1]['sigla']: {Brazil[1]['sigla']}")

# Introsuzindo Valores:

print('\nIntroduzindo Valores: ')
brasil = list()
estado = dict()
for a in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())  # Caso use o [:] dará erro.
for e in brasil:
    print(e['sigla'], ' = ', e['uf'])

# Mostra os identificadores e os valores
print('\nItems: ')
for e in brasil:
    for k, v in e.items():
        print(f'O compo {k} tem o valor {v}')

# Mostra os valore dentro da lista
print('\nValues:')
for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print()
