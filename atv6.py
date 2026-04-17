def calcular_tempcelsius():


    temp= [32.5, 28.0, 30.1, 35.2, 29.8, 31.0, 27.5]
    soma = 0


    for temp in temp:
        soma = soma + temp

    media = soma / 7


    print("E as temperaturas dessa semana foram:", temp)
    print("A média das temperaturas foiii:", round(media, 2), "graus celsius")


calcular_tempcelsius()