"""
Continuacao de funcoes

parâmetros especiais

def f(pos1, pos2, / , pos_or_kwd, *, kw1,kw2):
      ---------       ----------     -------
        |               |               |
        |    Positional or keyworld     |
        |                               -Keyworld only
        --Positional only


Objetos de primeira classe
Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe.
Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores 
em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).

Escopo local e escopo global
Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali 
feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais 
utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo 
local é global. Essa NÃO é uma boa prática e deve ser evitada.


"""

#exemplo

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido, 
#os parametros estao sendo passados por keyworld na parte em que eles obrigatoriamente sao passados por posicao

#keyworld only
def fazer_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

fazer_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #valido

#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

print()

#Funcao como objeto de primeira classe

def somar(a,b):
    return a+b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operacao {a} + {b} = {resultado}")

exibir_resultado(10,10,somar)

#escopo local e global

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))  # a variavel salario precisa ser puxada do escopo global para o local
