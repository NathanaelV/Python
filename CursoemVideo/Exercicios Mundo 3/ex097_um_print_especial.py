# Class Challenge 20

# função escreva() vai receber um texto
# Mostrar na tela com linhas em cima e embaixo com tamanho adaptavel

def escreva(msg):
    print('~' * (len(msg) + 6))
    print(f'   {msg.title()}')
    print('~' * (len(msg) + 6))


escreva('welcome to Jurassic Park')
escreva('Python')
escreva('Curso em video teach Python')

# Teacher Example:
# Teacher example is similar
