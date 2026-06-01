"""

Old style % -> %s (strings) %d (inteiros) %f (ponto flutuante) -- %()

Método format -> {} ao fim da string .format(variaveis) . Podemos indicar o indice da lista para mudar a ordem das variaveis,
util quando precisamos colocar varias vezes a mesma variável
Podemos tmb passar o argumento de forma nomeada

f-string -> passamos diretamente o nome da variável, pode ser formatado de uma maneira bem simplificada

"""

nome = "Aruan Macena"
idade = 35
profissao = "programador"
linguagem = "python"
saldo =45.432

dados= {"nome": "Aruan da Silva Macena","idade":35}

print("Nome: %s Idade: %d anos" %(nome,idade)) # old style

print("Nome: {} Idade: {} anos" .format(nome,idade)) # método format

print("Nome: {1} Idade: {0} anos" .format(idade,nome))

print("Nome: {name} Idade: {age} anos" .format(age=idade,name=nome))
print("Nome: {nome} Idade:{idade} anos".format(**dados)) #utilizando um dicionario

#utilizando o f-strings

print(f"Nome: {nome} Idade {idade} anos")

print(f"Nome: {nome} Idade {idade} anos. Saldo:{saldo:10.1f}")