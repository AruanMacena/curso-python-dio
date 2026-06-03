from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero,agencia,cliente,historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    
    def saldo(self):
        pass

    def sacar(self):
        pass

    def depositar(self):
        pass

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(0,numero,"0001",cliente,[])


#a = Conta.nova_conta("Aruan",1)

#print(f"nome:{a._cliente}, nuemro da conta:{a._numero}, agencia: {a._agencia}, saldo:{a._saldo}, historico:{a._historico}")

class Conta_corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite=100,limite_saques=4):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques



class Cliente:
    def __init__(self,endereco,contas=[]):
        self._endereco = endereco
        self._contas = contas
    
    def adicionar_conta(self):
        pass

    def realizar_transacao(self):
        pass

class Pessoa_Fisica(Cliente):
    def __init__(self,endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Transacao(ABC):

    @abstractmethod
    def registrar(self):
        pass

class Deposito:
    def depositar(self, valor):
        pass #verificar condicoes para deposito e operacao de deposito

class Saque:
    def sacar(self):
        pass #condicoes de saque e operacoes de saque

class Historico:
    def adicionar_transacao(self):
        pass