from personagem import Personagem
from status import Status
from background import Ground
from tupy import BaseImage, keyboard, Label

class Game(BaseImage):
    mensagemIniciar = "Pressione espaço para começar o jogo"

    def __init__(self):
        self._hide()
        self.ground = Ground(850, 510)
        self.ground2 = Ground(-160, 510)
        self.personagem = Personagem()
        self.mensagemIniciar = Label(Game.mensagemIniciar, 200, 200)

    def update(self):
        if (not Status.executando and keyboard.is_key_just_down('space')):
            self.mensagemIniciar._hide()
            self.iniciar()

    def iniciar(self):
        Status.executando = True
        self.ground.animar()
        self.ground2.animar()

