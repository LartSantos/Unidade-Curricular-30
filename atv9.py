valor = float(input("Digite ai o valor da compra: "))

if valor > 500:
    desconto = valor * 0.20
    valor_final = valor - desconto
elif valor >= 200:
    desconto = valor * 0.10
    valor_final = valor - desconto
else:
    valor_final = valor

print("O valor final da tua compra é:", valor_final)