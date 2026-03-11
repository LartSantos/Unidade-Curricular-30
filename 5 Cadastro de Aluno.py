nome_doaluno = input("Digite ai o nome completo do aluno: ")

matricula_texto = input("Digite ai a matrícula do aluno: ")
matricula = int(matricula_texto)

nota1_texto = input("Digite a primeira nota: ")
nota1 = float(nota1_texto)

nota2_texto = input("Digite a segunda nota: ")
nota2 = float(nota2_texto)

media = (nota1 + nota2) / 2

print("----- RELATÓRIO DO ALUNO DE GABY -----")
print("Nome:", nome_doaluno)
print("Matrícula:", matricula)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média Final fica:", media)
print("------------------------------")