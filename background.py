from tupy import *

class Sky(Image):
    def __init__(self, file, x, y, v):
        # v é a velocidade
        self.file = file
        self.x = x
        self.y = y
        self.v = v

    def update(self) -> None:
        if(self.x - self.v) < -500:
            self.x = 1450
        else: 
            self.x -= self.v
        
class Ground(Image):
    def __init__(self, file, x, y, v):
        self.file = file
        self.x = x 
        self.y = y 
        self.v = v
        
    def update(self) -> None:
        if (self.x - self.v) < -505:
            self.x = 1560
        else:
            self.x -= self.v
