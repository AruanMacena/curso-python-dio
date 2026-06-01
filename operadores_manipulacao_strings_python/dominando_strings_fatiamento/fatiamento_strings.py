"""
Fatiamento de strings - > Tecnica utilizada para retornar substrings indicando inicio, fim e passo [start:stop:[step]]
Utilizamos como referencia o índice


"""
nome = "Aruan da Silva Macena"

print(nome[0]) #Inclui somente o caracter na posicao 0

print(nome[:9]) #Pega a partir do 0 até o caracter 8 (o 9 é exclusivo)

print(nome[10:]) #Pega a partir do caracter 10 e vai ate o fim

print(nome[10:13]) #retorna só o pedaco entre o caracter 10 até o 13 (exclusivo)

print(nome[2:7:2]) #Retorna a partir do caracter 2 até o 7, pulando de 2 em 2

print(nome[:]) #retorna a string inteira

print(nome[::-1]) # cria uma cópia espelhada da string