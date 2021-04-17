# Class Challenge 13

# Ler uma frase e verificar se é um Palindromo
# Palindromo: Frase que quando lida de frente para traz e de traz para frente
# Serão a mesma coisa
# Ex.: Apos a sopa; a sacada da casa; a torre da derrota; o lobo ama o bolo;
# Anotaram a data da maratona.
# Desconsiderar os espaços e acentos. Programa tira os espaços

print('Descobrindo se a frase é um Palindromo.')
frase = str(input('Digite uma frase: ')).strip().upper()
array = frase.split()
junto = ''.join(array)
n = len(junto)
s = 0
for a in range(1, n+1):
    if junto[a-1] != junto[n-a]:
        s += 1
if s == 0:
    print('A frase é um Palindromo.')
else:
    print('A frase não é um Palindromo')

# Exemplo do professor
print('\nExemplo do professor: ')
palavras = frase.split()
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('Não temos um Palindromo')

# 3ª Alternativa como o Python
inverso2 = junto[::-1]
# Frase junto, do começo ao fim, porém de traz para frente
# Por isso o -1
print(inverso2)
