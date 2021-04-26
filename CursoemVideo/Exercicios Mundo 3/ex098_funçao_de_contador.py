# Class Challenge 20

# função contador() recebe 3 valores
# Incio, fim e passo
# Deve ser realizado 3 contagens: de 1 até 10 de 1 em 1
# De 10 até 0 de 2 em 2; Uma contagem personalizada
from time import sleep

def contar(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Counting from {i} to {f} of {p} in {p}...')
    if i > f:
        f -= 1
    else:
        f += 1
    if i > f and p > 0:
        p *= -1
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.3)
    print('Fim!')


def div():
    print('-=' * 30)


div()
contar(1, 10, 1)
div()
contar(10, 0, 2)
div()
print("Now it's your turn to customize the count:")
start = int(input('Start: '))
end = int(input('End:   '))
step = int(input('Step:  '))

contar(start, end, step)

print('FIM!')
