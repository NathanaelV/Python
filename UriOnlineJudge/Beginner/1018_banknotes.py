# Esse código deu erro
# Presentation error (100%)

N = int(input())
if 0 < N < 1000000:
    print(N)
    n100 = N // 100
    N = N - n100 * 100
    print('{} nota (s) de R$ 100,00'.format(n100))
    n50 = N // 50
    N = N - n50 * 50
    print('{} nota (s) de R$ 50,00'.format(n50))
    n20 = N // 20
    N = N - n20 * 20
    print('{} nota (s) de R$ 20,00'.format(n20))
    n10 = N // 10
    N = N - n10 * 10
    print('{} nota (s) de R$ 10,00'.format(n10))
    n5 = N // 5
    N = N - n5 * 5
    print('{} nota (s) de R$ 5,00'.format(n5))
    n2 = N // 2
    N = N - n2 * 2
    print('{} nota (s) de R$ 2,00'.format(n2))
    print('{} nota (s) de R$ 1,00'.format(N))
