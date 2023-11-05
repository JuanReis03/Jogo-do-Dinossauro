from personagem import Personagem
from tupy import BaseImage, toast, keyboard, Label

mensagemIniciar = "Pressione espaço para começar o jogo"

class Frame:
    DinossauroCorrendo = ['dino/dino-frame01.png', 'dino/dino-frame02.png']
    DinossauroParado = 'dino/dino-parado.png'

class Status():
    executando = False
    
class Game(BaseImage):
    def __init__(self):
        self._hide()
        self.personagem = Personagem(Frame.DinossauroParado, 80, 440)
        self.mensagemIniciar = Label(mensagemIniciar, 200, 200)

    def update(self):
        if not Status.executando and keyboard.is_key_just_down('space'):
            self.mensagemIniciar._hide()
            self.iniciar()

    def iniciar(self):
        Status.executando = True
        self.personagem.animar(Frame.DinossauroCorrendo)

