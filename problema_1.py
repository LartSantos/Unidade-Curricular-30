def soma_segura(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        
        print("Entrada errada meu nobre")
        return 0

print(soma_segura(3, 5))
print(soma_segura("oieeee", 5))