def calculadora_de_imc():

    try:

        pesokg = float(input("Diga ai teu peso em kg: "))
        alturam= float(input("Agora sua altura em metros: "))

        imc = pesokg / (alturam * alturam)

        if imc < 18.5:
            print("Teu IMC é:", round(imc, 2))
            print("Categoria: Abaixo do peso, bora comer um feijãozinho")

        elif imc <= 24.9:
            print("Teu IMC é:", round(imc, 2))
            print("Categoria: Peso normal, tá bom demais!!!")

        elif imc <= 29.9:
            print("Teu IMC é:", round(imc, 2))
            print("Categoria: Sobrepeso, cuidado aii")

        else:
            print("Teu IMC é:", round(imc, 2))
            print("Categoria: Obeso, tu e doidoo!!!!!")

    except ValueError:
        print("Valor errado, coloque só números, exemplo: kg = 70.1 altura = 1.72.")


calculadora_de_imc()