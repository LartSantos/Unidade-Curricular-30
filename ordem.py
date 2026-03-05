import random

numeros = [10, 33, 99, 67, 77]
print("Lista oficial:", numeros)

#sort crescente
numeros.sort()
print("Após sort():", numeros)

#sort decrescente
numeros.sort(reverse=True)
print("Após sort():", numeros)

dados = [1, 2, 3, 4, 5]
random.shuffle(dados)
print("Embaralhar: ", dados)

