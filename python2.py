def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente KKKKKKKKKKKKK Muito pobre"
    else:
        if saque > 1000:
            taxa = saque * 0.02
            saque = saque + taxa

        saldo_quesobrou = saldo - saque
        return saldo_quesobrou