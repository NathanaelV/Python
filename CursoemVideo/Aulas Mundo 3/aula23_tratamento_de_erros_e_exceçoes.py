# Challenge 113 - 115(a, b, c)

# Erros que normalmente funcionariam, não são erros, mas exeções.
# Como um print(x) sem inicializar a variavel. Não há problemas no print, mas x não tinha sido identificada
# NameError: Erro de significado, erro de semantica
# Quando tem entrada de string quando pede-se um int ou float
# ValueError: Erro de valor
# ZeroDivisionError: divisão por zero
# TypeError: operações matematicas com string. Ex.: a = 4 / '2' (O primeiro é int, o segundo str)
# IndexError: pedir para exibir um valor que não existe na lista.
# lst=[3,4,5] print(lst[3]), não há o 3º elemento. Correto seria lst[2] = 5
# KeyError: Quando acontece o mesmo com dicionarios
# ModuleNotFoundError: Quando não encontra-se um Modulo/biblioteca

try:
    a = int(input('1º N: '))
    b = int(input('2º N: '))
    r = a / b
# Caso não aconteça o que eu espero
# Com o Exception posso especificar o erro.
except Exception as erro:
    print('Tivemos um Problema:( ')
    print(f'O problema foi: {erro.__class__}')
else:  # Caso não aconteça o problema
    print(f'O resultado é {r:.2f}')
finally:  # Vai acontecer, idependente do que aconteça
    print('Volte sempre!')


# Exemplo com vários Except:

try:
    x = int(input('1º N: '))
    y = int(input('2º N: '))
    z = x / y
except (TypeError, ValueError):  # Para digirar dois preciso colocar entre ()
    print('Erro como o valor digitado. ')
except ZeroDivisionError:
    print('Não pode ter divisão por zero.')
except KeyboardInterrupt:
    print('Usuário não informou os dados.')
except Exception as erro2:
    print(f'O Erro foi : {erro2.__cause__}')
else:
    print(f'A divisão é: {z}')
finally:
    print('Volte Sempre Obrigado!')
