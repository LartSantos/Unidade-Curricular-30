def resumo_dasnotas(nota):


    soma = 0
    maior = nota[0]
    menor = nota[0]


    for n in nota:
        soma = soma + n

        if n > maior:
            maior = n

        if n < menor:
            menor = n

    media = soma / len(nota)

    return soma, media, maior, menor



nota = [7, 8.5, 6, 9, 10]

resultado = resumo_dasnotas(nota)

print("Soma:", resultado[0])
print("Média:", resultado[1])
print("Maior:", resultado[2])
print("Menor:", resultado[3])