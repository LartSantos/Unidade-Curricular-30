paes = int(input())
doces = int(input())
bolos = int(input())

pontos_dos_paes = paes * 1
pontos_dos_doces = doces * 2
pontos_dos_bolos = bolos * 3

total = pontos_dos_paes + pontos_dos_doces + pontos_dos_bolos

premio = "N"

if total >= 100:
    premio = "P"

if total >= 120:
    premio = "D"

if total >= 150:
    premio = "B"

print(premio)