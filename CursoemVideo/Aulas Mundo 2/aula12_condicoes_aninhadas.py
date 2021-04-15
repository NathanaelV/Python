# Challenge 036 - 045
# Programa a melhor impotese, mas deve-se ver outras alternativas
# else if = elif

nome = str(input('Digite seu nome: '))
if nome.lower() == 'gustavo':
    print('Que nome bonito.')
elif nome.lower() == 'pedro' or nome == 'maria' or nome == 'joão' or nome == 'paulo':
    print('Seu nome é popular no Brasil.')
elif nome.lower() in 'ana cláudia jéssica juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é normal.')
print('Muito prazer, {}!'.format(nome))
