# Class Challenge 16

# Montar uma tupla com muitas palavras, sem acento
# Mostra as palvras e quais são as vogais dessas palavras
# Na ordem em que aparecem e repetindo
# Ex.: CASA tem a a. PEDREIRO tem e e i 0
# Lista: APRENDER, PROGRAMAR, LINGUAGEM, PYTHON, CURSOS, GRATIS, ESTUDAR, PRATICAR
# TRABALHAR, MERCADO, PROGRAMADOR, FUTURO.

words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSOS', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
a = 'APRENDERA'
for w in words:
    print(f'The word {w} has the vowels: ', end=' ')
    if 'A' in w:
        print('{}'.format(w[w.index('A')]), end=' ')
    if 'E' in w:
        print('{}'.format(w[w.index('E')]), end=' ')
    if 'I' in w:
        print('{}'.format(w[w.index('I')]), end=' ')
    if 'O' in w:
        print('{}'.format(w[w.index('O')]), end=' ')
    if 'U' in w:
        print('{}'.format(w[w.index('U')]), end=' ')
    print('')
