from obstaculo import Obstaculo
from personagem import Personagem
from status import Status
from background import Ground
from tupy import BaseImage, keyboard, Label
from animacao import Contador
import random

class Game(BaseImage):
    mensagemIniciar = "Pressione espaço para começar o jogo"

    def __init__(self):
        self._hide()
        self.ground = Ground(850, 510)
        self.ground2 = Ground(-160, 510)
        self.personagem = Personagem()
        self.mensagemIniciar = Label(Game.mensagemIniciar, 200, 200)
        self.obstaculo = Obstaculo()
        self._contador = Contador(5)
        self.pontuacao = 0
        self.recorde = 0
        self.mensagemPontuacao = Label(f'Pontos: {self.pontuacao}', 20, 20)
        self.mensagemRecorde = Label(f'Recorde: self.recorde', 20, 50)

    def update(self):
        if (not Status.executando and keyboard.is_key_just_down('space')):
            self.mensagemIniciar._hide()
            self.iniciar()
            

        if (Status.executando):
            if (self.deve_spawnar_obstaculo()):
                self.obstaculo.deve_spawnar = True
                # self.obstaculo = random.choice([Passaro(True), Cacto(True)])
            self.pontuacao += 1
            self.mensagemPontuacao.text = f'Pontos: {self.pontuacao}'
            
            if self.pontuacao > self.recorde:
                self.recorde = self.pontuacao
                self.mensagemRecorde.text = f'Recorde: {self.recorde}'

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

