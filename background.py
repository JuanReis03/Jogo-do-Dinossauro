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

s1 = Sky('background/fundo.png', 500, 260, 4)
s2 = Sky('background/fundo.png', 1500, 260, 4)
# a velocidade que o céu se move é continua todo o jogo

g1 = Ground('background/chao.png', 850, 510, 8)
g2 = Ground('background/chao.png', -160, 510, 8)
# a velocidade do chão aumenta gradualmente, quanto mais pontos o jogador fizer, mais ela aumenta
