import random


numeros = [91, 34, 67, 15, 82]

print("Lista original:", numeros)


numeros.sort()
print("Ordem crescente:", numeros)


numeros.sort(reverse=True)
print("Ordem decrescente:", numeros)



dados = [80, 7, 10, 9, 19]

random.shuffle(dados)

print("Lista embaralhada:", dados)



lista3 = [12, 45, 3, 27, 90, 8]

print("Lista 3 original:", lista3)

lista3.sort()
print("Lista 3 crescente:", lista3)

lista3.sort(reverse=True)
print("Lista 3 decrescente:", lista3)

random.shuffle(lista3)
print("Lista 3 embaralhada:", lista3)