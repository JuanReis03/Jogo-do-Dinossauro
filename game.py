from obstaculo import *
from personagem import Personagem
from background import GroundBase, Nuvem
from tupy import BaseImage, keyboard, Label
from animacao import Contador
from status import Status
import random

class Game(BaseImage):
    """
        Classe que vai conter e gerenciar as classes do jogo.
    """
    MENSAGEM_INICIAR = "Pressione espaço para começar o jogo"
    MENSAGEM_GAMEOVER = "GAME OVER \nAperte espaço para começar novamente"
    PERIODO_MINIMO_SPAWN = 25
    PERIODO_MAXIMO_SPAWN = 45

    def __init__(self) -> None:
        self._hide()
        self.ground = GroundBase()
        self.nuvem = Nuvem()
        self.personagem = Personagem()
        self._contador = Contador(5)
        self.pontuacao = 0
        self.recorde = 0
        self.label_mensagem_iniciar = Label(Game.MENSAGEM_INICIAR, 440, 260, anchor='center')
        self.label_mensagem_gameover = Label(Game.MENSAGEM_GAMEOVER, 440, 260, anchor='center')
        self.mensagem_pontuacao = Label(f'Pontos: {self.pontuacao}', 20, 20)
        self.mensagem_recorde = Label(f'Recorde: {self.recorde}', 20, 50)
        self.gameover = False
        self.obstaculos: list[Obstaculo] = []
        self.velocidade_obstaculos = 20
        self.label_mensagem_gameover._hide()

    def set_obstaculo(self) -> None:
        if (self.deve_spawnar_obstaculo()):
            obstaculo_escolhido  = random.choice([Passaro, Cacto])
            obstaculo_escolhido.velocidade = self.velocidade_obstaculos
            self.obstaculos.append(obstaculo_escolhido())

    def set_recorde(self) -> None            :
        if (self.pontuacao > self.recorde):
            self.recorde = self.pontuacao
            self.mensagem_recorde.text = f'Recorde: {self.recorde}'    

    def deve_spawnar_obstaculo(self) -> bool:
        if self._contador.esta_zerado():
            deve_spawnar = random.choice([True, False])
            self._contador = Contador(random.randint(Game.PERIODO_MINIMO_SPAWN, Game.PERIODO_MAXIMO_SPAWN))
            self._contador.incrementa()
            return deve_spawnar
        else:
            self._contador.incrementa()
            return False

    def update(self) -> None:
        if (self.gameover):
            if (keyboard.is_key_just_down('space')):
                self.reiniciar() 
            return
        
        if (not Status.executando and keyboard.is_key_just_down('space')):
            self.label_mensagem_iniciar._hide()
            self.iniciar() 
              
        if (Status.executando):
            self.set_obstaculo()
            
            self.velocidade_obstaculos = min(20 + self.pontuacao // 5, 500)
            
            self.pontuacao += 1
            self.mensagem_pontuacao.text = f'Pontos: {self.pontuacao}' 

            for obstaculo in self.obstaculos:
                if (isinstance(obstaculo, Obstaculo) and self.personagem._collides_with(obstaculo)):
                    self.game_over()       
                
    def game_over(self) -> None:
        Status.executando = False
        self.gameover = True
        self.label_mensagem_gameover._show()
        self.set_recorde()       

    def iniciar(self) -> None:
        self.gameover = False
        self.ground.animar()
        self.pontuacao = 0
        Status.executando = True
            
    def reiniciar(self):
        self.personagem.destroy()

        for obstaculo in self.obstaculos:
            if (isinstance(obstaculo, Obstaculo)):
                obstaculo.reset()
        self.obstaculos.clear()

        self.label_mensagem_gameover._hide()
        self.gameover = False
        self.personagem = Personagem()
        self.iniciar()
        
  

