"""
Permitem o desvio de fluxo de controle quando determinadas expressões lógicas são atendidas

if(palavra reservada)- estrutura condicional composta por um unico desvio. O comando ira testar a expressão lógica e em caso de
retorno verdadeiro as açoes presentes no bloco de código do if serão executadas

if/else (palavras reservadas) - se a estrucao logica do of for verdadeira ela executara. caso contrario, 
o que esta na identacao do "else" sera realizado

if/elif/else -elif eh composto por uma nova expressão logica, garantindo vários casos abrangidos na estrutura

if aninhados - podemos ter estruturas condicionais aninhadas (dentro do bloco de identacao)

if ternário - permite escreverr uma condicao em uma unica linha. 3 partes (retorno se V, expressao, retorno se F)

"""
#IF/ELSE
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = 17

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")

else:
    print("ainda não pode tirar cnh")

#IF/ELSE/ELIF
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")

elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não as práticas")

else:
    print("ainda não pode tirar cnh")

#IF aninhados

conta_normal=True
conta_universitaria = False

saldo=2000
saque = 2500
cheque_especial = 450


if conta_normal:
    if saldo>=saque:
        print("saque realizado com sucesso")
    elif saque<=(saldo+cheque_especial):
        print("saque realizado com uso do cheque especial")
    else:
        print("saldo insuficiente")
elif conta_universitaria:
    if saldo>=saque:
        print("saque realizado com sucesso")
    else:
        print("saldo insuficiente")

else:
    print("sistema nao reconheceu seu tipo de conta! Entre em contato com a agência")

#IF ternário

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")