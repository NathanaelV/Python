# Class Challenge 13

# Fazer uma tabuada.
print('Fazendo Tabuada!')
t = int(input('Deseja saber a tabuada de qual número? '))
m = int(input('Multiplicando até qual número? '))
print('-' * 15)
for a in range(1, m+1):
    print('{} X {:>2} = {}'.format(t, a, a * t))
print('-' * 15)
