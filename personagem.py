from animacao import Animacao, Frame
from tupy import BaseImage, keyboard
from status import Status

class Personagem(BaseImage):
    POSICAO_INICIAL_X = 80
    POSICAO_INICIAL_Y = 440

    def __init__(self):
        self._file = Frame.Dinossauro['parado']
        self._x = Personagem.POSICAO_INICIAL_X
        self._y = Personagem.POSICAO_INICIAL_Y
        self._pulando = False
        self._caindo = False
        self._abaixado = False
        self._animacao = Animacao(2)
        self._altura_pulo = Personagem.POSICAO_INICIAL_Y - 100
        
    def update(self) -> None:
        if Status.executando:
            if not self._pulando and not self._caindo:
                
                if keyboard.is_key_down('Down'):       
                    self._file = self._animacao.definir_frame(Frame.Dinossauro['abaixado'])
                else:
                    print('correndo')
                    self._file = self._animacao.definir_frame(Frame.Dinossauro['correndo'])
                
                if keyboard.is_key_just_down('space'):
                    self._pulando = True
                    self._velocidade_y = -40 # Ajuste a velocidade conforme necessário

            if self._pulando or self._caindo:
                self._y += self._velocidade_y
                self._velocidade_y += 5  # Adiciona a aceleração devido à gravidade

            if self._y >= Personagem.POSICAO_INICIAL_Y:
                self._y = Personagem.POSICAO_INICIAL_Y
                if self._pulando:
                    self._pulando = False
                    self._caindo = True
                    self._velocidade_y = 0  # Reseta a velocidade ao começar a cair

            if self._caindo and self._y <= Personagem.POSICAO_INICIAL_Y:
                self._y = Personagem.POSICAO_INICIAL_Y
                self._caindo = False
                self._velocidade_y = 0
            

        
