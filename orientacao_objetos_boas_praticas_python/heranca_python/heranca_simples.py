class Veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave,valor in self.__dict__.items()])}'


class Motocileta(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):

    def __init__(self,cor, placa, numero_rodas, carregado=False):
        super().__init__(cor, placa,numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        if self.carregado == False:
            print('nao estou carregado')
        else:
            print('esta carregado')

moto = Motocileta('prata','BUJ-0190',2)
carro = Carro('branco', "xxd-0923", 4)
caminhao = Caminhao("roxo", "abd-0234", 6)

print(moto)
print(carro)
print(caminhao)

