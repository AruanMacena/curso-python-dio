"""
Listas podem armazenar de maneira sequencial qualquer tipo de objeto python
Podemos criar listas usando o construtor list, a funcao range ou colocando valores separados por vírgula dentro de colchetes.
Listas são objetos mutáveis

Acessando listas
A lista é uma sequencia, portanto podemos acessar seus dados utilizando índices. Eles são contados a partir de 0

Listas podem conter outras listas (listas aninhadas) - representar tabelas e matrizes

Fatiamento- >Podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o indice inicial e/ou final para acessar
o conjunto. Podemos ainda informar quantas posições o cursor ira pular no acesso

Iterar listas -> a forma mais comum é a partir do comando "FOR"

Compressao de listas: Gera uma nova lista aplicando alguma midificacao nos elementos de uma lista existente
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
nome = list("Aruan Macena")
print(nome[2:])
print(nome[:3]) # retorna ["A","r"",u"]
print(nome[6:9]) #printa ["M","a","c"]
print(nome[0:6:2]) #printa ["A","u","n"]
print(nome[::]) #retona a lista completas, pois todos os parâmetros estao vazios
print(nome[::-1]) # espelha a sequencia

#Iterando listas

carros = ["gol","celta", "palio"]

for carro in carros:
    print(carro)

#usando a funcao ENUMERATE

for indice,carro in enumerate(carros):
    print(f"indice da lista: {indice} e o objeto é: {carro}")

#Compressão de listas - Filtro versão 1 (ex: quero os valores impares em uma lista e pares em outra)
numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
pares = []
impares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)

# Compressão de listas -Filtro versão 2
numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
pares = [numero for numero in numeros if numero % 2 ==0] # primeira parte-> retorno, segunda parte-> iteracao,  
print(pares)

##Modificando numeros - Versao 1

numeros = [1,2,3,4,5]
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

print(quadrado)

##Modificando numeros - Versao 2

numeros = [1,2,3,4,5]
cubo = [numero**3 for numero in numeros]

print(cubo)