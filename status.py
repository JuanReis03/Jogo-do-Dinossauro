class Status():
    executando = False
    
    @classmethod
    def reset(cls):
        # Resetar o estado da classe Status
        cls.executando = False