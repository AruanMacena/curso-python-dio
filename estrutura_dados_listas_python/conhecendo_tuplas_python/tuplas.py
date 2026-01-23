"""
Tuplas
Estruturas parecida com lista. Diferença: Tuplas sao imutaveis
Podemos criar tupla atravez da classe tuple ou colocando valores separados por vírgula de parêntesis

Acesso
Utilizamos o índice, assim como em listas

Tuplas aninhadas
tuplas de tuplas

Métodos da classe tuple:
    ().count -contar quantos elementos tem
    ().index
    len - funcao


"""
#criando tuplas
frutas = ("laranja","caju","banana","uva","pera",)
letras = tuple("python")
numeros = tuple([1,2,3,4])
pais = ("Brasil")

print(frutas)
print(letras)
print(numeros)
print(pais)

#acesso a elementos da tupla
print(frutas[1])

#tupla bidimensional (tupla de tupla)

matriz = ((1,"a",7),
    ("b",3,4),
    (5,"ca","s"),
)

print(matriz[0])
print(matriz[-1])
print(matriz[1][2])
print(matriz[0][-1])
print()

#fatiamento
print(matriz[1:])
print(matriz[::-1])

