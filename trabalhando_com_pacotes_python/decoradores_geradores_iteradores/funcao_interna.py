def principal():
    print("executando a funcao principal")

    def funcao_interna1():
        print("executando a funcao interna 1")

    def funcao_interna2():
        print("executando a funcao interna 2")
    
    funcao_interna2()
    funcao_interna1()

principal() # executo a funcao principal, dentro dela existem as 2 funcoes que sao chamadas dentro dela.
            #As funcoes internas só existem dentro da funcao principal, nao podendo serem chamadas de outro modo
