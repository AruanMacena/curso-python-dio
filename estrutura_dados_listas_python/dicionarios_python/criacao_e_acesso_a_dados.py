"""
Criaçao e acesso a dados

Conjunto nao-ordenado de pares chave:valor, onde as chaves são unicas em uma dada instância do dicionario.
Dicionários sao delimitados por chaves: {}, e contem uma lista de pares chave:valor separadas por vírguilas

Para ser chave no python, tem que ser um valor imutavel como strings e tuplas

Acessar os dados:
utilizar o valor da chave para achar o valor

Dicionarios aninhados
Podem adicionar qualquer tipo de objeto, podemos ter um dicionario dentro de um dicionario.
A chave tem que ser imutavel, mas o objeto pode ser qualquer coisa

A forma mais comum para percorrer os dados de um dicionario é utilizando o comando FOR
"""
#criando dicionarios
pessoa1 = {"nome":"Guilherme","idade": 28}
print(pessoa1)
pessoa2 = dict(nome="Guilherme", idade = 28)
print(pessoa2)
pessoa2["telefone"] = "3333-1234"
print(pessoa2)

#acessando valores no dicionario

dados = {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'}

print(dados['nome'])
print(dados["idade"])

#podemos sobre escrever os dados

dados["nome"] = "Aruan Macena"
print(dados)

#dicionario aninhados

contatos = {
    "aruan.macena@gmail.com":{"nome":"Aruan Macena","telefone":"16-981885128"},
    "pedro.cabral@hotmail.com":{"nome":"Pedro","telefone":"16-984557414"},
    "pipoka.cabrera.gls@gmail.com":{"nome":"Luis","telefone":"16-997514414"},
    "antoni_bandeira@bol.com.br":{"nome":"Antonio","telefone":"16-965548774"}
}

print(contatos["pipoka.cabrera.gls@gmail.com"]["nome"]) #exemplo de busca dentro de um dicionário aninhado

#Percorrendo o dicionario
print()
for chave in contatos:
    print(chave,contatos[chave]) # nao é a melhor forma
print()
for chave,valor in contatos.items(): #metodo do dicionario
    print(chave,valor)

print()
print(type(contatos))