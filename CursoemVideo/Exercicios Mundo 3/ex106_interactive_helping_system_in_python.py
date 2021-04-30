# Class Challenge 21

# Mini sistema que utilize o Interactive Help do Python
# Usuário vai digitar COMANDO e o manual vai aparecer
# Quando o usuario digitar FIM o programa se ENCERRA.
# OBS: Use CORES


def titles(txt):
    print('\033[30;46m', end='')
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))
    print('\033[m', end='')


def ajuda():
    from time import sleep
    while True:
        resp = str(input('\033[35mType a command or library? (Enter FIM to exit) \033[m'))
        if resp.upper() == 'FIM':
            print('Exit', end='')
            for p in range(0, 3):
                print(end='.')
                sleep(0.5)
            print('  <<< THANKS! CHECK BACK OFTEN! >>>')
            break
        else:
            titles(f'Searching for the "{resp}" Command Manual')
            sleep(1)
            print('\033[30;42m')
            help(resp)
            sleep(1)
            print('\033[m')


# Principal program:
titles('System PyHELP')
ajuda()


# Teacher Example:
print('\nTeacher Example')

c = ('\033[m',         # 0 - Sem cor
     '\033[30;41m',    # 1 - Vermelho
     '\033[30;42m',    # 2 - Verde
     '\033[30;43m',    # 3 - Amarelo
     '\033[30;44m',    # 4 - Azul
     '\033[30;45m',    # 5 - Roxo
     '\033[30;46m',    # 6 - Siano
     '\033[7;30;41m')  # 7 - Branco


def comando(com):
    # Não está reconhecendo os comandos em volta
    titulo(f"Acessando o manual do comando '{com}'", 2)
    help(com)


def titulo(msg, cor=0):
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyTHON', cor=1)
    resposta = str(input('Função ou Biblioteca > '))
    if resposta.upper() == 'FIM':
        break
    else:
        print(c[7], end='')
        help(resposta)
        print(c[0], end='')
titulo('ATÉ LOGO!', 6)
