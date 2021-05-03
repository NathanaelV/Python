def leiadin(txt):
    res = str(input(txt)).strip().replace(',', '.')
    if res.isalpha() or res == '':
        print('Its not numeric')
    else:
        return float(res)
