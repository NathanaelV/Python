# Class Challenge 19

# Read name and media of several students
# Show whether the student has failed or passed

student = dict()
na = str(input('Enter the student name: '))
m = float(input('Enter the student media: '))
student['name'] = na
student['media'] = m
if m >= 7:
    student['Situation'] = 'Aprovado'
elif 5 <= m < 7:
    student['Situation'] = 'Recuperação'
else:
    student['Situation'] = 'Reprovado'
print('-=' * 30)
for v, i in student.items():
    print(f' - {v.capitalize()} es equal a {i}')

# Teacher Example:

print('\nTeacher Example:')

aluno = dict()
aluno['Nome'] = str(input('NOme: '))
aluno['media'] = float(input(f'Media do {aluno["nome"]}'))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in student.items():
    print(f'  - {k} é igual {v}')
