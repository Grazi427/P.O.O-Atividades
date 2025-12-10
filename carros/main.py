from carro import Carro
from carro_esportivo import CarroEsportivo
from carro_inteligente import CarroInteligente
from carro_corrida import CarroCorrida

def teste_drive(carro):
    print(f'\nTesteando {carro.__class__.__name__}:')
    carro.acelerar()
    carro.exibe_velocidade()

if __name__=='__main__':
    carro_inteligente = CarroInteligente(10)
    print('Carro Inteligente')
    carro_inteligente.estacionar()
    teste_drive(carro_inteligente)


    carro_esportivo = CarroEsportivo(50)
    print( 'Carro esportivo')
    carro_esportivo.turbo()
    teste_drive(carro_esportivo)


    carro_corrida = CarroCorrida(100)
    teste_drive(carro_corrida)

