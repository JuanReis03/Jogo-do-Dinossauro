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

