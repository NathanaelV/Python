# Challenge 022 - 027

# Python armazena os carcteres de uma string, as letras de uma frase, separadamente

# Python conta os espaços e a contagem começa com 0
# Para exibir um caracter específico só especificar entre []


    # Fatiamento


frase = 'Curso em Vídeo Python'
print('\nFATIAMENTO!\n')
print('frase[9]:', frase[9])
print('frase[13]:', frase[13])
print('frase[9:13]:', frase[9:13])  # Do 9 ao 13, sem incluir o 13

# Caso eu queira incluir até o final da frase se inclui um número a mais do que
# foi contado. Se a contagem acabar em 20 coloco [9:21] assim aparece tudo

print('frase[9:21:2]:', frase[9:21:2])  # Vai do 9 ao 21 pulando de 2 em 2
print('frase[:5]:', frase[:5])  # Começa no 0 e vai até o 4, pois exclui o 5
print('frase[15:]:', frase[15:])  # Começa no 15 e vai até o último
print('frase[9::3]:', frase[9::3])  # Começa no 9 e vai até o final pulando de 3 em 3


    # Analise


print('\nANALISE!\n')
# fução length

print('Sentence Length. len(frase): ', len(frase))
# Quantos carcteres tem na palavra, incluindo so espaços
# Caso use com uma lista, mostrará quantos componentes tem o Array

o = frase.count('o')  # Conta quantas vezes o letra 'o' minusculo aparece na frase
# Python diferencia maiúsculo de minúsculo

print('Quantas vezes a letra  o  aparece na frase: ', format(o))

print('Quantas veses a letra o aparece até o carcater 13:', end=' ')
print(frase.count('o', 0, 13))  # Quantas vezes a letra 'o' aparece na frase
# Até o caracter 13, sem contar o 13, contagem com fatiamento

print('Apartir de que carcter aparece o trecho deo:', end=' ')
print(frase.find('deo'))  # Indica onde começa os caracteres procurados, 'deo'

print('Encontrar a palavra Android: ', end='')
print(frase.find('Android'))  # Se pedir para localizar uma palavra que não existe
# na String, será retornado um valor: -1

print('A palavra Curso está na frase?: ', 'Curso' in frase)
# para saber se a palavra Curso existe na frase
# Responde True or False

print('Prucurar vídeo, v minúsculo: ', frase.find('vídeo'))
print('Usando comando lower: ', frase.lower().find('vídeo'))


    #Transformação


print('\nTRANSFORMAÇÃO!\n')

print('frase.replace(Python,android): ', frase.replace('Python', 'Android'))
# Troca a primeira palavra pela segunda.
# Não precisa ter o mesmo tamanho. o Python adapta
# Não é possível atribuir outroa valor a String. O adroid só aparece no lugar
# de Python na impressão, mas na memoria ainda é Python
# Para conseguir mudar é necessário usar outro comando

frase = frase.replace('Python', 'Android')
print('O Valor da Str frase foi alterada: {}'.format(frase))

frase.upper()  # Coloca todas as letras em maiúscula

frase.lower()  # Transforma tudo em minúsculo

frase.capitalize()  # Joga tudo para minusculo e depois só coloca a primeira letra maiúscula

frase.title()  # Transforma todas as letras depois dos espaços em Maiúsculo

# Funções para remover os espaços no começo da frase
# Acontece da pessoa dar alguns espaços antes de começar a digitar

frase2 = '    Aprenda Python    '

frase2.strip()  # Remove os espaços antes da primeira letra e os que vem depois
# Da ultima letra

frase2.rstrip()  # Só Remove os espaços do lado direito Right, por causa do r

frase2.lstrip()  # Só Remove os espços do lado esquerdo left, por causa do l


    # Divisão


print('\nDIVISÃO E JUNSÃO\n')

print('Comando frase.split(): \n', frase.split())
# Cria uma divisão onde existir espaços. Criando uma nova lista
separada = frase.split()
print(separada[0])  # Mostra o primeiro intem da lista
print(separada[0][2])  # No primeiro intem da lista, vai mostrar a 3ª letra
print(len(separada))  # Mostra a quantidade de elementos na lista

print('Join: ')
print('-'.join(frase))  # Junta as palvras divididas usado o que tiver entre ''.
# Nesse caso teria - entre as palavras, pois fiz '-'.join(frase)

# Para escrever um texto grande usa-se:
print("""Texto     
muito 
Grande
com 
Enter""")  # O texto é impresso incluindo os Enter

print('\nTexto '                # Desse jeito o python pula linhas aqui
      'pequeno com aspas '      # Mas na hora de colocar na tela 
      'simples e enter')        # Sai tudo em uma só linha

# Combinação de funções:
print('Quntos O maiúsculos tem na frase: ')
print(frase.count('O'))
print('E agora? Usando função upper():')
print(frase.upper().count('O'))

# Espaço também conta como carcter
frase3 = '    Curso em Video Python    '  # Não aparece os espaços na impressão
print('Frase com espaços: {}.\nQuantidade: {}'.format(frase, len(frase3)))
print('Com corte de espaços: {}'.format(len(frase3.strip())))


