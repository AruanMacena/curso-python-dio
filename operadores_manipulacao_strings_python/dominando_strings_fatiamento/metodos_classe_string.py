"""
Classe string->varios métodos


"""
curso = "    PyTHoN    "

print(curso.upper()) #tudo maiuscula

print(curso.lower()) # tud minuscula

print(curso.title()) # só a primeira letra em maiuscula e as demais em minusculas

print(curso.strip()) #remove todos os espaços em branco

print(curso.rstrip()) #remove os espaços da direita em branco

print(curso.lstrip()) #remove os espaços da esquerdaem branco

curso = "Python"

print(curso.center(10,"#")) # (numero de caracteres que ira ocupar, opcional, caracter que voce quer colocar no espaço m branco)

print(".".join(curso))  #passa item a item, separando pelo caractere que voce colocou no Join
                        #util e comum em listas, mas da para fazer com strings tmb

