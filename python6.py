def lancar_foguetinho(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente que pena..."
    
    if clima != "bom":
        return "Clima desfavorável num vai dar não"
    
    if sistema_ok == False:
        return "Falha no sistema SOCORROOOOOO"
    
    return "Lançamento autorizado pode ir chefe"