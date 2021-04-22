# Class Challenge 17

# Digitar uma expressao matemática qualquer.
# Verificar se os parenteses que abrem se fecham, não pode faltar e nem ter a mais.
# Os parenteses devem ser abertos na ordem correta
# Usar em forma de lista.

expression = str(input('Enter a expression: '))
op = expression.count('(')
cl = expression.count(')')
print(f'Open: {op}, Closed: {cl}')
if op == cl:
    print('The expression is VALID.')
else:
    print('The expression is INVALID')
