nome = input("DIgite seu nome: ")
if len(nome) >20:
   print("Seu nome é grande, ele possui mais de 20 letrinhas")
print(f"Ele possui {len(nome)} caracteres.")


valor = int(input("Digite um número:  "))
if valor % 2 == 0:
   print("O numero é par")
else:
   print("O número e ímpar")

nota == float(input("Digite sua nota"))

if nota >= 10:
   print("Passou")
elif nota == 7:
   print("Pode melhorar")
else:
   print("Recuperação")

idade = int(input("Digite sua idade: "))
if idade >= 16 and idade <= 69:
   print("Faixa permitida: ")
else:
   print("Fora da faixa")