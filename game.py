from obstaculo import *
from personagem import Personagem
from background import *
from tupy import BaseImage, keyboard, Label
from animacao import Contador
from status import Status
import random

class Game(BaseImage):
    mensagem_iniciar = "Pressione espaço para começar o jogo"
    mensagem_gameover = "GAME OVER \nAperte espaço para começar novamente"
    periodo_minimo_spawn = 25
    periodo_maximo_spawn = 45

    def __init__(self):
        self._hide()
        self.ground = Ground(850, 510)
        self.ground2 = Ground(-160, 510)
        self.nuvem = Nuvem(90, 440)
        self.personagem = Personagem()
        self._contador = Contador(5)
        self.pontuacao = 0
        self.recorde = 0
        self.mensagem_iniciar = Label(Game.mensagem_iniciar, 440, 260, anchor='center')
        self.mensagem_pontuacao = Label(f'Pontos: {self.pontuacao}', 20, 20)
        self.mensagem_recorde = Label(f'Recorde: {self.recorde}', 20, 50)
        self.gameover = False
        self.obstaculos = [Obstaculo]
        self.velocidade_obstaculos = 20
        self.periodo_minimo_spawn = 35
        self.periodo_maximo_spawn = 50

    def set_obstaculo(self):
        if (self.deve_spawnar_obstaculo()):
            obstaculo_escolhido  = random.choice([Passaro, Cacto])
            obstaculo_escolhido.velocidade = self.velocidade_obstaculos
            self.obstaculos.append(obstaculo_escolhido())

    def set_recorde(self)            :
        if (self.pontuacao > self.recorde):
            self.recorde = self.pontuacao
            self.mensagem_recorde.text = f'Recorde: {self.recorde}'    

    def update(self):
        if (self.gameover):
            if (keyboard.is_key_just_down('space')):
                self.reiniciar() 
            return
        
        if (not Status.executando and keyboard.is_key_just_down('space')):
            self.mensagem_iniciar._hide()
            self.iniciar() 
              
        if (Status.executando):
            self.set_obstaculo()
            
            self.velocidade_obstaculos = min(20 + self.pontuacao // 5, 500)
            
            self.pontuacao += 1
            self.mensagem_pontuacao.text = f'Pontos: {self.pontuacao}' 

            for obstaculo in self.obstaculos:
                if (isinstance(obstaculo, Obstaculo) and self.personagem._collides_with(obstaculo)):
                    self.game_over()       
                
    def game_over(self):
        self.mensagem_gameover = Label(Game.mensagem_gameover, 440, 260, anchor='center')
        Status.executando = False
        self.gameover = True
        self.set_recorde()       

    def deve_spawnar_obstaculo(self):
        if self._contador.esta_zerado():
            deve_spawnar = random.choice([True, False])
            self._contador = Contador(random.randint(Game.periodo_minimo_spawn, Game.periodo_maximo_spawn))
            self._contador.incrementa()
            return deve_spawnar
        else:
            self._contador.incrementa()
            return False

    def iniciar(self):
        self.gameover = False
        self.ground.animar()
        self.ground2.animar()
        self.pontuacao = 0
        Status.executando = True
            
    def reiniciar(self):
        self.personagem.destroy()

        for obstaculo in self.obstaculos:
            if (isinstance(obstaculo, Obstaculo)):
                obstaculo.reset()
        self.obstaculos.clear()

        self.mensagem_gameover._hide()
        self.gameover = False
        self.personagem = Personagem()
        self.iniciar()
        
  

