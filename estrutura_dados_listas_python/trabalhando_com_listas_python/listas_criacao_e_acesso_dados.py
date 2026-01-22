"""
Listas podem armazenar de maneira sequencial qualquer tipo de objeto python
Podemos criar listas usando o construtor list, a funcao range ou colocando valores separados por vírgula dentro de colchetes.
Listas são objetos mutáveis

Acessando listas
A lista é uma sequencia, portanto podemos acessar seus dados utilizando índices. Eles são contados a partir de 0

Listas podem conter outras listas (listas aninhadas) - representar tabelas e matrizes

Fatiamento- >Podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o indice inicial e/ou final para acessar
o conjunto. Podemos ainda informar quantas posições o cursor ira pular no acesso

"""

# Criando listas

frutas = ["Pera","Uva","Maça","Laranja"]
carros = [] #cria uma lista vazia
aruan = list("AruanMacena") # este construtor pede somente 1 argumento iterável, neste caso, separará todos os char 
numeros = list(range(10)) #cria uma lista com cada numero de 0 a 9
carro = ["Ferrari","f12","4200000.00","2020","2900","São Paulo","True"]

print(frutas)
print(aruan)
print(carros)
print(numeros)
print(carro)

#acessando listas

print(frutas[0]) #retorna pera

#podemos utilizar indices negativos

print(frutas[-1]) #retorna laranja, ultimo elemento da lista

#criacao de matriz bidimensional

matriz = [
    [1,"a",2],
    [13,"b",4],
    [5,"c",8],
]

print(matriz)
print(matriz[0]) #retorna a primeira linha da matriz
print(matriz[-1]) #retorna a ultima linha da matriz
print(matriz[1][0]) #retona o primeiro elemento da 2ª linha da matriz
print(matriz[-1][-1]) #retorna o ultimo elemento da ultima linha da tabela
"""
#este bloco retorna a ultima coluna da tabela
y=[]
for x in matriz:
    y.append(x[-1])
print(y)
"""

#Fatiamento
