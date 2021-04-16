# Class Challenge 13

# Mostrar todos os números PARES entre 1 e 50.
# Fazer também um exemplo usando o if else
for a in range(2, 51, 2):  # Essa é a melhor versão, usando apenas 25 laços
    print(a, end=' ')      # Usa menos o processador
print('\nFim\n')

print('Usando o if:')   # Essa versão usa mais o processador, pois faz um laço
for a in range(0, 51):  # Que sabemos que não vai gerar resultado.
    if a % 2 == 0:
        print(a, end=' ')
print('\nFim')
