class Estudante:
    escola = "DIO" # atributo de classe, vai valer para todos os objetos criados

    def __init__(self, nome, matricula):
        self.nome = nome # atributos de instancia, cada objeto tem o seu
        self.matricula = matricula # atributos de instancia, cada objeto tem o seu

    def __str__(self):
        return f"escola: {self.escola},nome:{self.nome}, matrícula:{self.matricula}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)



e1 = Estudante('Aruan',1)
e2 = Estudante('Gui',2)
e3 = Estudante('Pipoka',3)

mostrar_valores(e1,e2,e3)

e1.matricula = 4
mostrar_valores(e1,e2,e3)

Estudante.escola = "Maria isabel"
mostrar_valores(e1,e2,e3)

e4 = Estudante('Denise',5)
print()
mostrar_valores(e1,e2,e3,e4)