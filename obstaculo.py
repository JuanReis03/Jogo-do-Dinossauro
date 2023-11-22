from status import Status
from tupy import BaseImage

class Obstaculo(BaseImage):
    posicao_inicial_x = 920
    posicao_inicial_y = 440
    
    def __init__(self, deve_spawnar = False):
        self._x = Obstaculo.posicao_inicial_x
        self._y = Obstaculo.posicao_inicial_y
        self.velocidade = 20
        self.deve_spawnar = deve_spawnar

    def update(self) -> None:
        if (Status.executando):
            if (self.deve_spawnar):
                self._x -= self.velocidade
                if (self._x <= -20):
                    self.deve_spawnar = False
                    self._x = Obstaculo.posicao_inicial_x
                    # self._destroy()
