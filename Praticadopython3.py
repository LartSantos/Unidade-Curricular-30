def controle_financeiro(gastos, mesada):

    total_gasto = sum(gastos)

    if total_gasto <= mesada:
        economizado = mesada - total_gasto
        print("João conseguiu economizar!!!!!! Sobrou R$ KKKKKKKKK", economizado)
    else:
        divida = total_gasto - mesada
        print("João gastou mais do que tinha!!!! Faltou R$ KKKKKKKKKK", divida)

gastos_do_joao = [150, 80, 200, 50, 120]
mesada_do_joao = 500

controle_financeiro(gastos_do_joao, mesada_do_joao)