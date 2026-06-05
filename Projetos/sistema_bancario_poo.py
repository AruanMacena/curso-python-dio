from abc import ABC, abstractmethod

class Conta:
    def __init__(self, numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f"Operação falhou! Saldo insuficiente na conta {self.__class__.__name__}")
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado!")
            return True
        
        else:
            print("Valor informado inválido")
        return False

    def depositar(self,valor):
        
        if valor>0:
            self._saldo += valor
            print("Depositado com sucesso!")
            return True
        else:
            print("Falha ao depositar")
            return False

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente,)


class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=100,limite_saques=4):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques



class Cliente:
    def __init__(self,endereco):
        self._endereco = endereco
        self._contas = [] #inicializacao do cliente sem contas (vazio)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
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