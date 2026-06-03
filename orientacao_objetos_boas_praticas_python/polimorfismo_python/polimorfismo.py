class Passaro:
    def voar(self):
        print("voando...")

    
class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao pode voar")


def plano_voo(obj): #todo os objetos que eu recebo no plano de voo, tem que ter o voar implementado
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)