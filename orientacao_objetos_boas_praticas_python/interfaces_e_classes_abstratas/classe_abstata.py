from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    
    @abstractmethod #define a obrigatoriedade de implementar este metodo na classe filha
    def ligar(self):
        pass

    @abstractmethod #define a obrigatoriedade de implementar este metodo na classe filha
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv!")
        print("TV Ligada")

    def desligar(self):
        print("desligando a tv")
        print("TV desligada")
    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar condicionado")
        print("Ar condicionado Ligado")

    def desligar(self):
        print("desligando o Ar condicionado")
        print("Ar condicionado desligado")

    @property
    def marca(self):
        return "Samsung"

controletv = ControleTV()
controletv.ligar()
controletv.desligar()

controlear = ControleArCondicionado()
controlear.ligar()
controlear.desligar()

print()
print(controletv.marca)