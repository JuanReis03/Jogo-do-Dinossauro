from tupy import BaseImage, BaseTupyObject

class Frame:
    Dinossauro = { 'parado': 'dino/dino-parado.png', 'correndo': ['dino/dino-frame01.png', 'dino/dino-frame02.png'] }
    Ground = 'background/chao.png'

class Contador:
    def __init__(self, maximo):
        self._maximo = maximo
        self._contador = 0

    def incrementa(self):
        self._contador += 1
        if self._contador == self._maximo:
            self._contador = 0
    
    def esta_zerado(self):
        return self._contador == 0

class Animacao():
    def __init__(self, arquivos, intervalo):
        self._arquivos = arquivos
        self._contador = Contador(intervalo)
        self._indice = 0
    
    def definir_frame(self) -> str:
        self._contador.incrementa()
        if self._contador.esta_zerado():
            self._indice = (self._indice + 1) % len(self._arquivos)
            return self._arquivos[self._indice]
        return self._arquivos[self._indice]
        
