"""
Funções
Bloco de código identificado por um nome e pode receber uma lista de parâmetros,
esses parametros podem ou nao ter valores padroes.

Torna o código mais legível e possibilita o reaproveitamento do codigo (pro
gramar de maneira estruturada)

palavra reservada -def

para retornar um valor, utilizamos a palavra reservada -> return
Toda funcao Python retorna none por padrao.
Em Python, uma funcao pode retornar mais de um valor

Argumentos nomeados -> são passados atraves de chave-valor

Args e kwargs
Podemos combinar parâmetros obrigatórios com args e kwargs. QUando esses são definidos
(*args e **kwargs), o método recebe os valores como tupla e dicionario respectivamente
"""

#exemplo de função

def exibir_mensagem():
    print("Hello World!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônomo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2("Aruan")
exibir_mensagem_3()
exibir_mensagem_3(nome="Pedro")

#exemplo do uso do return

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero+1
    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))

#Argumentos nomeados
print(f"\nArgumentos nomeados")

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no BD...
    print(f"Carro da marca {marca}, modelo {modelo} do ano {ano} e placa {placa} foi inserido com sucesso!")


salvar_carro("Fiat","Palio","1999","ABC-1234") #sem referencia, passado por ordem
salvar_carro(marca="Fiat",modelo="Palio",ano="1999",placa="ABC-1234") #com referencia

salvar_carro(**{"marca":"Fiat","modelo":"Palio","ano":"1999","placa":"ABC-1234"}) #passa como referencia um dicionario qwue converte nas referencias

##Args e kwargs
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args) #pegamos todas as strings e concatenamos com \n
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Araraqura, 25 de Janeiro de 2026Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
