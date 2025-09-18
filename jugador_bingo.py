from carton_bingo import CartonBingo

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carton = CartonBingo()

    def marcar_numero(self, numero):
        self.carton.marcar(numero, self.nombre)

    def ha_ganado(self):
        return self.carton.esta_lleno()