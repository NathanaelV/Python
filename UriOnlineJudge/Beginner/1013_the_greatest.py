a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
M = (a + b + abs(a - b)) / 2
R = (c + M + abs(c - M)) / 2
print('{} eh o maior'.format(int(R)))
