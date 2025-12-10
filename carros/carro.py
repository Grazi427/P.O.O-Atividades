class Carro:
    def __init__(self, velocidade_inicial):
        self.velocidade = velocidade_inicial

    def acelerar(self):
        self.velocidade += 1

    def freiar(self):
        self.velocidade -= 1

    def exibe_velocidade(self):
        print(f'Velocidade atual: {self.velocidade} km/h')