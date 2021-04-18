# Class Challenge 14

# Ler um número n e mostrar os n primeiros números de Fibonacci
# 0, 1, 1, 2, 3, 5, 8...

n = int(input('Digite enéssimo número que deseja saber da sequencia de Fibonacci: '))
a1 = 0
a2 = 1
a3 = 1
i = 0
while i < n:
    print(a3, end=', ')
    a3 = a1 + a2
    a2 = a1
    a1 = a3
    i += 1
print('Fim!')
