class Frame:
    """
        Classe estática que contem todos os frames utilizados no game.
    """
    Dinossauro = {'correndo': ['dino/dino-frame01.png', 'dino/dino-frame02.png'], 'abaixado': ['dino/dino-abaixado-frame01.png', 'dino/dino-abaixado-frame02.png'] }
    Dinossauro_parado = 'dino/dino-parado.png'
    Ground = 'background/chao.png'
    Passaro =  ["dino/Bird2.png", "dino/Bird1.png"]
    Cacto = ['cacto/LargeCactus1.png', 'cacto/LargeCactus2.png', 'cacto/LargeCactus3.png', 'cacto/SmallCactus1.png', 'cacto/SmallCactus2.png', 'cacto/SmallCactus3.png']
    Nuvem = 'background/Cloud.png'

class Contador:
    """
        Classe que vai realizar a contagem de frames do jogo
    """
    def __init__(self, maximo: int) -> None:
        self._maximo = maximo
        self._contador = 0

    def incrementa(self) -> None:
        self._contador += 1
        if self._contador == self._maximo:
            self._contador = 0
    
    def esta_zerado(self) -> bool:
        return self._contador == 0

class Animacao():
    """
        Classe que vai realizar a seleção dos frames que serão animados
    """
    def __init__(self, intervalo: int) -> None:
        self._arquivos: list[str] = []
        self._contador = Contador(intervalo)
        self._indice = 0
    
    def definir_frame(self, arquivos: list[str]) -> str:
        self._arquivos = arquivos
        self._contador.incrementa()
        if self._contador.esta_zerado():
            self._indice = (self._indice + 1) % len(self._arquivos)
            return self._arquivos[self._indice]
        return self._arquivos[self._indice]
        
