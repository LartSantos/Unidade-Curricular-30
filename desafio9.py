def verificar(n):
    if n > 0:
        return "positivo"
    else:
        if n < 0:
            return "negativo"
        else:
            return "zero"

print(verificar(5))