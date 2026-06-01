class Conta:
    def __init__(self, nro_agencia, saldo=0,):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    
    
    
conta = Conta("0001",100)

# conta._saldo += 100 #driblando o encapsulamento, python permite isso, pois nao existe variaveis/metodos realmente globais
#ideal seria utilizar metodo de deposito
conta.depositar(100)
print(conta._saldo)

conta.sacar(50)
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())