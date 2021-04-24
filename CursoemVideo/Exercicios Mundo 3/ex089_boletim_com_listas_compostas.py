# Class Challenge 18

# Make a list with names and within each name a list of 2 notes.
# Show each student's grade and average.
# Show individual student grades that the user wants to know.

'''
group = list()
names = list()
note = list()

while True:
    print('-' * 30)
    names.append(str(input('Enter a student name: ')))
    note.append(float(input('Enter first student note: ')))
    note.append(float(input('Enter second student note: ')))

    names.append(note[:])
    note.clear()
    group.append(names[:])
    names.clear()

    resp = ' '
    while resp not in 'YyNn':
        resp = str(input('Do you want to continue? [Y/N] ')).strip()[0]
    if resp in 'Nn':
        break

numero = 0
print('=' * 30)
print(f'{"Nº"} {"NOME":<15}{"MÉDIA"}')
for n, p in enumerate(group):
    n1 = p[1][0]
    n2 = p[1][1]
    m = (n1 + n2)/2
    numero = n
    print(f'{n}  {p[0]:<15}{m:.2f} ')

while True:
    print('-' * 50)
    print("Do you want to see which student's grades?")
    resp = int(input("Enter a student Nº: (Enter 999 to exit) "))
    if 0 <= resp <= numero:
        # print('-' * 50)
        print(f'Student {group[resp][0]} has grades: {group[resp][1]}')
    elif resp == 999:
        break
    else:
        print('-' * 50)
        print(f'Enter a valid Number: 0 to {numero}')
'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 35)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    npc = int(input('Mostra notas de qual aluno? (999 para sair): '))
    if npc == 999:
        print('FINALISANDO...')
        break
    if npc <= len(ficha)-1:
        print(f'Notas de {ficha[npc][0]} são {ficha[npc][1]}')
print('<<< VOLTE SEMPRE >>>')
