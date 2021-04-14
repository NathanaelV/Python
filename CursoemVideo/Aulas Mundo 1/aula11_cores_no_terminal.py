# ANSI escape sequence
# Esse são comandos do padrão ANSI
# Tudo dentro de ANSI começa com contra barra ' \ '
# Cores boas para usar no Pyton, tem o código \033
# \033[style; text; backm
# style: estilo da fonte
    # 0: None (nenhum)
    # 1: Bold (negrito)
    # 4: Underline (sublinhado)
    # 7: Negative (O que era fundo vira letra e letra vira fundo)
# text: cor do texto
    # 30 (branco), 31 (vermelho), 32 (verde), 33 (amarelo)
    # 34 (azul), 35 (magenta), 36 (siano), 37 (cinza)
# back: Cor do fundo
    # 40 (branco), 41 (vermelho), 42 (verde), 43 (amarelo)
    # 44 (azul), 45 (magenta), 46 (siano), 47 (cinza)

print('\033[1mMudando a Fonte!', '\n')
print('\033[1;31mParte Teorica:\n')
print('\033[1;30;41mTesto [1;30;41m')

# para a barra não ir até o final, só tirar o comando
print('\033[4;33;44mTesto [4;33;44m \033[m')
print('\033[1;35;43mTesto [1;35;43m \033[m')
print('\033[30;42mTesto [30;42m')
print('\033[mTesto [m')  # Usa o padrão do terminal e desfaz qualquer coisa
print('\033[7;30mTesto [7;30m \033[m')
print('\033[4;30;45mHello, world! \033[m')

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'amarelo': '\033[33m'}

a = 4
b = 6
print('Os valores são \033[1;31m{}\033[m e \033[1;34m{}\033[m. Tenha um bom dia'.format(a, b))
nome = 'Guanabara'
print('\nOlá, muito prazer em te conhecer {}{}{}. '
      'Tenha um bom dia'.format(cores['amarelo'], nome, cores['limpa']))
