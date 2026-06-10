"""
Criacao e uso de decoradores, em cima (comentada) utiliazano a funcao decoradora como parametro
em baixo, deixando mais facil visivelmente, mas o efeito do decorador é o mesmo

"""


#def meu_decorador(funcao):
    #def envelope():
        #print("Faz algo antes de executar a funcao")
        #funcao()
        #print("Faz algo após executar a funcao")
    #return envelope
#
#def ola_mundo():
    #print("Ola Mundo!")
#
#ola_mundo = meu_decorador(ola_mundo)
#ola_mundo()


def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a funcao")
        funcao()
        print("Faz algo após executar a funcao")
    return envelope

@meu_decorador # nome da funcao decoradora
def ola_mundo():
    print("Ola Mundo!")


ola_mundo()