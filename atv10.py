notas = [6.5, 7.0, 8.2, 5.9, 9.1, 7.5, 4.3]

contador = 0

for nota in notas:
    if nota > 7:
        contador = contador + 1


print("Quantidade de notas que ficaram acima de 7:", contador)