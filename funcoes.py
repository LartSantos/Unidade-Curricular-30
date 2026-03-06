notas = [7, 5 , 8.0, 9.5 , 6.0, 8.5, ]
print("Ntas: ", notas)

print("Menor nota:", min(notas))
print("Menor nota ", max (notas))
print("Soma :", sum(notas))
print("Media:", sum(notas) / len(notas))

nomes = ["Adriana", "Barbara", "Carla", "Daniel"]
print("Usando FOR simples") #apenas elementos 

for nome in nomes:
    print (f"Olá ,{nome}")

for indice, nome in enumerate (nomes):
    print (f"posição {indice}: {nomes} ")

original = ["A","B","C"]
copia = list (original)

print("Original:" , original)
print("Cópia:", copia)
print("São iguais:" , original == copia)

copia.append("D")
print("Original:" , original)
print("Cópia:", copia)
print("São iguais:" , original == copia)