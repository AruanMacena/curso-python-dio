# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = 100
cupom = "DESCONTO20"


# TODO: Aplique o desconto se o cupom for válido:

  
x=preco-((descontos[cupom])*preco)

print(x)