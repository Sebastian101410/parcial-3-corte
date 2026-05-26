# Gestor del Mundial 

equipos = ["Argentina", "Colombia", "Polonia", "Arabia"]
puntos = [0, 0, 0, 0]

for partido in range(6):
    print(f"\nPartido {partido+1}")
    print("1-Argentina  2-Colombia  3-Polonia  4-Arabia")
    e1 = int(input("Equipo 1: ")) - 1
    e2 = int(input("Equipo 2: ")) - 1
    g1 = int(input(f"Goles {equipos[e1]}: "))
    g2 = int(input(f"Goles {equipos[e2]}: "))

    if g1 > g2:
        puntos[e1] += 3
    elif g2 > g1:
        puntos[e2] += 3
    else:
        puntos[e1] += 1
        puntos[e2] += 1

print("\n--- Tabla Final ---")
for i in range(len(equipos)):
    print(f"{equipos[i]}: {puntos[i]} puntos")
