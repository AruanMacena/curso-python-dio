"""
#######Conjuntos#######

-Estrutura de dados set-
É uma coleçao de objetos que tem elementos unicos, sem ser repetidos
Utilizamos sets para representar conjuntos matematicos para eliminar itens duplicados
dentro de objetos iteraveis

***nao garante a ordem.***
set(iteravel)

Acessando dados
Conjuntos em Python nao suportam indexaçao, precisa converter para lista

Iterar conjuntos
podemos iterar utilizando for

funcao enumerate
para saber o0 indice do elemento

metodos da classe set
(operacoes de conjuntos)

{}.union
junta os 2 conjuntos

{}.intersection
parte dos 2 conjuntos que são iguais

{}.difference
a diferenca dos conjuntos

{}.simmetric_difference
todos os elementos que não estao na interseccao

{}.issubset
metodo que retorna se o objeto é um subconjunto do argumento

{}.issuperset
metodo que retorna se o objeto engloba todos os itens do argumento

{}.isdisjoint
conjunto onde eles não se tocam (sem elementos em comum)

{}.add
passo um elemento, e se ele nao existir, ele é adicionado

{}.clear
limpa todo o set

{}.copy
gera uma copia do conjunto

{}.discart
elimina objetos do set, se passar um valor que nao existe ele nao da erro

{}.pop 
tira os valores da lista (valores da frente)

{}.remove
diferenca entre remove e discart -> ele da erro se o elemento nao existe

len (funcao)
retira o tamanho do conjunto

in
->esta
"""

x= set([1,2,3,4,1,2,4,5,6,7,8])         #{1, 2, 3, 4, 5, 6, 7, 8}
y= set("Abacaxi")                       #{'a', 'A', 'i', 'c', 'b', 'x'}
z= set(("palio","gol","celta","palio")) #{'gol', 'celta', 'palio'}

aa = {"python","java","python"}
print(x)
print(y)
print(z)
print(aa)

#iteracao

z= set(("palio","gol","celta","palio"))
for carro in z:
    print(carro)

#enumerate
z= set(("palio","gol","celta","palio"))
for indice,carro in enumerate(z):
    print(f"{indice}:{carro}")

#union
conjunto_a = {1,2}
conjunto_b = {3,4}
print(conjunto_a.union(conjunto_b))

#intersection
conjunto_a = {1,2,3,4,5}
conjunto_b = {3,4,5,6,7,8}

print(conjunto_a.intersection(conjunto_b))

#difference
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#symmetric_difference
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.symmetric_difference(conjunto_b))

#issubset
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
print(conjunto_b.issubset(conjunto_a))
print(conjunto_a.issubset(conjunto_b))

#issuperset
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
print(conjunto_b.issuperset(conjunto_a))
print(conjunto_a.issuperset(conjunto_b))

#isdisjoint
print()
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

# add
print()
sorteio = {1,23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

#clear
conjunto_a = {1,2,3,4,5}
print(conjunto_a.clear)

#copy
sorteio = {1,23}
sorteio2 = sorteio.copy()
print(f"{id(sorteio)}:{id(sorteio2)}")

#discart
print()
numeros = {1,2,3,4,5,6,7,8,9,0}
numeros.discard(1)
numeros.discard(45)
print(numeros)

#remove
print()
numeros = {1,2,3,4,5,6,7,8,9,0}
numeros.remove(1)
#numeros.remove(45) #da erro se tentar tirar valor que nao esta no conjunto
print(numeros)

#pop
numeros = {1,2,3,4,5,6,7,8,9,0}
numeros.pop()
numeros.pop()
numeros.pop()
print(numeros)

#len
print()
numeros = {1,2,3,4,5,6,7,8,9,0}
print(len(numeros))

#in
print()
numeros = {1,2,3,4,5,6,7,8,9,0}
print(1 in numeros)
print(10 in numeros)

