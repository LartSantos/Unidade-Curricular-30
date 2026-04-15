def divisao(x, y):
    try:
        resultado = x / y
        return resultado
    except ZeroDivisionError:
        return "Ei, não pode dividir por zero!!!!"

print(divisao(10, 2))
print(divisao(10, 0))