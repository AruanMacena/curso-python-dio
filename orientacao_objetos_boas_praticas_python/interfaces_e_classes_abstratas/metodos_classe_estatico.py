class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_a_partir_dn(cls, ano, mes, dia, nome): #aponta para a classe e não para uma instancia do objeto
        print(cls)
        
        idade = 2026-ano
        return cls(nome, idade)

    @staticmethod   #método estatico, nao precisa do contexto da classe
    def e_maior_idade(idade):
        return idade >= 18


p2=Pessoa.criar_a_partir_dn(1994,3,21,"Aruan") # classe.método de classe(parametros)
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))