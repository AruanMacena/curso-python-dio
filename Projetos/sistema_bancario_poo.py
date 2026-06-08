from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

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

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["Tipo"]==Saque.__name__]

        )

        excedeu_limite = valor>self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("Falha! Valor de saque maior que limite disponível por saque")
        
        elif excedeu_saques:
            print(f"Numero maximo de saques foi superado ao de {self._limite_saques}")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t {self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self._cliente._nome}
        """

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

    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:


    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
                "Data": datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

            }
        )

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova conta
    [l]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extratos(clientes)

        elif opcao == "n":
            numero_conta = len(contas) +1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "nu":
            criar_clientes(clientes)
        
        elif opcao == "q":
            break

        else:
            print(
                """
                Opção inválida, digite a operação desejada
                """

            )

main()