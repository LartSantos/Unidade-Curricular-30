META = 100
doacoes = []

def pedir_quantidade():
    while True:
        try:
            valor = float(input("Quantidade (kg): "))
            if valor > 0:
                return valor
            else:
                print("Digite um valor maior que 0")
        except:
            print("Digite apenas números")

while True:
    print("\n--- SISTEMA DE DOAÇÕES ---")
    print("1 - Registrar doação")
    print("2 - Ver relatório")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("\n--- NOVA DOAÇÃO ---")
        
        nome = input("Nome do doador: ")
        alimento = input("Alimento: ")

        print("Categoria:")
        print("1 - Grãos")
        print("2 - Enlatados")
        print("3 - Higiene")
        print("4 - Outros")

        cat = input("Escolha: ")

        if cat == "1":
            categoria = "Grãos"
        elif cat == "2":
            categoria = "Enlatados"
        elif cat == "3":
            categoria = "Higiene"
        else:
            categoria = "Outros"

        quantidade = pedir_quantidade()

        # lista simples ao invés de dicionário
        doacoes.append([nome, alimento, quantidade, categoria])

        print("Doação registrada!")

    elif opcao == "2":
        print("\n--- RELATÓRIO ---")

        if len(doacoes) == 0:
            print("Nenhuma doação ainda.")
        else:
            total = 0

            for d in doacoes:
                print(d[0], "doou", d[2], "kg de", d[1], "-", d[3])
                total = total + d[2]

            print("\nTotal:", total, "kg")

            if total < META:
                print("Faltam", META - total, "kg")
            else:
                print("Meta atingida!")

    elif opcao == "3":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")