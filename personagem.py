from animacao import Animacao
from tupy import BaseImage, keyboard

class Personagem(BaseImage):
    def animar(self, frame):
        self._hide()
        Animacao(frame, 4)
