def calcular_compra():

    try:
        preco_do_primeiro_produto = float(input("Digite ai o preço do primeiro produto: "))

        preco_do_segundo_produto = float(input("Digite ai agora o preço do segundo produto: "))

        total_da_compra = preco_do_primeiro_produto + preco_do_segundo_produto

        print("O valor total da compra é de  R$", round(total_da_compra, 2))

    except ValueError:
        print("Isso não é um númerooooo! Os preços devem ser numéricos.")


calcular_compra()