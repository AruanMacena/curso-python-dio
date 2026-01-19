"""
Operadores logicos
Expressões booleanas

E  (and)        - expressão verdadeira se todos forem verdadeiras
OU (or)         - expressão verdadeira se pelo menos 1 for verdadeiro
Negação (not)   - inverso do resultado anterior

Parenteses tmb servem para delimitar a precedência


"""
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Tres métodos de fazer a mesma comparação, facilitando a visualização

exp = saldo >= saque and saque <=limite or conta_especial and saldo >= saque

exp2 = (saldo >=saque and saque <=limite) or (conta_especial and saldo>=saque)

print(exp)
print(exp2)

saldo_suficiente = saldo >= saque and saque <=limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

print(saldo_suficiente or conta_especial_com_saldo_suficiente)