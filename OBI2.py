infectados_no_dia_zero = int(input())
fator_r = int(input())
meta = int(input())

total = infectados_no_dia_zero
novos = infectados_no_dia_zero
dias = 0

while total < meta:
    novos = novos * fator_r
    total = total + novos
    dias = dias + 1

print(dias)