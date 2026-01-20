"""
Strings de multiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Podem ocupar várias 
linhas de códigos,e  todo espaco em branco sao incluidos na string final

"""
nome = "Aruan"

mensagem = f'''
    Olá, meu nome é {nome}, 
                     Eu estou aprendendo Python
            Essa mensagem tem diferentes recuos
'''
print(mensagem)

#criando um menu

menu = """
    +++++++++++++++++++++MENU+++++++++++++++++++++
    
    1. SACAR 
    2. DEPOSITAR 
    
    0. SAIR 
    
    +++++++Obrigado por usar nosso sistema!+++++++

"""
print(menu)