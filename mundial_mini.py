# Grupo del mundial

equipos = {"Colombia":0, "Brasil":0, "Argentina":0, "Uruguay":0}

for i in range(3):

    eq1 = input("Equipo 1: ")
    g1 = int(input("Goles: "))

    eq2 = input("Equipo 2: ")
    g2 = int(input("Goles: "))

    if g1 > g2:
        equipos[eq1] += 3

    elif g2 > g1:
        equipos[eq2] += 3

    else:
        equipos[eq1] += 1
        equipos[eq2] += 1

print("\nTABLA DE POSICIONES")

for equipo, puntos in equipos.items():
    print(equipo, "-", puntos, "puntos")