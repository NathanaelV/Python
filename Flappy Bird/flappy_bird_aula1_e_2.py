# Aula 1

# NEAT: Neural Evolution Augmenting Topology
# O passaro é uma rede neural, ele vai recer Inputs vai reagir com Output

# Input; São as informações que o passaro vai receber
# Output: Como o passaro vai reagir de acordo com os Inputs. Devo pensar no que eu faria se estivesse jogando

# Input:
# Preciso saber a altura do passáro e a altura dele em relação ao cano de cime e o de baixo

# Output:
# Decide se o passaro pula ou não.

# Entrada de informações:
# pega a altura dele: 30
# Posição dele para o cano de cima: 4
# Posição para o cano de baixo: -7

# Com essas medidas o programa vai aplicar um peso para cada um:
# Ex.: 30*0.5 + 4*2 + (-7)*1.3 = 13.9
# O NEAT faz essas contas por baixo dos panos
# Ele pegara esse resultado e somará a um número aleatório (bias)
# Vai calcular uma FUNÇÃO de ATIVAÇÃO.
# Para evitar que o número vá de valores absurdos negativos e positivos.
# Colocamos dentro de uma tangente hiperbolica: varia de (-1; 1)

# Tomada de decisão:
# Referência para o pássaro agir ou não (Pular)
# Assim determino um número, acima desse valor, o passáro pula.

# Os valoers que multiplicam a altura e o bias são determinados pelo pc e escolhidos aleatóriamente
# Quando o jogo começa, o programa roda vários passaros e com isso vai aprendendo

# Ele vai pegar os passáros que chegaram mais longe e vai criar uma nova geração
# A segunda será clona com os ultimos 2 passáros.
# Porém terá uma pequena alteração:
# Da segunda geração ele vai pegar os que foram mais longes e criar uma terceira geração


# O que é essa mudança:
# Haverá mudança nos pesos, no bias e talvez até a criação de uma nova camada de cálculo
# Novamente, pegará os melhores e replicaram


# 1º PASSO: Criar o jogo como se eu fosse jogar:
# 2º PASSO: Passar os parãmentros para regular a IA
# 3º PASSO: Colocar a IA para jogar

import pygame
import os  # Permite acessar arquivos do pc e trazer para o Python. Como as imagens
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

# Pelo arquivo estar em outra pasta preciso usar o OS
# scale2x: Serve para almentar a imagem 2 vezes
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('Imagem', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('Imagem', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('Imagem', 'bg.png')))
IMAGENS_PASSAROS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('Imagem', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('Imagem', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('Imagem', 'bird3.png')))
]

# Usar uma fonte para marcar a pontuação
# Iniciar a fonte
pygame.font.init()

# Escolher a fonte e o tamanho
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


# Criar os objetos do jogo
# Pensar no que existe e as coisas que se mexem no jogo
# O fundo não se movimenta
# MOVE: O pássaro, Cano e o chão
# O pássaro só se mexe no eixo Y
# O chão e os canos só se mexem no eixo X
# Os objetos são os que se mexem


# Cada objeto será uma classe: Terei que criar uma para cada objeto
# Para cada classe devo pensar nos Atributos, as informações:


# Pássaro:

# Posição no eixo x, eixo y, altura
# Velocidade que sobe e dece,
# Ângulo, qual a cara do pássaro, qual das 3

# Método:
# Desenhar na tela,
# Movimenta para cima e para baixo
# Pode Pular

# Cano:
# Posição da parte de baixo e da parte de cima
# Posição no eixo X
# A velocidade que se movimenta

# Traduzir isso para o programa: Atributos da classe e forma de métodos da classe


class Passaro:
    IMGS = IMAGENS_PASSAROS
    # animações da rotação: Para não ter mudanças bruscas entre as 3 imagens do pássaro
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    # Atributos do pássaro: Informações
    # Posição nos eixos X e Y
    # Altura, Velocidade

    # Dentro dos ():
    # Informações o passaro recebe quando é criado
    # Onde ele vai aparecer
    def __init__(self, x, y):  # Função que cria o pássaro
        self.x = x  # Caracteristica de X
        self.y = y  # Caracteristica de Y
        self.angulo = 0  # Ângulo que ele começa
        self.velocidade = 0  # Velocidade que ele começa
        # Só tem velocidade para cima e para baixo
        self.altura = self.y  # A altura do pássaro é a posição dele no eixo y

        # Parâmetros auxiliares:
        self.tempo = 0  # Para ajudar na animação. Fazer a parabola do pássaro caindo
        # Importante para não ter uma movimentação muito reta
        self.contagem_imagem = 0  # Saber qual imagem estou usando, 1, 2 ou 3.
        self.imagem = IMGS[0]  # Imagem que começa


    # Criar a função PULAR:
    # Da esquerda para direita o X aumenta
    # De CIMA para BAIXO o Y AUMENTA
    # Para subir o Y diminui, descer o Y aumenta


    def pular(self):
        self.velocidade = -10.5  # Para pular para cima. Y aumenta para baixo
        self.tempo = 0  # Para o cálculo da parabola
        self.altura = self.y


    # Função par amovimentar o pássaro:
    def mover(self):
        # Calcular o deslocamento
        self.tempo += 1  # Execultar essa funão a cada freme
        deslocamento = 1.5*(self.tempo**2) + self.velocidade + self.tempo
        # Fórmula Sorvetão: S = So + Vot + at²/2
        # 1.5 Valor empírico. Movimentação do pássaro: Aceleração

        # Restringir o deslocamento:
        # O pássaro não vai acelerar infinitamente para cima e nem para baixo
        if deslocamento > 16:  # Restrige o deslocamento em 16 Pixels
            deslocamento = 16
        elif deslocamento < 0:  # Da um incremento no salto, um ganho extra.
            deslocamento -= 2  # Sem isso o salto fica muito pequeno

        self.y += deslocamento  # Para o Pás se mexer

        # Ângulo do pássaro:
        # Quando pula vira para cima
        # Quando cai vira para baixo
        if deslocamento < 0 or self.y < (self.altura + 50):  # Comando para manter o Pás virado para cima
                    # Enquanto estiver acima da posição que saltou, o Pás permanecerá virado para cima






class Cano:
    pass


class Chao:
    pass



