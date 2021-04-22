# Class Challenge 17

# Digitar uma expressao matemática qualquer.
# Verificar se os parenteses que abrem se fecham, não pode faltar e nem ter a mais.
# Os parenteses devem ser abertos na ordem correta
# Usar em forma de lista.

expression = str(input('Enter a expression: '))
op = expression.count('(')
cl = expression.count(')')
i = 0
for a in expression:
    if a == '(':
        i += 1
    if a == ')':
        i -= 1
    if i < 0 or op != cl:
        print('The Expression is INVALID!')
        break
if i == 0:
    print('The Expression is VALID!')

# Teacher example:

print('\nTeacher Example:')
pilha = []
for simb in expression:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão está válida.')
else:
    print('Sua expressão está inválida.')
