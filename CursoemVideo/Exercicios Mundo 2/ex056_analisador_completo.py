# Class Challenge 13

# Ler Nome, idade e sexo de 4 pessoas. E Mostrar
# A média das idades, nome do homem mais velho,
# Quantas mulheres com menos de 20 anos

'''

i = 0  # Para o cálculo da somatória das idades
n = 0  # Para saber o nome do mais velho
f = 0  # Contar o número de mulheres com menos de 20 anos
nomevelho = 'João'

for c in range(0, 4):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sex = str(input('Digite o sexo [F/M]: ')).strip().upper()
    i += idade
    if sex == 'M' and idade > n:
        nomevelho = nome
        n = idade
    if sex == 'F' and idade < 20:
        f += 1

print('\nA média das idades é {:.0f}.'.format(i/4))
print('O homem mais velho é o {}.'.format(nomevelho))
print('O grupo tem {} mulher(es) com menos de 20 anos.'.format(f))

'''

# Exemplo do Professor:

print('\nExemplo do Professor:')
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).strip()
    idade = int(input('Idade: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        nomevelho = nome
        maioridadehomem = idade
    if sexo in 'Mm' and idade > maioridadehomem:
        nomevelho = nome
        maioridadehomem = idade
    if sexo in 'Ff' and idade < 20:
            totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(mediaidade))
print('O Homem mais velho é o {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
