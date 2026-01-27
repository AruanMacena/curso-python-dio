"""
Desafio DIO

Otimizando o sistema Bancário com funcões Python
DESCRIÇÃO
Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido
com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, 
implementando as operações de depósito, saque e extrato em funções específicas. Você terá a 
chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a 
manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados 
de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando 
Python.

A funcao saque deve receber os argumentos apenas por nome (keyworld only)

A funcao deposito deve receber os argumentos apenas por posicao(positional only)

A funcao extrato deve receber os argumentos por posicao e nome (positional only and keyworld only)

Novas funçoes -> criar usuario e criar conta corrente

Criar usuario -> deve armazenar usuários em uma lista. Um usuario é composto por: nome, DN, cpf e 
endereco. O endereço é uma string com formato: logradouro,nro - bairro -cidade/sigla estado. 
Deve ser armazenado somente os numeros do cpf. Nao podemos cadastrar 2 usuarios com o mesmo cpf

Criar conta corrente -> O programa deve armazenar contas em uma lista, uma conta é composta por 
agencia, numero da conta e usuário. O numero da conta é sequencial, iniciando em 1. O numero da 
agencia é fixo: "0001". O usuario pode ter mais de uma conta, mas uma conta pertence a somente 
um usuario.

Dice: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF 
informado para cada usuário da lista

"""
def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(limite,saldo,extrato,numero_saques,LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato,numero_saques

def extrato_conta(saldo, /,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")    


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

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(saldo,extrato)      

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo=saldo,extrato=extrato,limite=limite,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES)
        

    elif opcao == "e":
        extrato_conta(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")