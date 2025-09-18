from juego_bingo import JuegoBingo

if __name__ == "__main__":
    nombres = input("Ingrese los nombres de los jugadores separados por coma: ").split(",")
    nombres = [n.strip() for n in nombres if n.strip()]
    if len(nombres) < 2:
        print("Se necesitan al menos 2 jugadores.")
    else:
        juego = JuegoBingo(nombres)
        juego.iniciar_juego()