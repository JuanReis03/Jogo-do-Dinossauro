from animacao import Animacao
from tupy import BaseImage, Image, keyboard
from status import Status

class Personagem(Image):
    def __init__(self, frame):
        self.file = frame
        self.x = 80
        self.y = 440
        self.pulando = False
        self.caindo = False

    def animar(self, frame):
        self._hide()
        self.animacao = Animacao(frame, 4)

    def update(self) -> None:
        if keyboard.is_key_just_down('space'):
            self.pulando = True
            print(self.pulando)
            print(self.y)
        if self.pulando and self.y >= 340: 
            self.animacao._hide()
            self._show()
            self.y -= 10
        elif self.pulando:
            self.pulando = False
            self.caindo = True
        if self.caindo and self.y <= 440:
            self.y += 10
        elif self.caindo:
            self._hide()
            self.animacao._show()
            self.caindo = False
            

        
