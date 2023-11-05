from personagem import Personagem
from status import Status
from background import *
from tupy import BaseImage, keyboard, Label

mensagemIniciar = "Pressione espaço para começar o jogo"

class Frame:
    DinossauroCorrendo = ['dino/dino-frame01.png', 'dino/dino-frame02.png']
    DinossauroParado = 'dino/dino-parado.png'
    Sky = 'background/fundo.png'
    Ground = 'background/chao.png'

class Game(BaseImage):
    def __init__(self):
        self._hide()
        self.personagem = Personagem(Frame.DinossauroParado)
        self.mensagemIniciar = Label(mensagemIniciar, 200, 200)

    def update(self):
        if not Status.executando and keyboard.is_key_just_down('space'):
            self.mensagemIniciar._hide()
            self.iniciar()

    def iniciar(self):
        Status.executando = True
        Sky(Frame.Sky, 500, 260, 4)
        Sky(Frame.Sky, 1500, 260, 4)
        # a velocidade que o céu se move é continua todo o jogo

        Ground(Frame.Ground, 850, 510, 8)
        Ground(Frame.Ground, -160, 510, 8)
        # a velocidade do chão aumenta gradualmente, quanto mais pontos o jogador fizer, mais ela aumenta
        self.personagem.animar(Frame.DinossauroCorrendo)
        self.personagem.animar(Frame.DinossauroCorrendo)

