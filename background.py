from tupy import *
from animacao import Frame
from status import Status

class GroundBase():
    def __init__(self):
        self.ground = Ground(850, 510)
        self.ground2 = Ground(-160, 510)

    def animar(self):
        self.ground.animar()
        self.ground2.animar()

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
    
    def __init__(self, x = 90, y = 440) -> None:
        self.x = x 
        self.y = y
        self.velocidade = 12
        self.file = Frame.Nuvem
    
    def update(self) -> None:
        if (Status.executando):
            self.x -= self.velocidade
            if (self._x <= -50):
                self._destroy()
                Nuvem(920, 200)
            