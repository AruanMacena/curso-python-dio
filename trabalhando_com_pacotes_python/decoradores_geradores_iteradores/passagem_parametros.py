def mensagem(nome):
    print('executando mensagem\n\n')
    return f'Oi {nome}\n\n'

def mensagem_longa(nome):
    print("executando mensagem longa\n\n")
    return f'Ola, tudo bem com vc {nome}?\n'

def executar(funcao, nome):
    print("executando executar\n")
    return funcao(nome)


"""
Foram definidas 3 funcoes como exemplo
abaixo esta sendo chamada a funcao executar e como parâmetros dessa funcao
esta sendo apontado para outra funcao e um parametro que esta sendo utilizada
por esta segunda funcao.

"""

print(executar(mensagem,"Aruan"))   # 1- executa a funcao executar que retorna uma funcao. 
                                    #2- executa a afuncao mensagem que esta sendo passada como parâmetro 

print(executar(mensagem_longa,"Aruan"))