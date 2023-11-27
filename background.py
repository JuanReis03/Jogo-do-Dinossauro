from tupy import *
from animacao import Frame
from status import Status

class GroundBase():
    """
        Classe que gerencia a animação do background
    """

    def __init__(self) -> None:
        self.ground = Ground(850, 510)
        self.ground2 = Ground(-160, 510)

    def animar(self) -> None:
        self.ground.animar()
        self.ground2.animar()

class Ground(BaseImage):
    def __init__(self, x: int, y: int) -> None:
        self._file = Frame.Ground
        self._x = x 
        self._y = y
        self._velocidade = 8
        self._hide()
        
    def update(self) -> None:
        if(Status.executando):
            if (self._x - self._velocidade) < -505:
                self._x = 1560
            else:
                self._x -= self._velocidade

    def animar(self) -> None:
        self._velocidade = 8         
        self._show()
        

class Nuvem(BaseImage):
    """
        Classe que gerencia a animação da nuvem
    """
    def __init__(self, x: int = 90, y: int = 440) -> None:
        self._x = x 
        self._y = y
        self._velocidade = 12
        self._file = Frame.Nuvem
    
    def update(self) -> None:
        if (Status.executando):
            self._x -= self._velocidade
            if (self._x <= -50):
                self._destroy()
                Nuvem(920, 200)
            