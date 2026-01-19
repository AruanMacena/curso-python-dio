"""
Aprender como o interpretador Python utiliza
identacao para delimitar blocos de comandos

Interpretador consegue determinar onde um 
bloco de comando inicia e onde ele termina

Utilizamos a tecla (tab) (4 valores em branco)

"""

def sacar(valor: float,saldo):
    saldo = saldo
    valor = valor

    if saldo >= valor:
        print('valor sacado!')
        print("retire o dinheiro no caixa")
        saldo -= valor
        

    print("Obrigado por ser cliente, tenha um bom dia!")    #sera mostrado no metodo,
    return saldo                                            #sempre sera mostrada na funcao

def depositar(valor:float,saldo):
    valor = valor
    saldo = saldo
    saldo+=valor
    return saldo

saldo = 500
saldo = sacar(100,saldo)
print(saldo)
saldo = depositar(1000,saldo)
print(saldo)