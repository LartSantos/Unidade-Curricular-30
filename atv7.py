# lista de vendas (exemplo)
vendas = [10, 15, 20, 7, 8, 13, 22]

# variável pra guardar a soma
soma_pares = 0

# passando por cada número da lista
for numero in vendas:
    # verificando se é par
    if numero % 2 == 0:
        soma_pares += numero  # soma só os pares

# mostrando o resultado
print("A soma dos números pares é:", soma_pares)