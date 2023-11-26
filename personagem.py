from animacao import Animacao, Frame
from tupy import BaseImage, keyboard
from status import Status

class Personagem(BaseImage):
    posicao_inicial_x = 80
    posicao_inicial_y = 440

    def __init__(self):
        self._file = Frame.Dinossauro['parado']
        self._x = Personagem.posicao_inicial_x
        self._y = Personagem.posicao_inicial_y
        self._pulando = False
        self._caindo = False
        self._animacao = Animacao(Frame.Dinossauro['correndo'], 2)
        self._altura_pulo = Personagem.posicao_inicial_y - 100
        
    def update(self) -> None:
        if Status.executando:
            if not self._pulando and not self._caindo:
                self._file = self._animacao.definir_frame()
                if keyboard.is_key_just_down('space'):
                    self._pulando = True
                    self._velocidade_y = -40 # Ajuste a velocidade conforme necessário

            if self._pulando or self._caindo:
                self._y += self._velocidade_y
                self._velocidade_y += 5  # Adiciona a aceleração devido à gravidade

            if self._y >= Personagem.posicao_inicial_y:
                self._y = Personagem.posicao_inicial_y
                if self._pulando:
                    self._pulando = False
                    self._caindo = True
                    self._velocidade_y = 0  # Reseta a velocidade ao começar a cair

            if self._caindo and self._y <= Personagem.posicao_inicial_y:
                self._y = Personagem.posicao_inicial_y
                self._caindo = False
                self._velocidade_y = 0
            

        
