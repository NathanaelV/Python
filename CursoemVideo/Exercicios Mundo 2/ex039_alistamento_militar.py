# Class Challenge 12
# Entrar com o ano de nascimento e calcular a idade e devolver:
# Informar quanto tempo falta falta para se alistar no exército,
# Se é o ano ou se já passou, quanto tempo passou.
from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - nascimento
if idade < 18:
    tempo = 18 - idade
    print('Faltam {} anos para o seu alistamento no exército'.format(tempo))
    print('Seu alistamento será em {}'.format(nascimento + 18))
elif idade > 18:
    tempo = idade - 18
    print('O ano do seu alistamento no exército foi há {} anos, em {}'.format(tempo, nascimento + 18))
else:
    print('Esse é o ano do seu alistamento no exército, não esqueça os documentos.')

# Exemplo do professor: Muito semelhante
