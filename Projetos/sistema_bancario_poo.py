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
    clientes = [] #lista que armazena os objetos clientes (pessoa fisica)
    contas = [] # lista que armazena os objetos do tipo conta

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

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

"""Funcoes, onde as interacoes entre objetos ocorrerão"""

def filtrar_cliente(cpf,clientes):
    clientes_filtrados = []
    for cliente in clientes:
        if cliente._cpf == cpf:
            clientes_filtrados.append(cliente)
            if clientes_filtrados:
                return clientes_filtrados[0] if clientes_filtrados else None

def criar_clientes(clientes):
    cpf = input("Digite o cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)

    if cliente:
        print("Ja existe cliente cadastrado com este CPF")
        return
    
    nome = input("Digite o nome do cliente")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço : ")

    cliente = Pessoa_Fisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("Cliente nao encontrado \n Retorno ao menu principal")
        return
    
    conta = Conta_corrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta) #adiciona a conta a lista geral
    cliente._contas.append(conta) #adiciona a conta ao cliente (cliente acessa o objeto._contas acessa o parametro contas do cliente que é uma lista)

    print("Conta criada com sucesso! \n Voltando ao menu principal")

def listar_contas(contas):
    for conta in contas:
        print("+" * 30)
        print(textwrap.dedent(str(conta)))

def recuperar_conta_cliente(cliente):
    if not cliente._contas:
        print("Cliente não possui contas nesta ilustre instituição")
        return

    print('\n*******Contas disponíveis: *******\n')
    for i, conta in enumerate(cliente._contas, start=1):
        print(f"[{i}]  |  {conta}")
        print("-------------------------")

    numero = int(input("Informe o numero relacionado a conta desejada: "))

    if numero <1 or numero> len(cliente._contas):
        print("Opcao inválida")
        return
    
    return cliente._contas[numero-1]

def depositar(clientes):
    cpf = input ("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor=valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado! \n")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico._transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['Tipo']}:\n\tR$ {transacao['Valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

main()