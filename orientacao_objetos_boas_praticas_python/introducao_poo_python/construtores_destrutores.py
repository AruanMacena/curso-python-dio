class Cachorro:
    def __init__(self, nome, cor, acordado=True): #construtor
        print('inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def falar(self):
        print("Auau!")

    def __del__(self): #destrutor
        print('Removendo a instancia da classe')


def criar_cachorro():
    c = Cachorro("Zeus", 'branco e preto', False)
    print (c.nome)

#c=Cachorro("Chappie", "amarelo")
#c.falar()

criar_cachorro()