def calcular_media():

    notas = []

    for numero_da_nota in range(3):

        try:
            nota = float(input("Digite uma nota: "))
            notas.append(nota)

        except ValueError:
            print("Eiiiiii não é um número! As notas devem ser numéricas.")
            return

    media = sum(notas) / 3

    print("A média final desse aluno é:", round(media, 2))


calcular_media()