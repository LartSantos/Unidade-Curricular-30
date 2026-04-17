def somador_de_compras():


    tudo = 0


    valor = float(input("Diga ai o valor do item ou so coloca 0 para sair: "))


    while valor!= 0:

        total = total + valor

        valor = float(input("Diga ai o valor do item ou so coloca 0 para sair:"))

    print("Tudo da sua compra deu: R$", total)


somador_de_compras()