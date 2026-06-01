"""
Desafio:
Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar 
em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados
em uma variável e exibidos na operação de extrato.

Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será 
possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e 
exibidos na operação de extrato.

Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

"""
menu = """
-----------------Banco do Macena-----------------

        Digite:

        d- Depositos
        s- Saques
        e- Extratos
        q- sair

-----------------Seja bem vindo!-----------------
-------------------------------------------------
"""

SAQUE_DIARIO = 2
LIMITE_POR_SAQUE = 500
saque_dia = 0
saldo = 0
saldo_inicial = 0
deposito =[]

saque=[]




while True:
    funcao=input(menu)
    
    if funcao == 'd':
        
        valor_deposito = float(input("digite o valor a depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Foi depositado {valor_deposito} na sua conta e o saldo atual é de {saldo:.2f}")
            deposito.append(valor_deposito)

        else:
            print("Este não é um valor que possa ser depositado, voce sera enviado novamente ao menu")
            
            
    elif funcao == 's':
        
        valor_saque = float(input("digite o calor a sacar"))
        if valor_saque > 0 and valor_saque <= LIMITE_POR_SAQUE and saque_dia <= SAQUE_DIARIO and valor_saque<=saldo:
            saldo -= valor_saque
            saque_dia = saque_dia+1
            print(f"Retire seu dinheiro abaixo, foi sacado um total de R${valor_saque}, seu saldo é de{saldo:.2f}")
            saque.append(valor_saque)

        else:
            print("impossível sacar no momento")

    elif funcao == 'e':
        if deposito or saque :
            i=0 #variavel auxiliar depositos
            j=0 #variavel auxiliar saques
            for x in deposito:
                i=i+1
                print(f"deposito {i} no valor de R${x:.2f}")
                    
            for x in saque:
            
                j=j+1
                print(f"saque {j} no valor de R${x:.2f}")
            print(f"\n\ndsaldo atual de: {saldo:.2f}\n ------------------------------")
        else:
            print("não foram realizadas movimentações")
        
    elif funcao == "q":
        print("Volte sempre, estamos a disposição")
        break


    else:
        print("insira o numero corretamente ou *q* para sair")
    