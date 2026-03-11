idade_texto = input("Digite a idade do grande atleta: ")

idade = int(idade_texto)


if idade < 12:
    categoria = "Infantil (Hello world) "
elif idade >= 12 and idade < 18:
    categoria = "Juvenil"
elif idade >= 18 and idade < 60:
    categoria = "Adulto"
else:
    categoria = "Sênior"


print("Sua categoria é:", categoria)

print("Bem-vindo à competição de natação! AEEEEEEEEEEEEEE!")