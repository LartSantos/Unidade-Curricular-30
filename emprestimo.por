programa {
  funcao inicio() {

    real valorCasa, salario, prestacao
    inteiro anos, meses

    escreva("Valor da casa: ")
    leia(valorCasa)

    escreva("Seu salario: ")
    leia(salario)

    escreva("Anos para pagar: ")
    leia(anos)

    meses = anos * 12
    prestacao = valorCasa / meses

    escreva("Prestacao mensal: ", prestacao, "\n")

    se (prestacao <= salario * 0.30) {
       escreva("Emprestimo aprovado")
    }
    senao {
       escreva("Emprestimo negado")
    }

  }
}