#definicao de classe em Python
class Bicicleta:
    def __init__(self,cor,modelo,ano,valor): #self representa a instancia do objeto, init (método construtor)
        self.cor = cor #atributos da classe
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    #métodos são como funcoes dentro das classes
    def buzinar(self):
        print("Plim Plim...!")
    
    def parar(self):
        print("parando a Bicicleta")
        print("bicicleta parada")

    def correr(self):
        print("Vrummmmmmm...!")


#criando objeto
b1 = Bicicleta("vermelha","caloi",2022,600)

#utilizando os métodos da classe
b1.buzinar() #Plim Plim...!
b1.correr()#Vrummmmmmm...!
b1.parar()#parando a Bicicleta bicicleta parada

#acessar atributos
print(b1.cor, b1.modelo,b1.ano,b1.valor) #vermelha caloi 2022 600

b2 = Bicicleta("verde","Monark",2000,189)

Bicicleta.buzinar(b2)