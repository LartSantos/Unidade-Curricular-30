import random


numero = random.randint(1, 100)
tentativas = 0
acertou = False

while acertou == False:
    palpite = int(input("Digite um número de 1 a 100: "))
    tentativas = tentativas + 1

    if palpite < numero:
        print("maior")
    elif palpite > numero:
        print("menor")
    else:
        print("Acertou!")
        acertou = True

print("Tentativas:", tentativas)



numeros = []
for i in range(8):
    n = int(input("Digite um número: "))
    numeros.append(n)


print("\nNúmeros repetidos:")

for num in numeros:
    if numeros.count(num) > 1:
        print(num, "apareceu", numeros.count(num), "vezes")