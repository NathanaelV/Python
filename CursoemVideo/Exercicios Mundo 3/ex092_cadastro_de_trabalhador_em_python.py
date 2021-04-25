# Class Challenge 19

# Ler nome, data de nascimento e carteira de trabalho
# Guardar a nome, idade e carteira de trabalho
# Carteira de Trabalho de Previdencia Social (CTPS)
# Se a CTPS for diferente de zero:
#    Receber o ano de contratação e o sálario da pessoa
# Calcular com quantos anos a pessoa vai se aposentar
#    Aposentadoria depois de 35 anos de contribuição
# Mostrar nome, idade, ctps, ano de contratação, salário, aposentadoria

from datetime import date

worker = dict()
worker['Name'] = str(input('Name: '))
birth = int(input('Year of birth: '))
worker['Age'] = date.today().year - birth
worker['CTPS'] = int(input("CTPS: (Enter 0 if you don't have) "))
if worker['CTPS'] != 0:
    worker['Hiring'] = int(input('When do you start to work? '))
    worker['Wage'] = float(input('How much do you wage? R$ '))
    worker['Retirement'] = worker['Age'] + 35 - (date.today().year - worker['Hiring'])

print('-=' * 15)
print(f"{'YOUR DATA':^30}")
print('-=' * 15)
for k, v in worker.items():
    print(f'{k} has the value {v}')
print('-' * 30)
print('Have a Nice Day!')

# Teacher Example:
# Teacher example is similar:
