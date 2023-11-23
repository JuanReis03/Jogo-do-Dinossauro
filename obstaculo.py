from status import Status
from tupy import BaseImage
import random
from animacao import Animacao, Frame

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
                if (self._x <= -50):
                    self._destroy()
                    self.deve_spawnar = False
                    
                    

class Passaro(Obstaculo):
    posicoes=[360,460,410]
    def __init__(self):
        super().__init__(True)
        self._y = random.choice(Passaro.posicoes)
        self._animacao = Animacao(Frame.Passaro, 2)
        self._file = self._animacao.definir_frame()
    
    def update(self) -> None:
        super().update()
        self._file = self._animacao.definir_frame()
        
        
            
        
        
   
        
        
        
                    
                   
    
    def reset(self):
        # Resetar propriedades do obstáculo
        self._x = Obstaculo.posicao_inicial_x
        self._y = Obstaculo.posicao_inicial_y
        self.velocidade = 20
        self.deve_spawnar = False
                    #self._x = Obstaculo.posicao_inicial_x
                    

class Cacto(Obstaculo):
    def __init__(self):
        super().__init__(True)
        self._file = random.choice(Frame.Cacto)
    #def update (self):
        #super().update()
        #self._destroy()
