# Class Challenge 21

# função notas(): Recebe informações de vários alunos e retorna um dicionário:
#    - Quantidade de notas
#    - A maior nota
#    - A menor nota
#    - A média da turma
#    - A situação (Opcional) media < 5: RUIM; 5 <= media < 7: RAZOAVEL; media => 7: BOA
# Adicionar as docstrings da função


def note(*notes, show=False):
    """
    -> Function to receive several notes and return a dictionary with the total number of numbers inserted, highest and
    lowest value, arithmetic mean and the situation of the class
    :param notes: receives several numbers
    :param show: (optional) To show the situation of the class. Average < 5: Bad, 5 <= Average < 7: Reasonable;
    Average >= 7: Good
    :return: A dictionary with Total, Highest, Lowest, Average (Optional: Situation)
    """
    student = dict()
    largest = 0
    smallest = 0
    s = 0
    for n, c in enumerate(notes):
        if n == 0:
            largest = c
            smallest = c
        else:
            if c > largest:
                largest = c
            if c < smallest:
                smallest = c
        s += c
    student['Total'] = len(notes)
    student['Highest'] = largest
    student['Lowest'] = smallest
    student['Average'] = s / len(notes)
    if show:
        if student['Average'] >= 7:
            student['Situation'] = 'Good'
        elif student['Average'] >= 5:
            student['Situation'] = 'Reasonable'
        else:
            student['Situation'] = 'Bad'
    return student


# Principal program
stud = note(4.5, 6, 8, 9, 10, 9, 3, 8, show=False)
print(stud)
print('\nCLASS INFO:')
print('-' * 30)
for k, v in stud.items():
    print(f'{k}: {v}')


# Teacher Example:

print('\nTeacher Example: ')


def notas(*n, sit=False):
    """
    -> Função para analisar as notas e situação de vários alunos
    :param n: Uma ou mais notas de alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionáro com várias informações sobre a situação da turma
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r
