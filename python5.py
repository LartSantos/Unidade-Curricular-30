def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Tá Bloqueado Bobão"
    
    if usuario == "admin" and senha == "1234":
        return "Acesso total aeeeee"
    elif usuario == "admin" and senha != "1234":
        return "Senha incorreta tenta de novo ai namoral"
    else:
        return "Usuário inválido KKKKKKKKK"