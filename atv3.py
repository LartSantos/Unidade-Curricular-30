resposta = input("Você tem carteira de motorista? (S/N): ")

resposta = resposta.upper()

if resposta == "S":
    carteira = True
else:
    carteira = False

print("Você tem carteira?", carteira)
print("O tipo da variável so pode ser:", type(carteira))

