while True:


    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sairrrrr")

    opcaoo = input("Escolha ai: ")

    if opcaoo == "5":
        print("Você saiu da calculadora TCHAUUUUUUUUUU")
        print("Cabou-se")
        break

    n1 = float(input("Digite ai o primeiro número: "))
    n2 = float(input("Digite agora o segundo número: "))

    if opcaoo == "1":
        print(n1 + n2)

    elif opcaoo == "2":
        print(n1 - n2)

    elif opcaoo == "3":
        print(n1 * n2)

    elif opcaoo == "4":
        print(n1 / n2)

    else:
        print("Opção errada, pelo amor de Deus né")