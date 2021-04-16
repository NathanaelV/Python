# Class Challenge 12
# Ler o ano de nascimento e idicar a categoria da criança
# até 9: Mirim
# Até 14: Infantil
# Até 19: Junior
# Até 20: Sênior
# Acima: Master

from datetime import date
nascimento = int(input('Qual o ano de nascimento: '))
sexo = str(input('Menino ou menina? ')).strip()
if sexo.lower() == 'menino':
    sexo = 'Ele'
else:
    sexo = 'Ela'

idade = date.today().year - nascimento

if idade <= 9:
    print('{} está na categoria Mirim, pois {} tem {} anos'.format(sexo, sexo.lower(), idade))
elif idade <= 14:
    print('{} está na cantegoria Infantil, pois {} tem {} anos'.format(sexo, sexo.lower(), idade))
elif idade <= 19:
    print('{} está na categoria Junior, pois {} tem {} anos'.format(sexo, sexo.lower(), idade))
elif idade <= 20:
    print('{} está na categoria Sênior, pois {} tem {} anos'.format(sexo, sexo.lower(), idade))
else:
    print('{} está na categoria Master, pois {} tem {} anos'.format(sexo, sexo.lower(), idade))

# Exemplo do professor
print('\nExemplo do professor:')

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('CATEGORIA: Mirim')
elif idade <= 14:
    print('CATEGORIA: Infantil')
elif idade <= 19:
    print('CATEGORIA: Junior')
elif idade <= 20:
    print('CATEGORIA: Senior')
else:
    print('CATEGORIA: Master')
