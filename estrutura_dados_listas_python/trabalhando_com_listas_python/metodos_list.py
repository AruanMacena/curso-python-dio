"""
Métodos da classe list

[].append
adiciona um objeto a lista

[].clear
limpar a lista

[].copy
cria uma copia do objeto

[].count
conta o numero de vezes que o objeto aparece na lista

[].extend
junta novos elementos (junta 2 listas)

[].index
onde ocorre a primeira ocorrencia de um objeto dentro da lista

[].pop
remove o ultimo elemento da lista, se for passo um argumento, ele remove o elemento do índice do argumento

[].remove
voce remove o objeto passando o objeto como parametro

[].reverse
faz o espelhamento da lista

[].sort
ordena a lista

[].len
ve o tamanho da lista

[].sorted
tmb ordena iteráveis
"""

#append
lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,20])
print(lista)

#clear
lista.clear()
print(lista)

#copy
lista = [1,"Python",[40,30,20]]
lista2 = lista.copy() #cria um novo objeto, que é uma cópia da lista
print(id(lista),id(lista2))

"""
# Isso só muda o ponteiro, nao cria novo objeto
x = lista
y = lista

x[0] = 2

print(f"{x}é igual a {y}")
"""
#count

cores=["vermelho","azul","amarelo","vermelho","vermelho"]

print(cores.count("vermelho"))

#extend
linguagens = ["python","java","C"]
linguagens.extend(["js","csharp","cplus"])
print(linguagens)

#index

linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus'] # nao retorna todas as ocorrencias, somente a primeira vez que um objeto aparece na lista
print(linguagens.index("java"))

#pop

linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
linguagens.pop(0)
linguagens.pop()
print(linguagens)

#remove
linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
linguagens.remove("C")
print(linguagens)

#reverse
linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
linguagens.reverse()
print(linguagens)

#sort
linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)
linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
linguagens.sort(key=lambda x: len(x))
print(linguagens)
linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

#len -função
linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
print(len(linguagens))

#sorted - parecido com o sort, a diferenca é que ele é uma função e não um método
linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
sorted(linguagens, key=lambda x: len(x))
print(linguagens)

linguagens = ['python', 'java', 'C', 'java', 'csharp', 'cplus']
sorted(linguagens, key=lambda x: len(x), reverse=True)
print(linguagens)