"""

São utilizadas para repetir um trecho de codigo um determinado numero de vezes. Esse numero pode ser
conhecido previamente ou determinado através de uma expressão lógica

FOR -> utilizado para percorrer um objeto iteravel, devemos saber previamente o numero de vezes que será executado

FOR/ELSE -> o else,embora nao comum, no comando for é utilizado para percorrer uma vez ao final do laço

Range -> funçao built-in do Python que é utilizada para produzir uma sequencia de números inteiros a partir de um
início (inclusivo) para um fim(exclusivo) range(start,stop,[step]) -> range object

WHILE -> repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de 
vezes que nosso bloco de cógigo deve ser executado

BREAK -> para a execuçao do laço

CONTINUE -> pular a execução de uma ou mais iterações

"""

#exemplo de utilização do laço de repetição FOR

texto = "qwertyuiopasdfghjklçzxcvbnm"
VOGAIS = "AEIOU"

for letra in texto: #letra age como uma variavel que recebe um valor a cada iteração
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print()

#exemplo da função range

print(list(range(4))) # printa [0, 1, 2, 3]
print(list(range(0,11))) # printa [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0,100,7))) # printa [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

# for com a função range

for numero in range(0,51,5):
    print(numero, end=" ") #printa 0 5 10 15 20 25 30 35 40 45 50

#exemplo com while

opcao =-1


while opcao !=0:
    opcao = int(input("\n[1]sacar \n[2]Extrato\n[0]Sair\n"))

    if opcao ==1:
        print("sacando...")
    elif opcao ==2:
        print("exibindo o extrato...")

#break

while True:
    numero = int(input("informe um numero"))

    if numero == 10:
        break

    print(numero)

#continue                
while True:
    numero = int(input("informe um numero"))

    if numero == 10:
        break

    if numero == 5:
        continue

    print(numero, end=" ")