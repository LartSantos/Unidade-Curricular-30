def rank_dojogador(pontos, derrotas):
    ponto_final = pontos - (derrotas * 10)

    if ponto_final < 0:
        return "Banido"
    elif ponto_final < 100:
        return "Bronze"
    elif ponto_final < 300:
        return "Prata"
    elif ponto_final < 600:
        return "Ouro"
    else:
        return "Diamante"