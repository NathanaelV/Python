# Class Challenge 09

# Digite uma frase qualquer. Deve mostrar quantas letras "A".
# Em qual posição aparece na 1ª Vez e na última vez

frase = str(input('Digite uma frase: ')).upper().strip()
f = frase.lower()
print('A frase tem {} letras a.'.format(frase.lower().count('a')))
print('A primeira letra a aparce na posição {} e a última na posição {}'.format(f.find('a'), f))

# Exemplo do professor:

print('\nExemplo do Professor:\n')

print('A frase tem {} letras a.'.format(frase.lower().count('a')))
print('A primeira letra a aparece na {}ª posição'.format(frase.lower().find('a')+1))
print('E a ultima na {}ª posição.'.format(frase.lower().rfind('a')+1))
# Com o rfind() a procura começa pelo lado direito
