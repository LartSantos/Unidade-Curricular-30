estatura = float(input("Digite sua altura:"))
estatura = estatura * 100

print(f"Sua altura é de {estatura}")
print("Sua altura é de:", estatura )


nome = input("Digite seu nome:")
idade = 17

texto = "Meu nome é {} e tenho {} anos. ".format(nome, idade)
texto = "Meu nome é {n} e tenho {i} anos. ".format(n=nome, i=idade)
print(texto)    