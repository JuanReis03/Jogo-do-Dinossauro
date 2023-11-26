from tupy import *
from animacao import Frame
from status import Status

class Ground(Image):
    def __init__(self, x, y):
        self.file = Frame.Ground
        self.x = x 
        self.y = y 
        self.v = 8
        self._hide()
        
    def update(self) -> None:
        if(Status.executando):
            if (self.x - self.v) < -505:
                self.x = 1560
            else:
                self.x -= self.v

    def animar(self) -> None:
        self.v = 8         
        self._show()
        

class Nuvem(Image):
    posicao_incial_x=920
    posicao_incial_y=440
    
    def __init__(self) -> None:
        self._x: int = Nuvem.posicao_inicial_x
        self._y: int = Nuvem.posicao_inicial_y
        self.velocidade = 10
    def update(self) -> None:
        if (Status.executando):
            self._x -= self.velocidade
            if (self._x <= -50):
                self._destroy()
