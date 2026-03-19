def pontuacao_total(pontos, tempo):
    if tempo < 30:
        pontos = pontos + 50
    elif tempo > 100:
        pontos = pontos - 20

    if pontos > 200:
        return "Ai MEu Deus Um ReCoRdE!!!!!"
    else:
        return pontos