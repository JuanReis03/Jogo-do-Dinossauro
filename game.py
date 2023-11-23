from obstaculo import *
from personagem import Personagem
from background import Ground
from tupy import BaseImage, keyboard, Label
from animacao import Contador
from status import Status
import random

class Game(BaseImage):
    mensagem_iniciar = "Pressione espaço para começar o jogo"
    mensagem_gameover = "GAME OVER"

    def __init__(self):
        self._hide()
        self.ground = Ground(850, 510)
        self.ground2 = Ground(-160, 510)
        self.personagem = Personagem()
        self.mensagem_iniciar = Label(Game.mensagem_iniciar, 440, 260, anchor='center')
        self.obstaculo = Obstaculo()
        self._contador = Contador(5)
        self.pontuacao = 0
        self.recorde = 0
        self.mensagemPontuacao = Label(f'Pontos: {self.pontuacao}', 20, 20)
        self.mensagemRecorde = Label(f'Recorde: self.recorde', 20, 50)

    def update(self):
        if (not Status.executando and keyboard.is_key_just_down('space')):
            self.mensagem_iniciar._hide()
            self.iniciar()
            

        if (Status.executando):
            if (self.deve_spawnar_obstaculo()):
                self.obstaculo.deve_spawnar = True
                self.obstaculo = Cacto()

    def deve_spawnar_obstaculo(self):
        if self._contador.esta_zerado():
            deve_spawnar = random.choice([True, False])
            self._contador = Contador(random.randint(10, 50))
            self._contador.incrementa()
            return deve_spawnar
        else:
            self._contador.incrementa()
            return False

    def iniciar(self):
        Status.executando = True
        self.ground.animar()
        self.ground2.animar()
        if self.recorde == 0:
            self.mensagemRecorde.text = f'Recorde: {self.recorde}'
        if self.pontuacao > self.recorde:
            self.recorde = self.pontuacao
            self.mensagemRecorde.text = f'Recorde: {self.recorde}'

